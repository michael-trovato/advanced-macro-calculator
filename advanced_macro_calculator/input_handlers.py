import re


CHANGE_UNITS = ('%', 'kg', 'lbs')
VALID_CHANGE_UNITS = ('pct', '%', 'kg', 'lbs')
HEIGHT_UNITS = ('cm', 'in')
WEIGHT_UNITS = ('kg', 'lbs')


def parse_input(user_input, available_units):
    user_input = user_input.lower()

    # Define the regex pattern to match numbers and units
    units = '|'.join(available_units)
    pattern = r"([-]?\d*\.?\d+)\s*(" + units + ")"

    # Search for matches in the user input
    match = re.search(pattern, user_input)

    if match:
        # Extract the number and unit from the matched groups
        number = float(match.group(1))  # Convert number to float
        unit = match.group(2)
        return number, unit
    else:
        raise ValueError()


def get_user_input():
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
            weight_input = input(f'What is your weight (units: {', '.join(WEIGHT_UNITS)})? ')
            weight, weight_units = parse_input(weight_input, available_units=WEIGHT_UNITS)
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
    else:
        body_fat_percentage = None

    # Height
    while True:
        print()
        try:
            height_input = input(f'What is your height (units: {', '.join(HEIGHT_UNITS)})? ')
            height, height_units = parse_input(height_input, available_units=HEIGHT_UNITS)
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
        print(f'Desired change per week (units: {', '.join(CHANGE_UNITS)})?\n'
              'Example:\n'
              '-1.0% (Lose 1% per week)\n'
              '0.25 lbs (Gain 0.25 lbs per week)')
        try:
            change, change_units = parse_input(input('> '), available_units=CHANGE_UNITS)
        except ValueError:
            print()
            print(f'Error: Please enter a number with units ({', '.join(CHANGE_UNITS)}).')
            continue
        break

    while True:
        print()
        print('How would you like to distribute remaining calories?\n'
              '(1) Favor Protein\n'
              '(2) Favor Carbohydrates\n'
              '(3) Favor Fat\n'
              '(4) Blend of Carbs & Fat\n'
              '(5) Blend of Fat & Protein\n'
              '(6) Blend of Carbs & Protein\n'
              '(7) Blend of Carbs, Fat, & Protein')
        try:
            distribution = int(input('> '))
        except ValueError:
            print()
            print('Error: Please enter a number 1 through 7.')
            continue
        if not 1 <= distribution <= 7:
            print()
            print('Error: Please enter a number 1 through 7.')
            continue
        break

    return tdee, distribution, change, change_units, weight, weight_units, body_fat_percentage, height, height_units, sex, age


def validate_input(tdee, distribution, change, change_units, weight, weight_units, body_fat_percentage, height,
                   height_units,
                   sex, age):
    if type(tdee) == int:
        if tdee < 0:
            ValueError('Error: Please enter a positive number.')
    else:
        raise ValueError('Error: Please enter a positive number.')

    if type(distribution) == int:
        if not 1 <= distribution <= 7:
            raise ValueError('Error: Please enter a number between 1 and 7.')
    else:
        raise ValueError('Error: Please enter a number between 1 and 7.')

    if type(change) != float:
        raise ValueError('Error: Please enter a number.')

    if type(change_units) != str:
        raise ValueError('Error: Please enter units as strings.')
    elif change_units not in VALID_CHANGE_UNITS:
        raise ValueError(f'Error: Unknown change unit {change_units}, available units: {', '.join(VALID_CHANGE_UNITS)}')

    if type(weight) != float:
        raise ValueError('Error: Please enter a number.')

    if type(weight_units) != str:
        raise ValueError('Error: Please enter units as strings.')
    elif weight_units not in WEIGHT_UNITS:
        raise ValueError(f'Error: Unknown weight unit {weight_units}, available units: {', '.join(WEIGHT_UNITS)}')

    if body_fat_percentage:
        if type(body_fat_percentage) != float:
            raise ValueError('Error: Please enter a number.')
        if body_fat_percentage <= 0:
            raise ValueError('Error: Please enter a positive number.')
        if body_fat_percentage >= 100:
            raise ValueError('Error: Body Fat Percentage must be between 0 and 100.')

    if type(height) != float:
        raise ValueError('Error: Please enter a number.')
    elif height <= 0:
        raise ValueError('Error: Please enter a positive number.')

    if type(height_units) != str:
        raise ValueError('Error: Please enter units as strings.')
    elif height_units not in HEIGHT_UNITS:
        raise ValueError(f'Error: Unknown height unit {height_units}, available units: {', '.join(HEIGHT_UNITS)}')

    if type(sex) != str:
        raise ValueError('Error: Please enter a string')
    elif sex not in ['m', 'f']:
        raise ValueError('Error: Please enter either M or F.')

    if type(age) == float:
        age = int(age)
    if type(age) == int:
        if age <= 0:
            raise ValueError('Error: Please enter a positive number.')
    else:
        raise ValueError('Error: Please enter a number.')