'''In this program we show an example of using dictionaries to keep track
 of information in a phonebook.

'''

phoneBook={}    #empty dictionary

while True:
    name:str=input("Enter name :")
    number:int=input("Enter  number")
    if name=='':
        break
    phoneBook[name]=number  #Syentax : dictionary[key] = value to store data.
print(phoneBook)


    