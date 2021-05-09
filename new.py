details = {'customer_name': input("Please enter the customer\'s name: "),
           'area': input("Please enter the customer\'s area [Rural/Urban]: "),
           'building': input("Please enter the customer\'s building [Residential, Light Industrial, "
                             "Heavy Industrial: "),
           'kilowatt': int(float(input("Please enter the customer\'s kilowatt usage: "))),
           'billing_address': input("Please enter the customer\'s billing address: "),
           'city': input("Please enter the customer\'s city: "), 'town': input("Please enter the customer\'s town: "),
           'country': '', 'monthly_cost': '', 'total_cost': ''}

data = []
for key, value in details.items():
    print(value)
    data.append(value)
print(data)