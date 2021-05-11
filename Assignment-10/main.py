import csv
from faker import Faker
import mysql.connector as m
from mysql.connector import Error
import pandas as pd

record_count = 100

fake = Faker()

with open('Employee_Records.csv', 'w', newline='') as csvfile:
    fieldnames = ["First_Name", "Last_Name", "SSN", "Email_address", "Phone", "Address",
                  "City", "state", "zipcode", "country"]

    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()

    for i in range(record_count):
        writer.writerow({
            'First_Name': fake.first_name(),
            'Last_Name': fake.last_name(),
            'SSN': fake.ssn(),
            'Email_address': fake.email(),
            'Phone': fake.phone_number(),
            'Address': fake.street_address(),
            'City': fake.city(),
            'state': fake.state(),
            'zipcode': fake.zipcode(),
            'country': fake.country()

        })


def database():
    option = ''
    conn = m.connect(
        host='localhost',
        user='root',
        password='',
        # port='3307',
        database='user'
    )
    try:
        if conn.is_connected():
            cur = conn.cursor()

            print("Dropping the user_details table if it exist")
            cur.execute("DROP TABLE IF EXISTS user_details;")

            print("Creating a user_details table")
            sql = """CREATE TABLE IF NOT EXISTS user_details (First_Name VARCHAR(255) NOT NULL, Last_Name 
            VARCHAR(255) NOT NULL,SSN VARCHAR(255) NOT NULL, Email_address VARCHAR(255), Phone VARCHAR(255), 
            Address VARCHAR(255) NOT NULL, City VARCHAR(255) NOT NULL, state VARCHAR(255) NOT NULL, 
            zipcode VARCHAR(255) NOT NULL, country VARCHAR(255) NOT NULL)"""

            cur.execute(sql)

            user_data = pd.read_csv('Employee_Records.csv', index_col=False, delimiter=',')
            user_data.head()
            while option != 'Q':
                option = input("Do you want to insert, select, delete, update a record: ")
                if option == 'Insert':
                    print("Inserting records into the database")
                    for i, row in user_data.iterrows():

                        qry = "INSERT INTO user.user_details VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

                        cur.execute(qry, tuple(row))
                        conn.commit()
                    print("Data has been insert successfully")
                elif option == 'Select':
                    print("Printing the records in the database")
                    cur.execute('SELECT * FROM user.user_details')
                    result = cur.fetchall()
                    print("Total records: %s" % len(result))

                    for i in result:
                        print(*i, sep=',')
                elif option == 'Delete':
                    print("Deleting records in the database")
                    del_data = input("delete records using this fields [First_Name,Last_Name,SSN,Email_address,"
                                     "Phone,Address,City,state,zipcode,country]: ")
                    if del_data == 'First_Name':
                        data = input('Delete records by First Name: ')
                        cur.execute('DELETE FROM user.user_details WHERE First_Name = %s', data)
                        conn.commit()
                        print("Record deleted successfully")
                    elif del_data == 'Last_Name':
                        data = input('Delete records by Last Name: ')
                        cur.execute('DELETE FROM user.user_details WHERE Last_Name = %s', data)
                        conn.commit()
                        print("Record deleted successfully")
                    elif del_data == 'SSN':
                        data = input('Delete records by SSN: ')
                        cur.execute('DELETE FROM user.user_details WHERE SSN = %s', data)
                        conn.commit()
                        print("Record deleted successfully")
                    elif del_data == 'Email_Address':
                        data = input('Delete records by Email Address: ')
                        cur.execute('DELETE FROM user.user_details WHERE Email_Address = %s', data)
                        conn.commit()
                        print("Record deleted successfully")
                    elif del_data == 'Phone':
                        data = input('Delete records by Phone: ')
                        cur.execute('DELETE FROM user.user_details WHERE Phone = %s', data)
                        conn.commit()
                        print("Record deleted successfully")
                    elif del_data == 'Address':
                        data = input('Delete records by Address: ')
                        cur.execute('DELETE FROM user.user_details WHERE Address = %s', data)
                        conn.commit()
                        print("Record deleted successfully")
                    elif del_data == 'City':
                        data = input('Delete records by City: ')
                        cur.execute('DELETE FROM user.user_details WHERE City = %s', data)
                        conn.commit()
                        print("Record deleted successfully")
                    elif del_data == 'state':
                        data = input('Delete records by state: ')
                        cur.execute('DELETE FROM user.user_details WHERE state = %s', data)
                        conn.commit()
                        print("Record deleted successfully")
                    elif del_data == 'zipcode':
                        data = input('Delete records by zipcode: ')
                        cur.execute('DELETE FROM user.user_details WHERE zipcode = %s', data)
                        conn.commit()
                        print("Record deleted successfully")
                    elif del_data == 'country':
                        data = input('Delete records by country: ')
                        cur.execute('DELETE FROM user.user_details WHERE country = %s', data)
                        conn.commit()
                        print("Record deleted successfully")
                elif option == 'Update':
                    print("Updating records in the database")
                    upt_data = input("Update records using this fields [First_Name,Last_Name,SSN,Email_address,"
                                     "Phone,Address,City,state,zipcode,country]: ")
                    if upt_data == 'First_Name':
                        new = input('Enter the new First Name: ')
                        old = input('Enter the old First Name: ')
                        qry = 'UPDATE user.user_details SET First_Name = ? WHERE First_Name = ?'
                        cur.execute(qry, (new, old))
                        conn.commit()
                        print("Record updated successfully")
                    elif upt_data == 'Last_Name':
                        new = input('Enter the new Last Name: ')
                        old = input('Enter the old Name Name: ')
                        qry = 'UPDATE user.user_details SET Last_Name = ? WHERE Last_Name = ?'
                        cur.execute(qry, (new, old))
                        conn.commit()
                        print("Record updated successfully")
                    elif upt_data == 'SSN':
                        new = input('Enter the new SSN: ')
                        old = input('Enter the old SSN: ')
                        qry = 'UPDATE user.user_details SET SSN = ? WHERE SSN = ?'
                        cur.execute(qry, (new, old))
                        conn.commit()
                        print("Record updated successfully")
                    elif upt_data == 'Email_Address':
                        new = input('Enter the new Email Address: ')
                        old = input('Enter the old Email Address: ')
                        qry = 'UPDATE user.user_details SET Email_Address = ? WHERE Email_Address = ?'
                        cur.execute(qry, (new, old))
                        conn.commit()
                        print("Record updated successfully")
                    elif upt_data == 'Phone':
                        new = input('Enter the new Phone: ')
                        old = input('Enter the old Phone: ')
                        qry = 'UPDATE TABLE SET Phone = ? WHERE Phone = ?'
                        cur.execute(qry, (new, old))
                        conn.commit()
                        print("Record updated successfully")
                    elif upt_data == 'Address':
                        new = input('Enter the new Address: ')
                        old = input('Enter the old Address: ')
                        qry = 'UPDATE user.user_details SET Address = ? WHERE Address = ?'
                        cur.execute(qry, (new, old))
                        conn.commit()
                        print("Record updated successfully")
                    elif upt_data == 'City':
                        new = input('Enter the new City: ')
                        old = input('Enter the old City: ')
                        qry = 'UPDATE user.user_details SET City = ? WHERE City = ?'
                        cur.execute(qry, (new, old))
                        conn.commit()
                        print("Record updated successfully")
                    elif upt_data == 'state':
                        new = input('Enter the new state: ')
                        old = input('Enter the old state: ')
                        qry = 'UPDATE user.user_details SET state = ? WHERE state = ?'
                        cur.execute(qry, (new, old))
                        conn.commit()
                        print("Record updated successfully")
                    elif upt_data == 'zipcode':
                        new = input('Enter the new zipcode: ')
                        old = input('Enter the old zipcode: ')
                        qry = 'UPDATE user.user_details SET zipcode = ? WHERE zipcode = ?'
                        cur.execute(qry, (new, old))
                        conn.commit()
                        print("Record updated successfully")
                    elif upt_data == 'country':
                        new = input('Enter the new country: ')
                        old = input('Enter the old country: ')
                        qry = 'UPDATE user.user_details SET country = ? WHERE country = ?'
                        cur.execute(qry, (new, old))
                        conn.commit()
                        print("Record updated successfully")
                elif option == 'Q':

                    conn.close()
                    print("Connection closed")

    except Error as e:
        print(str(e))


database()
