
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
    print()
    print("1. List Phone Numbers")
    print("2. Add a Contact")
    print("3. Remove a Contact")
    print("4. Update a Contact")
    print("5. Lookup a Contacts by Number")
    print("Q. Quit")
    print()

    option = str(input("Type in a number (1-5 or Q): "))

    if option == '1':
        print("List Phone Numbers")
        for i in contact.keys():
            numbers = contact[i]['phone_number']
            if numbers == '':
                print(f"No number is found in {i}")
            else:
                print(f"The Phone numbers in {i} is: {numbers}")

    elif option == '2':
        print("Adding Contact")
        print()
        while input("Do you want to add a new contact (y/n): ") == 'y':
            cont_loc = str(input(
                "Enter the location you want to save your contact [contact1, contact2, and contact3]: "))
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
                    contact[i]['zip_code'] = input("Enter ZipCode: ")
                    contact[i]['email_address'] = input(
                        "Enter Email Address: ")
                    contact[i]['phone_number'] = input("Enter Phone Number: ")

                    print()
                    result = """First Name: {} \nMiddle Initials: {} \nLast Name: {} \nMailing Address: {} \nCity: {} \nCountry: {} \nState: {} \nZip code: {} \nEmail Address: {} \nPhone Number: {}""".format(contact[i]['first_name'],
                                                                                                                                                                                                                contact[i][
                        'middle_initial'],
                        contact[i][
                        'last_name'],
                        contact[i][
                        'mailing_address'],
                        contact[i][
                        'city'],
                        contact[i][
                        'country'],
                        contact[i][
                        'state'],
                        contact[i][
                        'zip_code'],
                        contact[i][
                        'email_address'],
                        contact[i]['phone_number'])

                    with open('contact.txt', 'w') as file:
                        file.write(result)
                        file.close()

                    print(result)

    elif option == '3':
        print("Removing Account")
        opt = input(
            "Enter location you want to delete your contact from [contact1, contact2, and contact3]: ")
        for i in contact.keys():
            if i == opt:
                name = input("Remove contact by name: ")
                if contact[i]['first_name'] == name:
                    del contact[i]['first_name']
                    del contact[i]['middle_initial']
                    del contact[i]['last_name']
                    del contact[i]['mailing_address']
                    del contact[i]['city']
                    del contact[i]['country']
                    del contact[i]['state']
                    del contact[i]['zip_code']
                    del contact[i]['email_address']
                    del contact[i]['phone_number']

                    print("The Contact has been removed")
                else:
                    print(f"{name} not found")

    elif option == '4':  # TODO Run the test
        opt = ''
        print("Updating a Contact")
        upt = input(
            "Enter location you want to update your contact from [contact1, contact2, and contact3]: ")

        for i in contact.keys():
            if i == upt:
                print(
                    "Field Options [first_name, middle_initial, last_name, mailing_address, city, country, state, zip_code, email_address, phone_number]")
                opt = input("What field will you will like to update: ")
                if opt == "first_name":
                    contact[i]['first_name'] = input("Enter First Name: ")
                    print(f"{opt} has been updated successfully")
                elif opt == "middle_initial":
                    contact[i]['middle_initial'] = input(
                        "Enter Middle Initial: ")
                    print(f"{opt} has been updated successfully")
                elif opt == "last_name":
                    contact[i]['last_name'] = input("Enter Last Name: ")
                    print(f"{opt} has been updated successfully")
                elif opt == "mailing_address":
                    contact[i]['mailing_address'] = input(
                        "Enter Mailing Address: ")
                    print(f"{opt} has been updated successfully")
                elif opt == "city":
                    contact[i]['city'] = input("Enter City: ")
                    print(f"{opt} has been updated successfully")
                elif opt == "country":
                    contact[i]['country'] = input("Enter Country: ")
                    print(f"{opt} has been updated successfully")
                elif opt == "state":
                    contact[i]['state'] = input("Enter State: ")
                    print(f"{opt} has been updated successfully")
                elif opt == "zip_code":
                    contact[i]['zip_code'] = input("Enter ZipCode: ")
                    print(f"{opt} has been updated successfully")
                elif opt == "email_address":
                    contact[i]['email_address'] = input(
                        "Enter Email Address: ")
                    print(f"{opt} has been updated successfully")
                elif opt == "phone_number":
                    contact[i]['phone_number'] = input("Enter Phone Number: ")
                    print(f"{opt} has been updated successfully")
            else:
                print("invalid input")

    elif option == '5':
        print("Lookup a Contact by Number")

        lookup = input(
            "Enter location you want to lookup number from [contact1, contact2, and contact3]: ")

        for i in contact.keys():
            if i == lookup:
                number = input("Please enter the number to look up: ")
                if contact[i]['phone_number'] == number:
                    result = """First Name: {} \nMiddle Initials: {} \nLast Name: {} \nMailing Address: {} \nCity: {} \nCountry: {} \nState: {} \nEmail Address: {} \nPhone Number: {}""".format(contact[i]['first_name'],
                                                                                                                                                                                                 contact[i][
                        'middle_initial'],
                        contact[i][
                        'last_name'],
                        contact[i][
                        'mailing_address'],
                        contact[i][
                        'city'],
                        contact[i][
                        'country'],
                        contact[i][
                        'state'],
                        contact[i][
                        'zip_code'],
                        contact[i][
                        'email_address'],
                        contact[i]['phone_number'])
                    print(result)
                else:
                    print(f"Phone number {number} not found")

def write_contact_to_text():
    with open("contact.txt", 'r') as file: # Use file to refer to the file object
        data = file.read()
        print(data.strip('\n'))


# write_contact_to_text()
