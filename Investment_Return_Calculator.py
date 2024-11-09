"""
Investment Return Calculator
Author: Sachin Chhetri
Date: 2024. Nov. 08

Description:
This program Calculates the final amount of an investment based on an initial investment
and a specified return rate (in percentage). It prompts the user to enter these values
and then displays the projected final amount.

Usage:
Run this script in a Python environment, and follow the prompts to enter the
initial investment and return rate. The result will display the final investment amount.
"""

def calculate_investment_return(initial_investment, return_rate):
    # Convert return rate from percentage to decimal
    return_rate_decimal = return_rate / 100
    # Calculate final amount
    final_amount = initial_investment * (1 + return_rate_decimal)
    return final_amount


def main():
    print("Welcome to the Investment Return Calculator!")

    # Get user input for initial investment and return rate
    try:
        initial_investment = float(input("Enter the initial investment amount in dollars: $"))
        return_rate = float(input("Enter the return rate (in percentage): "))

        # Calculate final amount
        final_amount = calculate_investment_return(initial_investment, return_rate)

        # Display the result
        print(f"\nWith an initial investment of ${initial_investment} and a return rate of {return_rate}%,")
        print(f"the final amount would be: ${final_amount:.2f}")

    except ValueError:
        print("Invalid input. Please enter numbers for both the initial investment and the return rate.")


if __name__ == "__main__":
    main()
