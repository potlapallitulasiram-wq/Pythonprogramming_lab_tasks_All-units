try:
    result = 10 / 0
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide 10 by zero.")