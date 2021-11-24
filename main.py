import psycopg2
import matplotlib.pyplot as plt

username = 'danylenko'
password = 'danylenko'
database = 'danylenko_DB'
host = 'localhost'
port = '5432'


query_1 = '''
CREATE VIEW ProductTotalSpend AS
SELECT TRIM(product_name), SUM(order_quantity * product_price) FROM customers JOIN orders USING(customer_steamid) JOIN products USING(product_id) GROUP BY product_name ORDER BY sum DESC
'''

query_2 = '''
CREATE VIEW CustomerOrdersCount AS
SELECT TRIM(customer_steamid), COUNT(order_id) FROM customers LEFT JOIN orders USING(customer_steamid) GROUP BY customer_steamid
'''

query_3 = '''
CREATE VIEW OrdersDateCount AS
SELECT order_date, COUNT(*) FROM orders GROUP BY order_date ORDER BY order_date ASC
'''


con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)



with con:
    cur = con.cursor()



    cur.execute('DROP VIEW IF EXISTS ProductTotalSpend')

    cur.execute(query_1)

    cur.execute('SELECT * FROM ProductTotalSpend')

    graph_data = {}
    for row in cur:
        graph_data[row[0]] = row[1]

    plt.bar(graph_data.keys(), graph_data.values(), width=0.5)
    plt.xticks(rotation=45)
    plt.xlabel('Товари')
    plt.ylabel('Витрати')
    plt.show()



    cur.execute('DROP VIEW IF EXISTS CustomerOrdersCount')

    cur.execute(query_2)

    cur.execute('SELECT * FROM CustomerOrdersCount')

    graph_data = {}
    pie_values = [0, 0, 0, 0]
    for row in cur:
        graph_data[row[0]] = row[1]

    for key in graph_data:
        if graph_data[key] == 0:
            pie_values[0] += 1
        elif graph_data[key] <= 1:
            pie_values[1] += 1
        elif graph_data[key] <= 2:
            pie_values[2] += 1
        else:
            pie_values[3] += 1

    labels = ['Не робили замовлення', '1 замовлення', '2 замовлення', '3 або більше замовлень']
    fig, ax = plt.subplots()
    ax.pie(pie_values, labels=labels, autopct='%1.1f%%', shadow=True, wedgeprops={'lw': 1, 'ls': '--', 'edgecolor': "k"})
    ax.axis("equal")
    plt.show()



    cur.execute('DROP VIEW IF EXISTS OrdersDateCount')

    cur.execute(query_3)

    cur.execute('SELECT * FROM OrdersDateCount')

    graph_data = {}
    for row in cur:
        graph_data[row[0]] = row[1]


    fig, ax = plt.subplots()
    ax.plot(graph_data.keys(), graph_data.values(), )

    plt.xlabel('Дата')
    plt.ylabel('Кількість замовлень')
    plt.show()
