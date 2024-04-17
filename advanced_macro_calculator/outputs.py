def print_results(data):
    print('\n\n')
    print('===== YOUR DIETARY BREAKDOWN =====')
    print(
        f"1. Protein:\n   Amount: {data['macros']['protein']['grams']['total']}g\n   Calories from Protein: {data['macros']['protein']['calories']} kcal")
    print(f"   Protein Percentage: {data['macros']['protein']['percentage']:.2f}%")
    print(
        f"   Protein / Lean Body Mass: {data['macros']['protein']['grams']['lean_body_mass']['kg']:.2f} g/kg ({data['macros']['protein']['grams']['lean_body_mass']['lbs']:.2f} g/lb)\n")
    print(
        f"2. Fat: \n   Total Fat: {data['macros']['fat']['total']['grams']:.0f}g\n   Calories from Fat: {data['macros']['fat']['total']['calories']} kcal")
    print(f"   Fat Percentage: {data['macros']['fat']['total']['percentage']:.2f}%")
    print(
        f"   Omega-3 EPA & DHA:\n      Amount: {data['macros']['fat']['omega3']['grams']:.2f}g\n      Calories: {data['macros']['fat']['omega3']['calories']} kcal")
    print(
        f"   Linoleic Acid:\n      Amount: {data['macros']['fat']['linoleic_acid']['grams']}g\n      Calories: {data['macros']['fat']['linoleic_acid']['calories']} kcal")
    print(
        f"   Saturated Fat:\n      Amount: {data['macros']['fat']['saturated_fat']['grams']}g\n      Calories: {data['macros']['fat']['saturated_fat']['calories']} kcal\n")
    print(
        f"3. Carbs:\n   Amount: {data['macros']['carb']['grams']}g\n   Calories from Carbs: {data['macros']['carb']['calories']} kcal")
    print(f"   Carb Percentage: {data['macros']['carb']['percentage']:.2f}%")

    print(f"\nDaily Caloric Intake: {data['stats']['metabolism']['total_calories']:,} kcal")
    print(f"Daily Caloric Change: {data['stats']['metabolism']['caloric_change']:,} kcal")

    print(f"\nYour Body Stats:")
    print(
        f"Lean Body Mass: {data['stats']['body_composition']['lean_body_mass']['kg']:.0f} kg ({data['stats']['body_composition']['lean_body_mass']['lbs']:.0f} lbs)")
    print(f"Body Fat Percentage: {data['stats']['body_composition']['body_fat_percentage']:.2f}%")
    print(f"Total Daily Energy Expenditure: {data['stats']['metabolism']['tdee']:,} kcal")
    print(f"Basal Metabolic Rate: {data['stats']['metabolism']['basal_metabolic_rate']:,} kcal")

    if data['warn']:
        print()
        print('===== IMPORTANT MEDICAL WARNING =====')
        print(
            f'Your calculated daily calorie intake {data['stats']['metabolism']['total_calories']:,} kcal is below your estimated basal metabolic rate (BMR) of {data['stats']['metabolism']['basal_metabolic_rate']:,} kcal.')
        print(
            'Consuming fewer calories than your BMR for an extended period can lead to potential health risks, including nutrient deficiencies and metabolic slowdown.')
        print(
            'Ensure your diet includes a variety of nutrient-dense foods to meet your vitamin, mineral, and overall nutritional needs.')
        print(
            'Additionally, consider consulting with a healthcare provider or dietitian before starting any calorie-restricted diet, especially one below your BMR.')
        print(
            'They may suggest a tailored multivitamin or specific supplements based on your individual health profile and dietary needs.')