import re
import math

CALORIES_PER_G_FAT = 9
CALORIES_PER_G_CARB = 4
CALORIES_PER_G_PROTEIN = 4
CALORIES_PER_KG_BODY_FAT = 7700  # 3,500 kcal/lb
MAX_KG_LOSS_PER_WEEK = -0.907185  # -2 lbs
MAX_KG_GAIN_PER_WEEK = 0.907185  # 2 lbs
MAX_PERCENTAGE_BELOW_BMR = 0.2
GRAM_PROTEIN_LEAN_BODY_MASS_KG = 2.2
MIN_FAT_G_LBM_KG = 0.75
MIN_FAT_SAFETY_FACTOR_PERCENTAGE = 0.2
OMEGA3_INTAKE_RANGE = (1.75, 2.5)  # Grams
LINOLEIC_ACID_AI_AGE_THRESHOLD = 50  # Years
LINOLEIC_ACID_AI = {
    'm': [17, 14],
    'f': [12, 11]
}
LBM_POP_DIST = (34, 72)  # 75-159 lbs


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


def parse_input(user_input, available_units):
    # Define the regex pattern to match numbers and units
    units = '|'.join(available_units)
    pattern = r"([-]?\d+\.?\d*)\s*(" + units + ")"

    # Search for matches in the user input
    match = re.search(pattern, user_input)

    if match:
        # Extract the number and unit from the matched groups
        number = float(match.group(1))  # Convert number to float
        unit = match.group(2)
        return number, unit
    else:
        raise ValueError()


def calculate_fatty_acids(sex, age, lean_body_mass):
    ratio = (lean_body_mass - LBM_POP_DIST[0]) / (LBM_POP_DIST[1] - LBM_POP_DIST[0])
    omega3 = OMEGA3_INTAKE_RANGE[0] + (ratio * (OMEGA3_INTAKE_RANGE[1] - OMEGA3_INTAKE_RANGE[0]))

    if omega3 < OMEGA3_INTAKE_RANGE[0]:
        omega3 = OMEGA3_INTAKE_RANGE[0]

    if age < LINOLEIC_ACID_AI_AGE_THRESHOLD:
        linoleic_acid = LINOLEIC_ACID_AI[sex][0]
    else:
        linoleic_acid = LINOLEIC_ACID_AI[sex][1]

    total = math.ceil(lean_body_mass * MIN_FAT_G_LBM_KG * (1 + MIN_FAT_SAFETY_FACTOR_PERCENTAGE))

    if total < omega3 + linoleic_acid:
        total = omega3 + linoleic_acid

    return total, omega3, linoleic_acid


def print_results(macros, lbm, bfp, bmr, warn):
    total_calories = macros['protein']['calories'] + macros['fat']['total']['calories'] + macros['carb']['calories']
    caloric_change = total_calories - tdee

    print('\n\n')
    print('===== YOUR DIETARY BREAKDOWN =====')
    print(
        f"1. Protein:\n   Amount: {macros['protein']['grams']}g\n   Calories from Protein: {macros['protein']['calories']} kcal")
    print(
        f"   Protein Percentage: {macros['protein']['calories'] / total_calories * 100:.2f}%")
    print(
        f"   Protein / Lean Body Mass: {macros['protein']['grams'] / lbm['kg']:.2f} g/kg ({macros['protein']['grams'] / lbm['lbs']:.2f} g/lb)\n")
    print(
        f"2. Fat: \n   Total Fat: {macros['fat']['total']['grams']:.0f}g\n   Calories from Fat: {macros['fat']['total']['calories']} kcal")
    print(
        f"   Omega 3 DHA & EPA:\n      Amount: {macros['fat']['omega3']['grams']:.2f}g\n      Calories: {macros['fat']['omega3']['calories']} kcal")
    print(
        f"   Linoleic Acid:\n      Amount: {macros['fat']['linoleic_acid']['grams']}g\n      Calories: {macros['fat']['linoleic_acid']['calories']} kcal\n")
    print(
        f"3. Carbs:\n   Amount: {macros['carb']['grams']}g\n   Calories from Carbs: {macros['carb']['calories']} kcal")

    print(f"\nDaily Caloric Intake: {total_calories:,} kcal")
    print(f"Daily Caloric Change: {caloric_change:,} kcal")

    print(f"\nYour Body Stats:")
    print(f"Lean Body Mass: {lbm['kg']:.0f} kg ({lbm['lbs']:.0f} lbs)")
    print(f"Body Fat Percentage: {bfp:.2f}%")
    print(f"Total Daily Energy Expenditure: {tdee:,} kcal")
    print(f"Basal Metabolic Rate: {bmr:,} kcal")

    if warn:
        print()
        print('===== IMPORTANT MEDICAL WARNING =====')
        print(
            f'Your calculated daily calorie intake ({total_calories:,} kcal) is below your estimated basal metabolic rate (BMR) of {bmr:,} kcal.')
        print(
            'Consuming fewer calories than your BMR for an extended period can lead to potential health risks, including nutrient deficiencies and metabolic slowdown.')
        print(
            'Ensure your diet includes a variety of nutrient-dense foods to meet your vitamin, mineral, and overall nutritional needs.')
        print(
            'Additionally, consider consulting with a healthcare provider or dietitian before starting any calorie-restricted diet, especially one below your BMR.')
        print(
            'They may suggest a tailored multivitamin or specific supplements based on your individual health profile and dietary needs.')


