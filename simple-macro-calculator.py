IDEAL_BFP_MALE = 12.5
IDEAL_BFP_FEMALE = 22.5
MALE_INITIAL_WEIGHT = 110
FEMALE_INITIAL_WEIGHT = 100
INITIAL_HEIGHT = 60
CALORIES_PER_G_FAT = 9
CALORIES_PER_G_CARB = 4
CALORIES_PER_G_PROTEIN = 4
CALORIES_PER_LB_BODY_FAT = 3500
MAX_LBS_LOSS_PER_WEEK = -2
MAX_LBS_GAIN_PER_WEEK = 1
GRAM_PROTEIN_LEAN_BODY_MASS = 1.2
MINIMUM_FAT_BODY_WEIGHT = 0.3


print("Press Ctrl-C to quit...")

while True:
    tdee = None
    try:
        print()
        tdee = int(input('What is your Total Daily Energy Expenditure? '))
    except ValueError:
        print('Error: Please enter a number.')
        continue
    if tdee < 0:
        print('Error: Please enter a positive number.')
        continue
    break

while True:
    print()
    try:
        weight = int(input('What is your weight in lbs? '))
    except ValueError:
        print('Error: Please enter a number.')
        continue
    if weight <= 0:
        print('Error: Please enter a positive number.')
        continue
    break

while True:
    print()
    bfp_known = input('Do you know your Body Fat Percentage (Y/N)? ').lower()
    if bfp_known == 'y':
        break
    elif bfp_known == 'n':
        break
    else:
        print('Error: Please enter either Y or N.')
        continue

body_fat_percentage = None
height = None
sex = None
if bfp_known == 'y':
    while True:
        print()
        try:
            body_fat_percentage = float(input('What is your body fat percentage? '))
        except ValueError:
            print('Error: Please enter a number.')
            continue
        if body_fat_percentage <= 0:
            print('Error: Please enter a positive number.')
            continue
        break

# Get height & sex if BFP isn't known
elif bfp_known == 'n':
    while True:
        print()
        try:
            height = int(input('What is your height in inches? '))
        except ValueError:
            print('Error: Please enter a number.')
            continue
        if height <= 0:
            print('Error: Please enter a positive number.')
            continue
        break

    while True:
        print()
        sex = input('What is your sex (M/F)? ').lower()
        if sex == 'm':
            sex = 1
            break
        elif sex == 'f':
            sex = 0
            break
        else:
            print('Error: Please enter either M or F.')

while True:
    print()
    print('How would you like to distribute remaining calories?\n'
          '(1) All Carbs\n'
          '(2) All Fat\n'
          '(3) Mix Carbs & Fat\n'
          '(4) Mix Fat & Protein\n'
          '(5) Mix Carbs, Fat & Protein')
    try:
        extra = int(input('> '))
    except ValueError:
        print('Error: Please enter a number 1 through 5.')
        continue
    break

while True:
    print()
    print('What percentage change per week?\n'
          'Example:\n'
          '-1.0 (Lose 1% per week)\n'
          '0.25 (Gain 0.25% per week)')
    try:
        percentage_change = float(input('> '))
    except ValueError:
        print('Error: Please enter a number.')
        continue
    break


def calculate_macros(tdee, extra, percentage_change, weight, body_fat_percentage, height, sex):
    lean_body_mass = None

    if body_fat_percentage:
        lean_body_mass = weight * (1 - body_fat_percentage / 100)
    else:
        height_difference = height - INITIAL_HEIGHT
        if sex == 1:
            ideal_weight = MALE_INITIAL_WEIGHT + (height_difference * 5)
            lean_body_mass = ideal_weight * (1 - IDEAL_BFP_MALE / 100)
        elif sex == 0:
            ideal_weight = FEMALE_INITIAL_WEIGHT + (height_difference * 5)
            lean_body_mass = ideal_weight * (1 - IDEAL_BFP_FEMALE / 100)

    protein_grams = int(lean_body_mass * GRAM_PROTEIN_LEAN_BODY_MASS)  # Set Minimum Protein
    fat_grams = int(weight * MINIMUM_FAT_BODY_WEIGHT)  # Set Minimum Fat

    protein_calories = protein_grams * CALORIES_PER_G_PROTEIN
    fat_calories = fat_grams * CALORIES_PER_G_FAT

    lbs_change = weight * (percentage_change / 100)
    if lbs_change < MAX_LBS_LOSS_PER_WEEK:  # Max lbs lost safety cap
        lbs_change = MAX_LBS_LOSS_PER_WEEK

    elif lbs_change > MAX_LBS_GAIN_PER_WEEK:  # Max lbs gain safety cap
        lbs_change = MAX_LBS_GAIN_PER_WEEK

    daily_calorie_change = lbs_change * CALORIES_PER_LB_BODY_FAT / 7
    daily_calories = tdee + daily_calorie_change
    extra_calories = daily_calories - protein_calories - fat_calories

    carb_grams = None
    if extra == 1:
        carb_grams = int(extra_calories / CALORIES_PER_G_CARB)
    elif extra == 2:
        carb_grams = 0
        fat_grams += int(extra_calories / CALORIES_PER_G_FAT)
    elif extra == 3:
        carb_grams = int(extra_calories / 2 / CALORIES_PER_G_CARB)
        fat_grams += int(extra_calories / 2 / CALORIES_PER_G_FAT)
    elif extra == 4:
        carb_grams = 0
        fat_grams += int(extra_calories / 2 / CALORIES_PER_G_FAT)
        protein_grams += int(extra_calories / 2 / CALORIES_PER_G_PROTEIN)
    elif extra == 5:
        carb_grams = int(extra_calories / 3 / CALORIES_PER_G_CARB)
        fat_grams += int(extra_calories / 3 / CALORIES_PER_G_FAT)
        protein_grams += int(extra_calories / 3 / CALORIES_PER_G_PROTEIN)

    protein_calories = int(protein_grams * CALORIES_PER_G_PROTEIN)
    fat_calories = int(fat_grams * CALORIES_PER_G_FAT)
    carb_calories = int(carb_grams * CALORIES_PER_G_CARB)

    return {
        'protein': {
            'grams': protein_grams,
            'calories': protein_calories,
        },
        'fat': {
            'grams': fat_grams,
            'calories': fat_calories,
        },
        'carb': {
            'grams': carb_grams,
            'calories': carb_calories,
        }
    }


macros = calculate_macros(tdee, extra, percentage_change, weight, body_fat_percentage, height, sex)
print()
print(f"Protein: {macros['protein']['grams']}g ({macros['protein']['calories']} calories)")
print(f"Fat: {macros['fat']['grams']}g ({macros['fat']['calories']} calories)")
print(f"Carbs: {macros['carb']['grams']}g ({macros['carb']['calories']} calories)")

total_calories = macros['protein']['calories'] + macros['fat']['calories'] + macros['carb']['calories']
print(f"Total Calories: {total_calories:,} kcal")
print(f"Percentage Protein: {macros['protein']['calories'] / total_calories * 100:.2f}%")
