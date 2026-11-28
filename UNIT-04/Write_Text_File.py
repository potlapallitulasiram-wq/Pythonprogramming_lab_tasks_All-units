line = input("Enter a line of text to write to output.txt: ")

with open("output.txt", "w", encoding="utf-8") as file:
    file.write(line + "\n")

print("Successfully wrote to output.txt.")