# File handling in Python allows you to work with files, such as reading from, writing to, and modifying them. Python provides built-in functions and methods to handle files easily. Here's a guide on how to perform basic file operations:

# 1. Opening a File
# To open a file in Python, use the open() function. This function requires the file name (or path) and an optional mode.

# Syntax:

file = open('filename', 'mode')
# Modes:

# 'r' - Read (default mode). Opens the file for reading. If the file does not exist, it throws an error.
# 'w' - Write. Opens the file for writing. Creates a new file if it doesn’t exist or truncates it (empties it) if it does.
# 'a' - Append. Opens the file for writing, but does not truncate it. New data is written at the end of the file.
# 'b' - Binary mode. Used when dealing with binary files (e.g., images, audio).
# 'x' - Exclusive creation. Creates a new file, and throws an error if the file already exists.
# 't' - Text mode (default). Files are treated as text. You don’t need to specify this explicitly.

# Open a file in write mode
file = open('example.txt', 'w')
file.write('Hello, world!')
file.close()  # Always close the file after you're done with it
# 2. Reading from a File
# You can read data from a file using several methods:

# read() – Reads the entire content of the file.
# readline() – Reads one line from the file.
# readlines() – Reads all the lines into a list.
# Example:

# Open a file in read mode
file = open('example.txt', 'r')
content = file.read()
print(content)
file.close()
# 3. Writing to a File
# To write data to a file, you use the write() method. If the file does not exist and the mode is 'w' or 'a', Python will create it.

# Open a file in write mode
file = open('example.txt', 'w')
file.write('This is a test.')
file.close()
# 4. Appending to a File
# If you want to add data to the end of a file without overwriting the existing content, use the 'a' mode.

# Example:

# Open the file in append mode
file = open('example.txt', 'a')
file.write('This is an additional line.\n')
file.close()
# 5. Closing a File
# Always close a file after performing file operations. This can be done using the close() method. Alternatively, you can use a with statement to automatically close the file when done.

# Example (using with):


with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# No need to call file.close(), it's handled automatically
# 6. Handling File Exceptions
# You should handle exceptions while working with files to prevent crashes if the file doesn’t exist or there are other issues.



try:
    file = open('non_existent_file.txt', 'r')
    content = file.read()
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()


# Example:


file = open('/path/to/directory/example.txt', 'r')
# 8. File Modes Summary:
# 'r': Read
# 'w': Write (creates or truncates the file)
# 'a': Append
# 'b': Binary mode
# 'x': Exclusive creation
# 't': Text mode (default)