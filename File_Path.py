import os

# Get current working directory
currentDirectory = os.getcwd()
print(f"Current Directory: {currentDirectory}")

# Check if file exists before reading
filePath = os.path.join(currentDirectory, "ITCS103.txt")
if os.path.exists(filePath):
    with open(filePath, "r") as file:
        print(f"File Content:\n{file.read()}")
else:
    print("File does not exist!")