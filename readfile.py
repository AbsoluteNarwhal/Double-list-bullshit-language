import main


file = open("hello-world.dlbl", "r")
fileContents = file.read()

code = main.splitTokens(fileContents)
print(main.translate(code))
file.close()