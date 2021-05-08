import constant
import mysql.connector as mysql
from mysql.connector import Error

# import sqlite3 as sql
# from sqlite3 import Error

details = {'customer_name': input("Please enter the customer\'s name: "),
           'area': input("Please enter the customer\'s area [Rural/Urban]: "),
           'building': input("Please enter the customer\'s building [Residential, Light Industrial, "
                             "Heavy Industrial: "),
           'kilowatt': int(float(input("Please enter the customer\'s kilowatt usage: "))),
           'billing_address': input("Please enter the customer\'s billing address: "),
           'city': input("Please enter the customer\'s city: "), 'town': input("Please enter the customer\'s town: "),
           'county': input("Please enter the customer\'s county: "), 'monthly_cost': '', 'total_cost': ''}


def charges_per_building():
    if details['area'] == 'Rural' and details['building'] == 'Residential':
        monthly_cost = constant.RES_RUR_KW + \
                       constant.NOMINAL_TAX + int(details['kilowatt'])
        details['monthly_cost'] = monthly_cost
        print(f"The monthly cost is {monthly_cost}")

    elif details['area'] == 'Urban' and details['building'] == 'Residential':
        monthly_cost = constant.RES_URBAN_KW + \
                       constant.NOMINAL_TAX + int(details['kilowatt'])
        details['monthly_cost'] = monthly_cost
        print(f"The monthly cost is {monthly_cost}")

    elif details['area'] == 'Rural' and details['building'] == 'Light Industrial':
        monthly_cost = constant.LI_RUR_KW + \
                       constant.NOMINAL_TAX + int(details['kilowatt'])
        details['monthly_cost'] = monthly_cost
        print(f"The monthly cost is {monthly_cost}")

    elif details['area'] == 'Urban' and details['building'] == 'Light Industrial':
        monthly_cost = constant.LI_URBAN_KW + \
                       constant.NOMINAL_TAX + int(details['kilowatt'])
        details['monthly_cost'] = monthly_cost
        print(f"The monthly cost is {monthly_cost}")

    elif details['area'] == 'Rural' and details['building'] == 'Heavy Industrial':
        monthly_cost = constant.HI_RUR_KW + \
                       constant.NOMINAL_TAX + int(details['kilowatt'])
        details['monthly_cost'] = monthly_cost
        print(f"The monthly cost is {monthly_cost}")

    elif details['area'] == 'Urban' and details['building'] == 'Heavy Industrial':
        monthly_cost = constant.RES_URBAN_KW + \
                       constant.NOMINAL_TAX + int(details['kilowatt'])
        details['monthly_cost'] = monthly_cost
        print(f"The monthly cost is {monthly_cost}")
    else:
        print("Invalid data input")


def discount():
    if 200 <= int(details['kilowatt']) <= 450:
        monthly_cost = details['monthly_cost']
        total_cost = monthly_cost - (0.03 * monthly_cost)
        details['total_cost'] = total_cost
        print(f"The monthly total cost is {details['total_cost']}")

    elif 451 <= int(details['kilowatt']) <= 500:
        monthly_cost = details['monthly_cost']
        total_cost = monthly_cost - (0.05 * monthly_cost)
        details['total_cost'] = total_cost
        print(f"The monthly total cost is {details['total_cost']}")

    elif 501 <= int(details['kilowatt']) <= 601:
        monthly_cost = details['monthly_cost']
        total_cost = monthly_cost - (0.07 * monthly_cost)
        details['total_cost'] = total_cost
        print(f"The monthly total cost is {details['total_cost']}")

    elif 602 <= int(details['kilowatt']) <= 701:
        monthly_cost = details['monthly_cost']
        total_cost = monthly_cost - (0.09 * monthly_cost)
        details['total_cost'] = total_cost
        print(f"The monthly total cost is {details['total_cost']}")

    elif 702 <= int(details['kilowatt']) <= 801:
        monthly_cost = details['monthly_cost']
        total_cost = monthly_cost - (0.11 * monthly_cost)
        details['total_cost'] = total_cost
        print(f"The monthly total cost is {details['total_cost']}")

    elif int(details['kilowatt']) >= 802:
        monthly_cost = details['monthly_cost']
        total_cost = monthly_cost - (0.12 * monthly_cost)
        details['total_cost'] = total_cost
        print(f"The monthly total cost is {details['total_cost']}")


# print(details)
# with open('Electricity.txt', 'w') as file:
#     for key, value in details.items():
#         display = "\n" + key + " -> " + str(value) + "\n"
#         file.write(display)
#
# file.close()


def electricity_DB():
    conn = mysql.connect(
        host='localhost',
        user='root',
        password='',
        database='electricity'
    )

    # conn = sql.connect('electricity.db')
    print("open database successfully")
    try:

        cur = conn.cursor(dictionary=True)

        columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in details.keys())
        values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in details.values())
        data = "INSERT INTO %s ( %s ) VALUES ( %s );" % ('customer_electricity_bill', columns, values)

        cur.execute(data)
        conn.commit()
        print("Record has been inserted successfully")

        sql = "SELECT * FROM customer_electricity_bill"
        cur.execute(sql)

        result = cur.fetchall()
        print(result)

        for x in result:
            with open('Electricity.txt', 'w') as file:
                for key, value in x.items():
                    display = "Kenya Power and Lighting Company (KPLC)\n" + key + " -> " + str(value) + "\n"
                    file.write(display)

            file.close()

        with open('kPLC_Customer.txt', 'w') as file:
            for row in result:

                file.write(str(row))
        file.close()

        conn.close()
    except Error as e:
        print("Error inserting data into customer_electricity_bill " + str(e))


charges_per_building()
discount()
electricity_DB()
