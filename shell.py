import main

print("DLBL Interpreter 0.1.1\nType 'helpme' for documentation.\n")
code = main.splitTokens(input("> "))
print(main.translate(code))