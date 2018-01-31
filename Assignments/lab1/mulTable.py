#Write a program that generate a multiplication table from 1 to the number passed

def mulTable(userNum):
    outList = []
    innerList = []
    userNum = int(userNum)
    for i in range(1, userNum + 1):
        for j in range(1 , i + 1):
            innerList.append(i*j)
        outList.append(innerList)
        innerList = []
    return outList    

if __name__ == '__main__':
    pass

#user isert the number
userNum = input("insert the number : ")

print(mulTable(userNum))
