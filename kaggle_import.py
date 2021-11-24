import csv
import decimal
import psycopg2

username = 'danylenko'
password = 'danylenko'
database = 'danylenko_DB'
host = 'localhost'
port = '5432'

INPUT_CSV_FILE = 'products.csv'

query_0 = '''
CREATE TABLE products_new
( 
    product_id     integer        UNIQUE NOT NULL,
    product_name   character(50)  NULL,
    product_price  numeric(5,2)   NULL,
    CONSTRAINT pk_products_new PRIMARY KEY (product_id)
)
'''

query_1 = '''
DELETE FROM products_new
'''

query_2 = '''
INSERT INTO products_new (product_id, product_name, product_price) VALUES (%s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:

    cur = conn.cursor()
    cur.execute(query_0)
    cur.execute(query_1)

    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)

        for idx, row in enumerate(reader):
            price = decimal.Decimal(row['Product_Price'])
            values = (row['Product_ID'], row['Product_Name'], price)
            cur.execute(query_2, values)

    conn.commit()