def get_user_input():
    body_fat_percentage = None
    height = None
    height_units = None
    sex = None

    print("Press Ctrl-C to quit...")

    # TDEE
    while True:
        tdee = None
        try:
            print()
            tdee = int(input('What is your Total Daily Energy Expenditure? '))
        except ValueError:
            print()
            print('Error: Please enter a number.')
            continue
        if tdee < 0:
            print()
            print('Error: Please enter a positive number.')
            continue
        break

    # Weight
    while True:
        print()
        try:
            weight_input = input('What is your weight (units: lbs or kg)? ')
            weight, weight_units = parse_input(weight_input, available_units=['lbs', 'kg'])
        except ValueError:
            print()
            print('Error: Please enter a number with lbs or kg as units.')
            continue
        if weight <= 0:
            print()
            print('Error: Please enter a positive number.')
            continue
        break

    while True:
        print()
        bfp_known = input('Do you know your Body Fat Percentage (Y/N)? ').lower()
        if bfp_known in ['y', 'n']:
            break
        else:
            print()
            print('Error: Please enter either Y or N.')
            continue

    if bfp_known == 'y':
        # Get BFP
        while True:
            print()
            try:
                body_fat_percentage = float(input('What is your body fat percentage? '))
            except ValueError:
                print()
                print('Error: Please enter a number.')
                continue
            if body_fat_percentage <= 0:
                print()
                print('Error: Please enter a positive number.')
                continue
            elif body_fat_percentage >= 100:
                print()
                print('Error: Body Fat Percentage must be between 0 and 100.')
                continue
            break

    # Height
    while True:
        print()
        try:
            height_input = input('What is your height (units: inches or cm)? ')
            height, height_units = parse_input(height_input, available_units=['inches', 'cm'])
        except ValueError:
            print()
            print('Error: Please enter a number with inches or cm as units.')
            continue
        if height <= 0:
            print()
            print('Error: Please enter a positive number.')
            continue
        break

    # Sex
    while True:
        print()
        sex = input('What is your sex (M/F)? ').lower()
        if sex in ['m', 'f']:
            break
        else:
            print()
            print('Error: Please enter either M or F.')

    # Age
    while True:
        print()
        try:
            age = int(input('What is your age (years)? ').lower())
            break
        except ValueError:
            print()
            print('Error: Please enter a number.')

    while True:
        print()
        print('How would you like to distribute remaining calories?\n'
              '(1) All Carbs\n'
              '(2) All Fat\n'
              '(3) Mix Carbs & Fat\n'
              '(4) Mix Fat & Protein\n'
              '(5) Mix Carbs & Protein\n'
              '(6) Mix Carbs, Fat & Protein')
        try:
            extra = int(input('> '))
        except ValueError:
            print()
            print('Error: Please enter a number 1 through 6.')
            continue
        break

    while True:
        print()
        print('What change per week (units: %, lbs, kg)?\n'
              'Example:\n'
              '-1.0% (Lose 1% per week)\n'
              '0.25 lbs (Gain 0.25 lbs per week)')
        try:
            change, change_units = parse_input(input('> '), available_units=['%', 'lbs', 'kg'])
        except ValueError:
            print()
            print('Error: Please enter a number and units (%, lbs, kg).')
            continue
        break

    return tdee, extra, change, change_units, weight, weight_units, body_fat_percentage, height, height_units, sex, age


