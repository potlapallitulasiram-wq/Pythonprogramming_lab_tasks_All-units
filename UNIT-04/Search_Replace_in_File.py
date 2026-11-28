filename = "sample.txt"
old_word = input("Enter word to replace (e.g., Python): ")
new_word = input("Enter replacement word (e.g., Java): ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

    updated_content = content.replace(old_word, new_word)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(updated_content)

    print(f"Replaced '{old_word}' with '{new_word}' in '{filename}'.")
except FileNotFoundError:
    print(f"Error: '{filename}' not found.")