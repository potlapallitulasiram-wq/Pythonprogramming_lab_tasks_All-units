text = input("Enter a number: ")

try:
    num = int(text)
except ValueError:
    print("Error: Could not convert input to an integer.")
else:
    print("Square:", num ** 2)
finally:
    print("Program finished")
    