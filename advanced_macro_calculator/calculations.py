import math

from .input_handlers import validate_input


class AdvancedMacroCalculator:
    CALORIES_PER_G_FAT = 9
    CALORIES_PER_G_CARB = 4
    CALORIES_PER_G_PROTEIN = 4
    CALORIES_PER_KG_BODY_FAT = 7700  # 3,500 kcal/lb
    MAX_KG_LOSS_PER_WEEK = -0.907185  # -2 lbs
    MAX_KG_GAIN_PER_WEEK = 0.907185  # 2 lbs
    MAX_PERCENTAGE_BELOW_BMR = 0.2
    GRAM_PROTEIN_LEAN_BODY_MASS_KG = 2.2
    MAX_GRAM_PROTEIN_LEAN_BODY_MASS_KG = 3
    GRAM_PROTEIN_FAT_MASS_KG = 0.044
    ANABOLIC_RESISTANCE_FACTOR = {50: 0.01, 65: 0.02}
    GRAM_SATURATED_FAT_LEAN_BODY_MASS_KG = 0.15
    MIN_FAT_G_LBM_KG = 0.75  # Default 0.75
    MIN_FAT_SAFETY_FACTOR_PERCENTAGE = 0.1  # Default 0.1
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

    @staticmethod
    def lbs_to_kg(lbs: float) -> float:
        return lbs / 2.205

    @staticmethod
    def kg_to_lbs(kgs: float) -> float:
        return kgs / 0.4536

    @staticmethod
    def cm_to_inches(cms: float) -> float:
        return cms * 0.393701

    @staticmethod
    def inches_to_cm(inches: float) -> float:
        return inches * 2.54

    @staticmethod
    def cm_to_meters(cms: float) -> float:
        return cms / 100

    @staticmethod
    def calculate_bmr(height, weight, age, sex):
        if sex == 'm':
            return int(88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age))
        elif sex == 'f':
            return int(447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age))

    @staticmethod
    def calculate_bmi(height, weight):
        meters = AdvancedMacroCalculator.cm_to_meters(height)
        return weight / meters ** 2

    @staticmethod
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

    @staticmethod
    def calculate_fatty_acids(sex, age, lean_body_mass):
        ratio = (lean_body_mass - AdvancedMacroCalculator.LBM_POP_DIST[0]) / (AdvancedMacroCalculator.LBM_POP_DIST[1] - AdvancedMacroCalculator.LBM_POP_DIST[0])
        omega3 = round(AdvancedMacroCalculator.OMEGA3_INTAKE_RANGE[0] + (ratio * (AdvancedMacroCalculator.OMEGA3_INTAKE_RANGE[1] - AdvancedMacroCalculator.OMEGA3_INTAKE_RANGE[0])), 2)

        if omega3 < AdvancedMacroCalculator.OMEGA3_INTAKE_RANGE[0]:
            omega3 = AdvancedMacroCalculator.OMEGA3_INTAKE_RANGE[0]
        elif omega3 > AdvancedMacroCalculator.OMEGA3_INTAKE_RANGE[1]:
            omega3 = AdvancedMacroCalculator.OMEGA3_INTAKE_RANGE[1]

        if age < AdvancedMacroCalculator.LINOLEIC_ACID_AI_AGE_THRESHOLD:
            linoleic_acid = AdvancedMacroCalculator.LINOLEIC_ACID_AI[sex][0]
        else:
            linoleic_acid = AdvancedMacroCalculator.LINOLEIC_ACID_AI[sex][1]

        saturated_fat = math.ceil(lean_body_mass * AdvancedMacroCalculator.GRAM_SATURATED_FAT_LEAN_BODY_MASS_KG)

        total = math.ceil(lean_body_mass * AdvancedMacroCalculator.MIN_FAT_G_LBM_KG * (1 + AdvancedMacroCalculator.MIN_FAT_SAFETY_FACTOR_PERCENTAGE))
        total_essential = omega3 + linoleic_acid + saturated_fat

        if total < total_essential:
            total = total_essential

        return total, omega3, linoleic_acid, saturated_fat

    @staticmethod
    def calculate_protein(lean_body_mass, protein_grams, extra_calories, split):
        protein_grams_upper_limit = lean_body_mass * AdvancedMacroCalculator.MAX_GRAM_PROTEIN_LEAN_BODY_MASS_KG
        remaining_protein_grams = protein_grams_upper_limit - protein_grams
        protein_calories_to_limit = remaining_protein_grams * AdvancedMacroCalculator.CALORIES_PER_G_PROTEIN

        additional_protein_calories = min(protein_calories_to_limit, int(extra_calories / split))
        remaining_calories = extra_calories - additional_protein_calories
        protein_grams += int(additional_protein_calories / AdvancedMacroCalculator.CALORIES_PER_G_PROTEIN)

        return protein_grams, remaining_calories

    @staticmethod
    def calculate_macros(tdee, distribution, change, change_units, weight, weight_units, body_fat_percentage, height,
                         height_units, sex, age):

        validate_input(tdee, distribution, change, change_units, weight, weight_units, body_fat_percentage, height,
                       height_units, sex, age)

        # Convert to kg
        if weight_units in frozenset(('lb', 'lbs', 'pounds')):
            weight = AdvancedMacroCalculator.lbs_to_kg(weight)

        # Convert to cm
        if height_units in frozenset(('in', 'inches')):
            height = AdvancedMacroCalculator.inches_to_cm(height)

        if body_fat_percentage:
            lean_body_mass = int(weight * (1 - body_fat_percentage / 100))
            fat_mass = weight - lean_body_mass
        else:
            bmi = AdvancedMacroCalculator.calculate_bmi(height, weight)
            body_fat_percentage = AdvancedMacroCalculator.bmi_to_bfp(bmi, sex, age)
            body_fat_percentage = round(body_fat_percentage, 2)
            lean_body_mass = int(weight * (1 - body_fat_percentage / 100))
            fat_mass = weight - lean_body_mass

        # Protein
        protein_grams = math.ceil(lean_body_mass * AdvancedMacroCalculator.GRAM_PROTEIN_LEAN_BODY_MASS_KG)  # Add Protein for Lean Mass
        protein_grams += math.ceil(fat_mass * AdvancedMacroCalculator.GRAM_PROTEIN_FAT_MASS_KG)  # Add Protein for Fat Mass

        age_factor = 1
        for age_threshold, ar_factor in AdvancedMacroCalculator.ANABOLIC_RESISTANCE_FACTOR.items():
            if age > age_threshold:
                age_factor = 1 + ar_factor * (age - age_threshold)
                break
        protein_grams = math.ceil(protein_grams * age_factor)

        max_allowed_protein = AdvancedMacroCalculator.MAX_GRAM_PROTEIN_LEAN_BODY_MASS_KG * lean_body_mass
        protein_grams = protein_grams if protein_grams <= max_allowed_protein else max_allowed_protein
        protein_calories = protein_grams * AdvancedMacroCalculator.CALORIES_PER_G_PROTEIN

        # Fatty Acids
        fat_grams, omega3_grams, linoleic_acid_grams, saturated_fat_grams = AdvancedMacroCalculator.calculate_fatty_acids(sex, age, lean_body_mass)
        fat_calories = fat_grams * AdvancedMacroCalculator.CALORIES_PER_G_FAT

        if change_units in frozenset(('pct', '%')):
            weight_change = weight * (change / 100)
        elif change_units == 'lbs':
            weight_change = AdvancedMacroCalculator.lbs_to_kg(change)
        elif change_units == 'kg':
            weight_change = change
        else:
            raise ValueError('Unrecognized change units')

        if weight_change < AdvancedMacroCalculator.MAX_KG_LOSS_PER_WEEK:  # Max loss safety cap
            weight_change = AdvancedMacroCalculator.MAX_KG_LOSS_PER_WEEK

        elif weight_change > AdvancedMacroCalculator.MAX_KG_GAIN_PER_WEEK:  # Max gain safety cap
            weight_change = AdvancedMacroCalculator.MAX_KG_GAIN_PER_WEEK

        daily_calorie_change = weight_change * AdvancedMacroCalculator.CALORIES_PER_KG_BODY_FAT / 7
        daily_calories = int(tdee + daily_calorie_change)

        bmr = AdvancedMacroCalculator.calculate_bmr(height, weight, age, sex)
        calories_lower_limit = bmr * (1 - AdvancedMacroCalculator.MAX_PERCENTAGE_BELOW_BMR)

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
            # All Protein
            if distribution == 1:
                protein_grams += math.ceil(extra_calories / AdvancedMacroCalculator.CALORIES_PER_G_PROTEIN)

            # All Carbs
            elif distribution == 2:
                carb_grams = math.ceil(extra_calories / AdvancedMacroCalculator.CALORIES_PER_G_CARB)

            # All Fat
            elif distribution == 3:
                fat_grams += math.ceil(extra_calories / AdvancedMacroCalculator.CALORIES_PER_G_FAT)

            # Mix Carbs & Fat
            elif distribution == 4:
                carb_grams = math.ceil(extra_calories / 2 / AdvancedMacroCalculator.CALORIES_PER_G_CARB)
                fat_grams += math.ceil(extra_calories / 2 / AdvancedMacroCalculator.CALORIES_PER_G_FAT)

            # Mix Fat & Protein
            elif distribution == 5:
                protein_grams, remaining_calories = AdvancedMacroCalculator.calculate_protein(lean_body_mass, protein_grams, extra_calories, 2)
                fat_grams += math.ceil(remaining_calories / AdvancedMacroCalculator.CALORIES_PER_G_FAT)

            # Mix Carbs & Protein
            elif distribution == 6:
                protein_grams, remaining_calories = AdvancedMacroCalculator.calculate_protein(lean_body_mass, protein_grams, extra_calories, 2)
                carb_grams = math.ceil(remaining_calories / AdvancedMacroCalculator.CALORIES_PER_G_CARB)

            # Mix Carbs, Fat, & Protein
            elif distribution == 7:
                protein_grams, remaining_calories = AdvancedMacroCalculator.calculate_protein(lean_body_mass, protein_grams, extra_calories, 3)
                additional_macro_calories = remaining_calories / 2
                carb_grams = math.ceil(additional_macro_calories / AdvancedMacroCalculator.CALORIES_PER_G_CARB)
                fat_grams += math.ceil(additional_macro_calories / AdvancedMacroCalculator.CALORIES_PER_G_FAT)

        protein_calories = int(protein_grams * AdvancedMacroCalculator.CALORIES_PER_G_PROTEIN)
        fat_calories = int(fat_grams * AdvancedMacroCalculator.CALORIES_PER_G_FAT)
        omega3_calories = int(omega3_grams * AdvancedMacroCalculator.CALORIES_PER_G_FAT)
        linoleic_acid_calories = int(linoleic_acid_grams * AdvancedMacroCalculator.CALORIES_PER_G_FAT)
        saturated_fat_calories = int(saturated_fat_grams * AdvancedMacroCalculator.CALORIES_PER_G_FAT)
        carb_calories = int(carb_grams * AdvancedMacroCalculator.CALORIES_PER_G_CARB)

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
        lean_body_mass_lbs = round(AdvancedMacroCalculator.kg_to_lbs(lean_body_mass), 2)
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
