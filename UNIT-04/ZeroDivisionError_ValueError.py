try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    quotient = numerator / denominator
    print("Result:", quotient)
except ValueError:
    print("Invalid input: Please enter numeric values only.")
except ZeroDivisionError:
    print("Math error: Denominator cannot be zero.")