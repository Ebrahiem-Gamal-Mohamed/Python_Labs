# accept string and search for specofoc letter ...

def index_Search(userString,user_Letter):
    output = []
    for index , letter in enumerate(userString.casefold()):
        if(letter == user_Letter.casefold()):
            output.append(index)
    return output   

if __name__ == '__main__':
    pass

#user insert string
user_Str = input("insert your message : ")

#user insert letter that search for
user_Let = input("insert the letter : ")

print(index_Search(user_Str,user_Let))
