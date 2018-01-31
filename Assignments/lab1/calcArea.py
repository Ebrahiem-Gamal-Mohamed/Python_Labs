#Write a function that calculate the area of these shapes:
#triangle = (0.5 * base * height), rectangle = (width * height), Circle= (PI * radius ^ 2)

def calcArea(shapeName,dim1=0,dim2=0):
    if shapeName == "t":
        return (0.5 * dim1 * dim2)
    elif shapeName == "r":
        return (dim1 * dim2)
    elif shapeName == "c":
        return ((22/7) * dim1 ** 2)
    elif shapeName == "s":
        return (dim1 * dim1)
    else:
        return 'no result found'

if __name__ == '__main__':
    pass

userInput = input("insert the character of shape : ")
if userInput == "c" or userInput == "s":
    dimention1 = int(input("insert the dimention of shape : "))
    print(calcArea(userInput, dimention1))
else:
    dimention1 = int(input("insert the first dimention of shape : "))
    dimention2 = int(input("insert the second dimention of shape : "))
    print(calcArea(userInput, dimention1, dimention2))
  