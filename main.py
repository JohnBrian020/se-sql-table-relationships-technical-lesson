import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

q = """PRAGMA table_info(employees);"""

q = """
SELECT firstName, lastName, email
FROM employees
WHERE jobTitle = 'Sales Rep'
;
"""
df = pd.read_sql(q, conn)
#print("Number of results:", len(df))

q = """SELECT firstName, lastName, email, city FROM employees JOIN offices USING(officeCode) WHERE jobtitle = 'Sales Rep';"""
#df = pd.read_sql(q, conn)
#print(df.head())

q = """SELECT productLine, textDescription FROM productlines;"""
#df = pd.read_sql(q, conn)
#print((df))

q = """SELECT productLine, textDescription, productVendor, productDescription FROM productlines JOIN products USING(productLine);"""
#df = pd.read_sql(q, conn)
#print((df.head()))

q = """SELECT * FROM offices JOIN customers USING(state);"""
#df = pd.read_sql(q, conn)
#print(len(df))

conn.close()