# Basic usage
print("Hello, World!")

# Printing multiple objects with a custom separator and ending
name = "Alice"
age = 30
print("Name:", name, "Age:", age, sep=" | ", end="\n\n")

# Redirecting output to a file
with open("output.txt", "w") as file:
    print("This will be written to output.txt", file=file)

# Flushing the output immediately
print("This will be flushed immediately.", flush=True)

OUTPUT:

Hello, World!
Name: | Alice | Age: | 30

(This will be written to output.txt)

This will be flushed immediately.
