
# print(anything) -- find("charcter")
#capitalize() -- len(name) -- replace("string","string") -- isdigit() -- str.format(*args,**kwargs) --
#int(“18”) -- long(18.5) -- float(15) -- complex(4,5) -- round(x) -- min(x,y,z) -- max(x,y,z) --
#newList = [] -- pop(4) -- pop() -- insert(3,variable) -- append(variable) -- remove(“C”) -- extend(yourList)
#newTuple = () -- Same as Lists but Tuples are immutable
#newDict = {} -- A key: value comma seperated elements Data Structure -- .keys() -- .items() -- .update(addInfoDict)
#if(): -- elif(): -- else: -- for variable in data Structure: --  
# range([start,] end[, step]) -- for i in range(10): -- while condition: 
# break -- continue -- pass
# input(prompt_message) -- for user input --
# def measureTemp ( temp ): commands and return some thing  -- def doSum(x, y = 2,z = 3):
# def doSum(*args):
# def doSum(**kwargs): for k in kwargs: print(kwargs[k])
# global name inside function -- nonlocal name inside function also --
# canFly = True bird = “Dove” if canFly else “Penguin” --
# swap --> x,y = 4,5 x,y = y,x -- 
# print(“Ahmed”, end=“. ”) -- “:”.join([“1”,“Ali”,“grp”]) -- “Sara Mohamed”.split(“ ”) -- for i , l in enumerate(languages):
# all(dataStructure) check if all items in an iterable are truthy value.
# any(dataStructure) check if one item at least in an iterable is truthy value.
#####################################################################################

# 1 )Write a program that remove all vowels from the input word and generate a brief version of it.

def vowels_removal(msg):
    vowels = ['a', 'e', 'o', 'i', 'u', 'A', 'E', 'O', 'U', 'I']
    for char in msg:
        if char in vowels:
            msg = msg.replace(char,'')
    return msg

if __name__ == '__main__':
    pass

msg = input("insert your message : ")
print(vowels_removal(msg))    

"""
==> Bonus function
#2)program to take list of strings and replace vowels .... 

fname = input("insert your first name : ").casefold()
lname = input("insert your last name : ").casefold()
userinput = [fname,lname]

def vowels_removal(args,vowels):
    f = 0
    while f < len(args):
        for i , j in vowels.items():
            args[f] = args[f].replace(i,j)
        f += 1
    return args

col = {"a":"", "e":"", "i":"", "o":"", "u":""}
print(vowels_removal(userinput, col))

"""

