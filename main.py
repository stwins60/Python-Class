options = ''

contact = {
    'First-name': '',
    'Middle-initial': '',
    'Last-name': '',
    'Mailing-address': '',
    'City': '',
    'Country': '',
    'State': '',
    'Zip-code': '',
    'Email': '',
    'Phone': ''
}

while options != 'Q':
    print("1. List Phone Numbers")
    print("2. Add a Contact")
    print("3. Remove a Contact")
    print("4. Update a Contact")
    print("5. Lookup a Contacts by Number")
    print("Q. Quit")

    options = str(input("Type in a number (1-5 or Q): "))

    if options == '1':
        print("List Phone Numbers")
        phone_number = contact['Phone']
        if phone_number == '':
            print(f"No number is found!!")
        else:
            print(f"The phone number found is {phone_number}")

    elif options == '2':
        print("2. Add a Contact")
        while input("Do you want to add a Contact [Y/N]: ") == 'Y':
            contact['First-name'] = input("Enter your first name: ")
            contact['Middle-initial'] = input("Enter your initials: ")
            contact['Last-name'] = input("Enter your last name: ")
            contact['Mailing-address'] = input("Enter your mailing address: ")
            contact['City'] = input("Enter your city: ")
            contact['Country'] = input("Enter your country: ")
            contact['State'] = input("Enter your state: ")
            contact['Zip-code'] = input("Enter your zip code: ")
            contact['Email'] = input("Enter your email address: ")
            contact['Phone'] = input("Enter your phone number: ")

            result = """First Name: {} \nMiddle Initials: {} \nLast Name: {} \nMailing Address: {} \nCity: {} \
            \nCountry: {} \nState: {} \nZip code: {} \nEmail: {} \nPhone: {} \n""".format(
                contact['First-name'], contact['Middle-initial'], contact['Last-name'], contact['Mailing-address'],
                contact['City'], contact['Country'], contact['State'], contact['Zip-code'], contact['Email'], contact['Phone']
            )
            print()
            print(result)
            with open('contact1.txt', 'w') as file:
                file.write(result)
                file.close()

    elif options == '3':
        print("3. Remove a Contact")
        del contact['First-name']
        del contact['Middle-initial']
        del contact['Last-name']
        del contact['Mailing-address']
        del contact['City'],
        del contact['Country']
        del contact['State']
        del contact['Zip-code']
        del contact['Email']
        del contact['Phone']

        for i in contact.keys():
            if i == '':
                print("The contact has been removed")
            else:
                print("The contact is still saved!!")

    elif options == '4':
        print("4. Update a Contact")
        field = input("Enter the field you want to update: ")
        if field == 'First-name':
            contact['First-name'] = input("Enter your first name: ")
            print(f"{contact['First-name']} has been updated successfully")
        elif field == 'Middle-initial':
            contact['Middle-initial'] = input("Enter your middle initial: ")
            print(f"{contact['Middle-initial']} has been updated successfully")
        elif field  == 'Last-name':
            contact['Last-name'] = input("Enter your last name: ")
            print(f"{contact['Last-name']} has been updated successfully")
        elif field == 'Mailing-address':
            contact['Mailing-address'] = input("Enter your mailing address: ")
            print(f"{contact['Mailing-address']} has been updated successfully")
        elif field == 'City':
            contact['City'] = input("Enter your City: ")
            print(f"{contact['City']} has been updated successfully")
        elif field == 'Country':
            contact['Country'] = input("Enter your Country: ")
            print(f"{contact['Country']} has been updated successfully")
        elif field == 'State':
            contact['State'] = input("Enter your State: ")
            print(f"{contact['State']} has been updated successfully")
        elif field == 'Zip-code':
            contact['Zip-code'] = input("Enter your zip code: ")
            print(f"{contact['Zip-code']} has been updated successfully")
        elif field == 'Email':
            contact['Email'] = input("Enter your Email: ")
            print(f"{contact['Email']} has been updated successfully")
        elif field == 'Phone':
            contact['Phone'] = input("Enter your Phone: ")
            print(f"{contact['Phone']} has been updated successfully")
        
        result = """First Name: {} \nMiddle Initials: {} \nLast Name: {} \nMailing Address: {} \nCity: {} \
            \nCountry: {} \nState: {} \nZip code: {} \nEmail: {} \nPhone: {} \n""".format(
                contact['First-name'], contact['Middle-initial'], contact['Last-name'], contact['Mailing-address'],
                contact['City'], contact['Country'], contact['State'], contact['Zip-code'], contact['Email'], contact['Phone']
            )
        print()
        print(result)
        with open('contact1.txt', 'w') as file:
            file.write(result)
            file.close()

    elif options == '5':
        print("5. Lookup a Contacts by Number")
        number = input("Enter the phone number to look up: ")
        if contact['Phone'] == number:
            result = """First Name: {} \nMiddle Initials: {} \nLast Name: {} \nMailing Address: {} \nCity: {} \
            \nCountry: {} \nState: {} \nZip code: {} \nEmail: {} \nPhone: {} \n""".format(
                contact['First-name'], contact['Middle-initial'], contact['Last-name'], contact['Mailing-address'],
                contact['City'], contact['Country'], contact['State'], contact['Zip-code'], contact['Email'], contact['Phone']
            )
            print(result)
        else:
            print(f"Phone number {number} not found")
