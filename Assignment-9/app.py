from electricity_details import customer_input
from electricity_details import details
import constant


def charges_per_building():
    # for i in details.keys():
    # global charges_per_building
    total_cost = 0
    float(details['Monthly_Cost'])
    if details['Area'] == 'Rural' and details['Building'] == 'Residential':
        details['Monthly_Cost'] = constant.RES_RUR_KW + constant.NOMINAL_TAX + int(details['Kilowatt'])
        print(details['Monthly_Cost'])
    elif details['Area'] == 'Urban' and details['Building'] == 'Residential':
        details['Monthly_Cost'] = constant.RES_URBAN_KW + constant.NOMINAL_TAX + int(details['Kilowatt'])
        print(details['Monthly_Cost'])
    elif details['Area'] == 'Rural' and details['Building'] == 'Light Industrial':
        details['Monthly_Cost'] = constant.LI_RUR_KW + constant.NOMINAL_TAX + int(details['Kilowatt'])
        print(details['Monthly_Cost'])
    elif details['Area'] == 'Urban' and details['Building'] == 'Light Industrial':
        details['Monthly_Cost'] = constant.LI_URBAN_KW + constant.NOMINAL_TAX + int(details['Kilowatt'])
        print(details['Monthly_Cost'])
    elif details['Area'] == 'Rural' and details['Building'] == 'Heavy Industrial':
        details['Monthly_Cost'] = constant.HI_RUR_KW + constant.NOMINAL_TAX + int(details['Kilowatt'])
        print(details['Monthly_Cost'])
    elif details['Area'] == 'Urban' and details['Building'] == 'Heavy Industrial':
        details['Monthly_Cost'] = constant.RES_URBAN_KW + constant.NOMINAL_TAX + int(details['Kilowatt'])
        print(details['Monthly_Cost'])
    else:
        print("Invalid data input")


# print(details['Kilowatt'])
# if details['Kilowatt'] <= 450:
#     print(True)

if int(details['Kilowatt']) >= 200 and int(details['Kilowatt']) <= 450:
    details['Total_Cost'] = int(details['Monthly_Cost']) - float(0.03)
    print(f"The monthly total cost is {details['Total_Cost']}")
elif int(details['Kilowatt']) >= 451 and int(details['Kilowatt']) <= 500:
    details['Total_Cost'] = int(float(details['Monthly_Cost'])) - float(0.05)
    print(f"The monthly total cost is {details['Total_Cost']}")
elif int(details['Kilowatt']) >= 501 and int(details['Kilowatt']) <= 601:
    details['Total_Cost'] = int(float(details['Monthly_Cost'])) - float(0.07)
    print(f"The monthly total cost is {details['Total_Cost']}")
elif int(details['Kilowatt']) >= 602 and int(details['Kilowatt']) <= 701:
    details['Total_Cost'] = int(float(details['Monthly_Cost'])) - (0.09)
    print(f"The monthly total cost is {details['Total_Cost']}")
elif int(details['Kilowatt']) >= 702 and int(details['Kilowatt']) <= 801:
    details['Total_Cost'] = int(float(details['Monthly_Cost'])) - float(0.11)
    print(f"The monthly total cost is {details['Total_Cost']}")
elif int(details['Kilowatt']) >= 802:
    details['Total_Cost'] = int(float(details['Monthly_Cost'])) - float(0.12)
    print(f"The monthly total cost is {details['Total_Cost']}")


# customer_input()
charges_per_building()
print(details)
