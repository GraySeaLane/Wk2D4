def printName(name):
    print(f"Hello Mr/Ms {name}...we've been waiting for you!")


def solution():

    input_1 = input("To calculate your square footage please type sqft or to calculate a circumference please type circ")
    
    if input_1.lower() == "sqft":
        length = int(input("Enter the value of length: "))
        width = int(input("Enter the value of width: "))
        area = (length * width)
        print(area)
    
    elif input_1.lower() == "circ":
        radius = int(input("Enter the value of radius: "))
        circum = (2 * 3.14 * radius)
        print(circum)
    
    else:
        print("Please select valid response")
        
solution()