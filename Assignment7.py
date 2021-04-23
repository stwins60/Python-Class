
option = ''
contact = {
    'contact1': {'first_name': '', 'middle_initial': '', 'last_name': '',
                 'mailing_address': '',
                 'city': '',
                 'country': '',
                 'state': '',
                 'email_address': '',
                 'phone_number': ''

                 },
    'contact2': {'first_name': '', 'middle_initial': '', 'last_name': '',
                 'mailing_address': '',
                 'city': '',
                 'country': '',
                 'state': '',
                 'email_address': '',
                 'phone_number': ''

                 },
    'contact3': {'first_name': '', 'middle_initial': '', 'last_name': '',
                 'mailing_address': '',
                 'city': '',
                 'country': '',
                 'state': '',
                 'email_address': '',
                 'phone_number': ''

                 }
}


while option != 'Q':

    option = str(input("Type in a number (1-5 or Q): "))

    if option == '1':
        print()

    elif option == '2':
        print("Adding Contact")
        while input("Do you want to add a new contact (y/n): ") == 'y':
            cont_loc = str(input("Enter the location you want to save your contact [contact1, contact2, and contact3]: "))
            for i in contact.keys():
                if i == cont_loc:
                    
                    contact[i]['first_name'] = input("Enter First Name: ")
                    contact[i]['middle_initial'] = input(
                        "Enter Middle Initial: ")
                    contact[i]['last_name'] = input("Enter Last Name: ")
                    contact[i]['mailing_address'] = input(
                        "Enter Mailing Address: ")
                    contact[i]['city'] = input("Enter City: ")
                    contact[i]['country'] = input("Enter Country: ")
                    contact[i]['state'] = input("Enter State: ")
                    contact[i]['email_address'] = input("Enter Email Address: ")
                    contact[i]['phone_number'] = input("Enter Phone Number: ")

                    print(contact)
                

            # print(contact)

        #         for item in contact.keys():
        #             contact[item]['first_name'] = input("Enter First Name: ")
        #             contact[item]['middle_initial'] = input("Enter Middle Initial: ")
        #             contact[item]['last_name'] = input("Enter Last Name: ")
        #             contact[item]['mailing_address'] = input("Enter Mailing Address: ")
        #             contact[item]['city'] = input("Enter City: ")
        #             contact[item]['country'] = input("Enter Country: ")
        #             contact[item]['state'] = input("Enter State: ")
        #             contact[item]['email_address'] = input("Enter Email Address: ")
        #             contact[item]['phone_number'] = input("Enter Phone Number: ")
        #             print(item)
        #     else:
        #             break
        # print(contact)

    elif option == '3': # TODO Work on removing the contact
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

    elif option == '4': # TODO Work on removing the contact
        opt = ''
        print("Updating a Contact")
        print(
            "Field Options [first_name, middle_initial, last_name, mailing_address, city, country, state, email_address, phone_number]")
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
