import math
import re

from .input_handlers import validate_input

CALORIES_PER_G_FAT = 9
CALORIES_PER_G_CARB = 4
CALORIES_PER_G_PROTEIN = 4
CALORIES_PER_KG_BODY_FAT = 7700  # 3,500 kcal/lb
MAX_KG_LOSS_PER_WEEK = -0.907185  # -2 lbs
MAX_KG_GAIN_PER_WEEK = 0.907185  # 2 lbs
MAX_PERCENTAGE_BELOW_BMR = 0.2
GRAM_PROTEIN_LEAN_BODY_MASS_KG = 2.2
MAX_GRAM_PROTEIN_LEAN_BODY_MASS_KG = 3
GRAM_SATURATED_FAT_LEAN_BODY_MASS_KG = 0.15
MIN_FAT_G_LBM_KG = 0.75
MIN_FAT_SAFETY_FACTOR_PERCENTAGE = 0.1
OMEGA3_INTAKE_RANGE = (2, 6)  # Grams
LINOLEIC_ACID_AI_AGE_THRESHOLD = 50  # Years
LINOLEIC_ACID_AI = {
    'm': (17, 14),
    'f': (12, 11),
}
LBM_POP_DIST = (34, 72)  # 75-159 lbs
CHANGE_UNITS = ('%', 'kg', 'lbs')
VALID_CHANGE_UNITS = ('pct', '%', 'kg', 'lbs')
HEIGHT_UNITS = ('cm', 'in')
WEIGHT_UNITS = ('kg', 'lbs')


def lbs_to_kg(lbs: float) -> float:
    return lbs / 2.205


def kg_to_lbs(kgs: float) -> float:
    return kgs / 0.4536


def cm_to_inches(cms: float) -> float:
    return cms * 0.393701


def inches_to_cm(inches: float) -> float:
    return inches * 2.54


def cm_to_meters(cms: float) -> float:
    return cms / 100


def calculate_bmr(height, weight, age, sex):
    if sex == 'm':
        return int(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))
    elif sex == 'f':
        return int(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age))


def calculate_bmi(height, weight):
    meters = cm_to_meters(height)
    return weight / meters ** 2


def bmi_to_bfp(bmi, sex, age):
    if sex == 'm':
        if age <= 15:
            return (1.51 * bmi) - (0.70 * age) - (3.6 * 1) + 1.4
        else:
            return (1.20 * bmi) + (0.23 * age) - (10.8 * 1) - 5.4
    elif sex == 'f':
        if age <= 15:
            return (1.51 * bmi) - (0.70 * age) - (3.6 * 0) + 1.4
        else:
            return (1.20 * bmi) + (0.23 * age) - (10.8 * 0) - 5.4


def calculate_fatty_acids(sex, age, lean_body_mass):
    ratio = (lean_body_mass - LBM_POP_DIST[0]) / (LBM_POP_DIST[1] - LBM_POP_DIST[0])
    omega3 = round(OMEGA3_INTAKE_RANGE[0] + (ratio * (OMEGA3_INTAKE_RANGE[1] - OMEGA3_INTAKE_RANGE[0])), 2)

    if omega3 < OMEGA3_INTAKE_RANGE[0]:
        omega3 = OMEGA3_INTAKE_RANGE[0]
    elif omega3 > OMEGA3_INTAKE_RANGE[1]:
        omega3 = OMEGA3_INTAKE_RANGE[1]

    if age < LINOLEIC_ACID_AI_AGE_THRESHOLD:
        linoleic_acid = LINOLEIC_ACID_AI[sex][0]
    else:
        linoleic_acid = LINOLEIC_ACID_AI[sex][1]

    saturated_fat = math.ceil(lean_body_mass * GRAM_SATURATED_FAT_LEAN_BODY_MASS_KG)

    total = math.ceil(lean_body_mass * MIN_FAT_G_LBM_KG * (1 + MIN_FAT_SAFETY_FACTOR_PERCENTAGE))
    total_essential = omega3 + linoleic_acid + saturated_fat

    if total < total_essential:
        total = total_essential

    return total, omega3, linoleic_acid, saturated_fat


