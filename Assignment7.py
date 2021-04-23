
option = ''
contact = {
    1:{},
    2:{},
    3:{}
}

while option != 'Q':

    option = str(input("Type in a number (1-5 or Q): "))

    if option == '1':
        print("1. List Phone Numbers")
        print("2. Add a Contact")
        print("3. Remove a Contact")
        print("4. Update a Contact")
        print("5. Lookup a Contacts by Number")
        print("Q. Quit")

    elif option == '2':
        print("Adding Contact")
        while True:
            add = input("Do you want to add a new contact (y/n): ")
            if add == 'y':
                for i in range(10):
                    contact[i]['first_name'] = input("Enter First Name: ")
                    contact[i]['middle_initial'] = input("Enter Middle Initial: ")
                    contact[i]['last_name'] = input("Enter Last Name: ")
                    contact[i]['mailing_address'] = input("Enter Mailing Address: ")
                    contact[i]['city'] = input("Enter City: ")
                    contact[i]['country'] = input("Enter Country: ")
                    contact[i]['state'] = input("Enter State: ")
                    contact[i]['email_address'] = input("Enter Email Address: ")
                    contact[i]['phone_number'] = input("Enter Phone Number: ")
                else:
                    break
        print(contact)

    elif option == '3':
        print("Removing Account")
        name = input("Remove contact by name: ")

        if name in contact.values():
            print(name)
            del contact['first_name']
            del contact['middle_initial']
            del contact['last_name']
            del contact['mailing_address']
            del contact['city']
            del contact['country']
            del contact['state']
            del contact['email_address']
            del contact['phone_number']

            print("The Contact has been removed")
        else:
            print(f"{name} not found")

    elif option == '4':
        opt = ''
        print("Updating a Contact")
        print("Field Options [first_name, middle_initial, last_name, mailing_address, city, country, state, email_address, phone_number]")
        opt = input("What field will you will like to update: ")
        if opt == "first_name":
            contact['first_name'] = input("Enter First Name: ")
        elif opt == "middle_initial":
            contact['middle_initial'] = input("Enter Middle Initial: ")
        elif opt == "last_name":
            contact['last_name'] = input("Enter Last Name: ")
        elif opt == "mailing_address":
            contact['mailing_address'] = input("Enter Mailing Address: ")
        elif opt == "city":
            contact['city'] = input("Enter City: ")
        elif opt == "country":
            contact['country'] = input("Enter Country: ")
        elif opt == "state":
            contact['state'] = input("Enter State: ")
        elif opt == "email_address":
            contact['email_address'] = input("Enter Email Address: ")
        elif opt == "phone_number":
            contact['phone_number'] = input("Enter Phone Number: ")
        else:
            print("invalid input")


# def add_contact():

    # contact['first_name'] = input("Enter First Name: ")
    # contact['middle_initial'] = input("Enter Middle Initial: ")
    # contact['last_name'] = input("Enter Last Name: ")
    # contact['mailing_address'] = input("Enter Mailing Address: ")
    # contact['city'] = input("Enter City: ")
    # contact['country'] = input("Enter Country: ")
    # contact['state'] = input("Enter State: ")
    # contact['email_address'] = input("Enter Email Address: ")
    # contact['phone_number'] = input("Enter Phone Number: ")


# def remove_contact():
#     if name in contact:
#         del contact[first_name]
#         del contact[middle_initial]
#         del contact[last_name]
#         del contact[mailing_address]
#         del contact[city]
#         del contact[country]
#         del contact[state]
#         del contact[email_address]
#         del contact[phone_number]
#     else:
#         print(f"{contact[first_name]} not found")

# def update_contact():
#     if
# def display_options():


# add_contact()

# print(contact)
