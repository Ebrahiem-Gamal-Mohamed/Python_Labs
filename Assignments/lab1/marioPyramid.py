# print * in the shape of mario pyramid ...

def marioPyramid(num):
    num = int(num)
    for i in range(num):
	    print (" "*(num-1*i)+("*")+("*"*(1*i)))

''' for i in range(0, 4):
        for j in range(0, num):
            print(end=" ")
        num = num - 2
        for j in range(0, i+1):
            print("* ",end="")
        print() '''

if __name__ == '__main__':
    pass

number = input("insert the number : ")

print(marioPyramid(number))