def calculate_protein(lean_body_mass, extra_calories, split):
    remaining_calories = 0

    protein_grams_per_kg_to_reach_limit = MAX_GRAM_PROTEIN_LEAN_BODY_MASS_KG - GRAM_PROTEIN_LEAN_BODY_MASS_KG
    protein_grams_to_limit = protein_grams_per_kg_to_reach_limit * lean_body_mass
    protein_calories_to_limit = protein_grams_to_limit * CALORIES_PER_G_PROTEIN

    calories_per_macro = extra_calories / split
    if calories_per_macro > protein_calories_to_limit:
        protein_calories_to_add = protein_calories_to_limit
        remaining_calories = calories_per_macro - protein_calories_to_limit
    else:
        protein_calories_to_add = calories_per_macro

    return protein_calories_to_add, remaining_calories, calories_per_macro


def calculate_macros(tdee, distribution, change, change_units, weight, weight_units, body_fat_percentage, height,
                     height_units,
                     sex, age):

    validate_input(tdee, distribution, change, change_units, weight, weight_units, body_fat_percentage, height,
                   height_units,
                   sex, age)

    # Convert to kg
    if weight_units in ['lb', 'lbs', 'pounds']:
        weight = lbs_to_kg(weight)

    # Convert to cm
    if height_units in ['in', 'inches']:
        height = inches_to_cm(height)

    if body_fat_percentage:
        lean_body_mass = weight * (1 - body_fat_percentage / 100)
    else:
        bmi = calculate_bmi(height, weight)
        body_fat_percentage = bmi_to_bfp(bmi, sex, age)
        body_fat_percentage = round(body_fat_percentage, 2)
        lean_body_mass = weight * (1 - body_fat_percentage / 100)

    protein_grams = math.ceil(lean_body_mass * GRAM_PROTEIN_LEAN_BODY_MASS_KG)  # Set Minimum Protein
    fat_grams, omega3_grams, linoleic_acid_grams, saturated_fat_grams = calculate_fatty_acids(sex, age, lean_body_mass)

    protein_calories = protein_grams * CALORIES_PER_G_PROTEIN
    fat_calories = fat_grams * CALORIES_PER_G_FAT

    if change_units in ['pct', '%']:
        weight_change = weight * (change / 100)
    elif change_units in ['lbs', 'kg']:
        weight_change = change
    else:
        raise ValueError('Unrecognized change units')

    if weight_change < MAX_KG_LOSS_PER_WEEK:  # Max loss safety cap
        weight_change = MAX_KG_LOSS_PER_WEEK

    elif weight_change > MAX_KG_GAIN_PER_WEEK:  # Max gain safety cap
        weight_change = MAX_KG_GAIN_PER_WEEK

    daily_calorie_change = weight_change * CALORIES_PER_KG_BODY_FAT / 7
    daily_calories = int(tdee + daily_calorie_change)

    bmr = calculate_bmr(height, weight, age, sex)
    calories_lower_limit = bmr * (1 - MAX_PERCENTAGE_BELOW_BMR)

    if daily_calories < calories_lower_limit:
        daily_calories = calories_lower_limit

    warn = False
    if daily_calories < bmr:
        warn = True

    extra_calories = daily_calories - protein_calories - fat_calories
    if extra_calories < 0:
        extra_calories = 0

    carb_grams = 0
    if extra_calories:
        if distribution == 1:  # All Protein
            protein_grams += math.ceil(extra_calories / CALORIES_PER_G_PROTEIN)
        elif distribution == 2:  # All Carbs
            carb_grams = math.ceil(extra_calories / CALORIES_PER_G_CARB)
        elif distribution == 3:  # All Fat
            fat_grams += math.ceil(extra_calories / CALORIES_PER_G_FAT)
        elif distribution == 4:  # Mix Carbs & Fat
            carb_grams = math.ceil(extra_calories / 2 / CALORIES_PER_G_CARB)
            fat_grams += math.ceil(extra_calories / 2 / CALORIES_PER_G_FAT)
        elif distribution == 5:  # Mix Fat & Protein
            protein_calories_to_add, remaining_calories, calories_per_macro = calculate_protein(lean_body_mass,
                                                                                                extra_calories, 2)

            fat_grams += math.ceil((remaining_calories + calories_per_macro) / CALORIES_PER_G_FAT)
            protein_grams += math.ceil(protein_calories_to_add / CALORIES_PER_G_PROTEIN)
        elif distribution == 6:  # Mix Carbs & Protein
            protein_calories_to_add, remaining_calories, calories_per_macro = calculate_protein(lean_body_mass,
                                                                                                extra_calories, 2)

            carb_grams = math.ceil((remaining_calories + calories_per_macro) / CALORIES_PER_G_CARB)
            protein_grams += math.ceil(protein_calories_to_add / CALORIES_PER_G_PROTEIN)
        elif distribution == 7:  # Mix Carbs, Fat, & Protein
            protein_calories_to_add, remaining_calories, calories_per_macro = calculate_protein(lean_body_mass,
                                                                                                extra_calories, 3)

            additional_macro_calories = calories_per_macro + (remaining_calories / 2)

            carb_grams = math.ceil(additional_macro_calories / CALORIES_PER_G_CARB)
            fat_grams += math.ceil(additional_macro_calories / CALORIES_PER_G_FAT)
            protein_grams += math.ceil(protein_calories_to_add / CALORIES_PER_G_PROTEIN)

    protein_calories = int(protein_grams * CALORIES_PER_G_PROTEIN)
    fat_calories = int(fat_grams * CALORIES_PER_G_FAT)
    omega3_calories = int(omega3_grams * CALORIES_PER_G_FAT)
    linoleic_acid_calories = int(linoleic_acid_grams * CALORIES_PER_G_FAT)
    saturated_fat_calories = int(saturated_fat_grams * CALORIES_PER_G_FAT)
    carb_calories = int(carb_grams * CALORIES_PER_G_CARB)

    total_calories = protein_calories + fat_calories + carb_calories
    caloric_change = total_calories - tdee
    caloric_percentage_change = round((total_calories - tdee) / tdee * 100, 2)

    # Percentages
    protein_percentage = round(protein_calories / total_calories * 100, 2)
    fat_percentage = round(fat_calories / total_calories * 100, 2)
    omega3_percentage = round(omega3_calories / total_calories * 100, 2)
    linoleic_acid_percentage = round(linoleic_acid_calories / total_calories * 100, 2)
    saturated_fat_percentage = round(saturated_fat_calories / total_calories * 100, 2)
    carb_percentage = round(carb_calories / total_calories * 100, 2)

    # Lean Body Mass
    lean_body_mass_lbs = round(kg_to_lbs(lean_body_mass), 2)
    lean_body_mass = round(lean_body_mass, 2)

    # Grams / LBM
    protein_grams_kg_lbm = round(protein_grams / lean_body_mass, 2)
    protein_grams_lbs_lbm = round(protein_grams / lean_body_mass_lbs, 2)

    macros = {
        'protein': {
            'grams': {
                'total': protein_grams,
                'lean_body_mass': {
                    'kg': protein_grams_kg_lbm,
                    'lbs': protein_grams_lbs_lbm,
                }
            },
            'calories': protein_calories,
            'percentage': protein_percentage,
        },
        'fat': {
            'total': {
                'grams': fat_grams,
                'calories': fat_calories,
                'percentage': fat_percentage,
            },
            'omega3': {
                'grams': omega3_grams,
                'calories': omega3_calories,
                'percentage': omega3_percentage,
            },
            'linoleic_acid': {
                'grams': linoleic_acid_grams,
                'calories': linoleic_acid_calories,
                'percentage': linoleic_acid_percentage,
            },
            'saturated_fat': {
                'grams': saturated_fat_grams,
                'calories': saturated_fat_calories,
                'percentage': saturated_fat_percentage,
            }
        },
        'carb': {
            'grams': carb_grams,
            'calories': carb_calories,
            'percentage': carb_percentage,
        }
    }

    data = {
        'macros': macros,
        'stats': {
            'metabolism': {
                'total_calories': total_calories,
                'caloric_change': caloric_change,
                'caloric_percentage_change': caloric_percentage_change,
                'tdee': tdee,
                'basal_metabolic_rate': bmr,
            },
            'body_composition': {
                'lean_body_mass': {
                    'kg': lean_body_mass,
                    'lbs': lean_body_mass_lbs,
                },
                'body_fat_percentage': body_fat_percentage
            }
        },
        'warn': warn,
    }

    return data