phonebook = {'book1': {},
             'book2': {}, 'book3': {}, 'book4': {}, 'book5': {}}

while input("Do you want to add a new contact [y/n]: ") == "y":
    location = input("Enter the location to save details: ")
    for i in phonebook.keys():
        if i == location:
            for data in range(1, 4):
                key = input("Enter key: ")
                value = input("Enter the value: ")
                phonebook[i][key] = value

                print(phonebook)


with open('phonebook.txt', 'w') as file:
    file.write(str(phonebook))
    file.close()


with open("phonebook.txt") as file: # Use file to refer to the file object
 
   data = file.readLine()
   print(data.strip('\n'))


    # if i == location:
    #     print(True)
    # else:
    #     print(False)

# for i in range(1,15):
#     for i in phonebook.keys():
#         if phonebook[i] == location:
#             key = input("Enter key: ")
#             value = input("Enter the value: ")
#             phonebook[key] = value

# print(phonebook)
