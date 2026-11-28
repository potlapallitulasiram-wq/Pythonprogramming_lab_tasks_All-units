filename = "sample.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    line_count = len(lines)
    word_count = sum(len(line.split()) for line in lines)
    char_count = sum(len(line) for line in lines)

    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {char_count}")
except FileNotFoundError:
    print(f"Error: '{filename}' not found.")