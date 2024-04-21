import main


# Add your file here
file = open("example.dlbl", "r")
fileContents = file.read()

print("DLBL Interpreter 0.1.1\nType 'helpme' for documentation.\n")
code = main.splitTokens(fileContents)
print(main.translate(code))
file.close()