def calculate_macros(tdee, extra, change, change_units, weight, weight_units, body_fat_percentage, height, height_units,
                     sex, age):
    # Convert to kg
    if weight_units == 'lbs':
        weight = lbs_to_kg(weight)

    # Convert to cm
    if height_units == 'inches':
        height = inches_to_cm(height)

    lean_body_mass = None
    if body_fat_percentage:
        lean_body_mass = weight * (1 - body_fat_percentage / 100)
    else:
        bmi = calculate_bmi(height, weight)
        body_fat_percentage = bmi_to_bfp(bmi, sex, age)
        lean_body_mass = weight * (1 - body_fat_percentage / 100)

    protein_grams = math.ceil(lean_body_mass * GRAM_PROTEIN_LEAN_BODY_MASS_KG)  # Set Minimum Protein
    fat_grams, omega3_grams, linoleic_acid_grams = calculate_fatty_acids(sex, age, lean_body_mass)

    protein_calories = protein_grams * CALORIES_PER_G_PROTEIN
    fat_calories = fat_grams * CALORIES_PER_G_FAT

    weight_change = None
    if change_units == '%':
        weight_change = weight * (change / 100)
    elif change_units in ['lbs', 'kg']:
        weight_change = change

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

    carb_grams = None
    if extra == 1:  # All Carbs
        carb_grams = math.ceil(extra_calories / CALORIES_PER_G_CARB)
    elif extra == 2:  # All Fat
        carb_grams = 0
        fat_grams += math.ceil(extra_calories / CALORIES_PER_G_FAT)
    elif extra == 3:  # Mix Carbs & Fat
        carb_grams = math.ceil(extra_calories / 2 / CALORIES_PER_G_CARB)
        fat_grams += math.ceil(extra_calories / 2 / CALORIES_PER_G_FAT)
    elif extra == 4:  # Mix Fat & Protein
        carb_grams = 0
        fat_grams += math.ceil(extra_calories / 2 / CALORIES_PER_G_FAT)
        protein_grams += math.ceil(extra_calories / 2 / CALORIES_PER_G_PROTEIN)
    elif extra == 5:  # Mix Carbs & Protein
        carb_grams = math.ceil(extra_calories / 2 / CALORIES_PER_G_CARB)
        protein_grams += math.ceil(extra_calories / 2 / CALORIES_PER_G_PROTEIN)
    elif extra == 6:  # Mix Carbs, Fat, & Protein
        carb_grams = math.ceil(extra_calories / 3 / CALORIES_PER_G_CARB)
        fat_grams += math.ceil(extra_calories / 3 / CALORIES_PER_G_FAT)
        protein_grams += math.ceil(extra_calories / 3 / CALORIES_PER_G_PROTEIN)

    protein_calories = int(protein_grams * CALORIES_PER_G_PROTEIN)
    fat_calories = int(fat_grams * CALORIES_PER_G_FAT)
    omega3_calories = int(omega3_grams * CALORIES_PER_G_FAT)
    linoleic_acid_calories = int(linoleic_acid_grams * CALORIES_PER_G_FAT)
    carb_calories = int(carb_grams * CALORIES_PER_G_CARB)

    macros = {
        'protein': {
            'grams': protein_grams,
            'calories': protein_calories,
        },
        'fat': {
            'total': {
                'grams': fat_grams,
                'calories': fat_calories,
            },
            'omega3': {
                'grams': omega3_grams,
                'calories': omega3_calories,
            },
            'linoleic_acid': {
                'grams': linoleic_acid_grams,
                'calories': linoleic_acid_calories,
            }
        },
        'carb': {
            'grams': carb_grams,
            'calories': carb_calories,
        }
    }

    lbm = {
        'kg': lean_body_mass,
        'lbs': kg_to_lbs(lean_body_mass),
    }

    return macros, lbm, body_fat_percentage, bmr, warn


if __name__ == '__main__':
    tdee, extra, change, change_units, weight, weight_units, body_fat_percentage, height, height_units, sex, age = get_user_input()
    macros, lbm, bfp, bmr, warn = calculate_macros(tdee, extra, change, change_units, weight, weight_units,
                                                   body_fat_percentage, height, height_units, sex, age)
    print_results(macros, lbm, bfp, bmr, warn)
