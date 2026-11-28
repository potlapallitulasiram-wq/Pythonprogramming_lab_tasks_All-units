filename = "sample.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    print(content)
except FileNotFoundError:
    print(f"Error: '{filename}' not found.")
    