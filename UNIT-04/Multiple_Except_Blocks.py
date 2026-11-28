items = ["apple", "banana", "cherry", "mango"]

try:
    idx = int(input(f"Enter an index (0 to {len(items) - 1}): "))
    print("Selected item:", items[idx])
except ValueError:
    print("Invalid input: Please enter a valid integer index.")
except IndexError:
    print("Index out of range: That index does not exist in the list.")