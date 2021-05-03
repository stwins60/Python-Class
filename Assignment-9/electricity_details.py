details = {
    'Customer_name': '',
    'Area': '',
    'Building': '',
    'Kilowatt': '',
    'Billing_address': '',
    'City': '',
    'Town': '',
    'Country': '',
    'Monthly_Cost': '',
    'Total_Cost': ''
}


def customer_input():
    # for i in details.keys():
    details['Customer_name'] = input("Please enter the customer\'s name: ")
    details['Area'] = input("Please enter the customer\'s area [Rural/Urban]: ")
    details['Building'] = input("Please enter the customer\'s building [Residential, Light Industrial, "
                                "Heavy Industrial: ")
    details['Kilowatt'] = int(float(input("Please enter the customer\'s kilowatt usage: ")))
    details['Billing_address'] = input("Please enter the customer\'s billing address: ")
    details['City'] = input("Please enter the customer\'s city: ")
    details['Town'] = input("Please enter the customer\'s town: ")
    details['Country'] = input("Please enter the customer\'s country: ")

    # print(details)


customer_input()
