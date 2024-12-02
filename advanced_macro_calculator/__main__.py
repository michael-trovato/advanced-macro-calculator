# __main__.py
from advanced_macro_calculator.input_handlers import get_user_input
from advanced_macro_calculator.calculations import AdvancedMacroCalculator
from advanced_macro_calculator.outputs import print_results


def main():
    # Get user input
    user_input = get_user_input()

    # Perform calculations
    amc = AdvancedMacroCalculator()
    results = amc.calculate_macros(*user_input)

    # Print or output the results
    print_results(results)


if __name__ == '__main__':
    main()
