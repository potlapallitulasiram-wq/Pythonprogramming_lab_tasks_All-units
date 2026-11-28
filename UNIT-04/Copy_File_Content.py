source_file = "sample.txt"
dest_file = "copy.txt"

try:
    with open(source_file, "r", encoding="utf-8") as src:
        data = src.read()

    with open(dest_file, "w", encoding="utf-8") as dst:
        dst.write(data)

    print(f"Copied content from '{source_file}' to '{dest_file}'.")
except FileNotFoundError:
    print(f"Error: '{source_file}' not found.")