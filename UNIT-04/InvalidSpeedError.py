class InvalidSpeedError(Exception):
    """Raised when vehicle speed is outside 0-120 km/h."""
    pass


try:
    speed = float(input("Enter vehicle speed (km/h): "))
    if speed < 0 or speed > 120:
        raise InvalidSpeedError("Speed must be between 0 and 120 km/h.")
    print(f"Speed {speed} km/h is within safe limits.")
except ValueError:
    print("Invalid input: Please enter a numeric speed.")
except InvalidSpeedError as e:
    print("Speed Error:", e)