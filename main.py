from time import sleep
import random

data = ["never gonna give you up", "never gonna let you down"]
stack = []

class Error:
    def __init__(self, errorType, errorText):
        self.errorType = errorType
        self.errorText = errorText
    
    def __repr__(self):
        return f"{self.errorType} Error: {self.errorText}\nRefer to the documentation for more information."



# Split the input into tokens
def split(text):
    result = text.split(';')
    result = [s for s in result if s != '']
    return result



# Translate tokens into actions
def translate(code):
    for i in range(len(code)):

        # sleep
        if code[i].startswith("bedtime"):
            try:
                sleep((int(code[i][7:])**2)+random.randint(-2, 2))
            except:
                return Error("NightmaresError", "Not an appropriate bedtime.")
            
        # print variable
        elif code[i].startswith("tnirp"):
            try:
                print(data.pop(int(code[i][5:])+1))
            except:
                return Error("ErrorError", "The program has forgotten what this error means.")
        
        # print documentation
        elif code[i] == "helpme":
            print("Documentation: This is the documentation. If you are reading this and want the documentation, you are in the right place because the documentation is found here. If you are not reading this, you are not in the right place because non-documentation is not found here. Thank you for reading the documentation.")

        # store data on stack  
        elif code[i].startswith("save"):
            try:
                data.append(stack.pop(int(code[i][4:])+1))
            except:
                return Error("CognitionError", "The program has forgotten what you told it to think about.")
        
        # load values in stack
        elif code[i].startswith("think"):
            try:
                stack.append(code[i][5:])
            except:
                return Error("CognitionError", "The program has forgotten what you told it to think about.")
        
        # data back to stack  
        elif code[i].startswith("remember"):
            try:
                stack.append(data.pop(int(code[i][8:])+1))
            except:
                return Error("MemoryError", "The program has forgotten what you told it to remember.")
        
        # copy values from data to stack without deleting it
        elif code[i].startswith("copy"):
            try:
                stack.append(data[int(code[i][4:])+1])
            except:
                return Error("MemoryError", "The program has forgotten what you told it to remember.")
        
        elif code[i].startswith("add"):
            try:
                result = code[i][3:].split('&')
                stack.append(str(stack.pop(int(result[0])) + stack.pop(int(result[1]))))
            except:
                return Error("MathError", "The program has forgotten basic math. Try again in 2nd grade.")
            
        elif code[i].startswith("multiply"):
            try:
                result = code[i][8:].split('&')
                stack.append(str(stack.pop(int(result[0])) + stack.pop(int(result[1]))))
            except:
                return Error("MathError", "The program has forgotten basic math. Try again in 2nd grade.")
        
            
        # invalid token
        else:
            return Error("SpellingError", "You got an F on the spelling test, womp womp.")
                



# Run the program
code = split(input("> "))
print(translate(code))