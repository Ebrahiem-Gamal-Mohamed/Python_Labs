#Write a program convert a list of names into sorted dictionary which key is the Alpha. and value
#is a list of names corresponding to this alpha.

def listToDic(inputList):
    inputList.sort()
    dic = {}
    for j in inputList:
        if j[0] in dic:
            dic[j[0]].append(j)
        else:
            dic[j[0]] = [j]
    return dic

if __name__ == '__main__':
    pass

inputList = []
for i in range(4):
    inputList.append(input("insert the name : "))

print(listToDic(inputList))    
