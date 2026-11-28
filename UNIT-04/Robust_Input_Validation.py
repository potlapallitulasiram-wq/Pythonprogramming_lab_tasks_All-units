class InvalidMarksError(Exception):
    """Raised when marks are outside 0-100."""
    pass


try:
    marks = float(input("Enter marks (0-100): "))
    if marks < 0 or marks > 100:
        raise InvalidMarksError("Marks must be between 0 and 100.")
    status = "Pass" if marks >= 40 else "Fail"
    print(f"Marks: {marks} | Result: {status}")
except ValueError:
    print("Invalid input: Please enter a number.")
except InvalidMarksError as e:
    print("Validation Error:", e)
finally:
    print("Marks validation complete.")