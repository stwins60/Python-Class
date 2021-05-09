import sqlite3 as sql

conn = sql.connect('electricity.db')

conn.execute('''CREATE TABLE electricity_bill
(customer_name TEXT NOT NULL, area TEXT NOT NULL, building TEXT NOT NULL, kilowatt INTEGER NOT NULL,
    Billing_address TEXT NOT NULL, City TEXT NOT NULL, Town TEXT NOT NULL, Country TEXT NOT NULL, \
    Monthly_cost INTEGER NOT NULL, Total_cost INTEGER NOT NULL);''')

print("Table created successfully")
conn.commit()