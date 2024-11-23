import sqlite3

def create_connection(db_name):
    connection = None
    try:
        connection = sqlite3.connect(db_name)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_CONNECTION function')
    return connection

def create_table(connection, sql):
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_TABLE function')


def insert_products(connection, product):
    try:
        sql = '''INSERT INTO products(product_title, price, quantity)VALUES(?, ?, ?)'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in INSERT_PRODUCTS function')


def update_quantity(connection, product):
    try:
        sql = '''UPDATE  products SET price=?, WHERE id=?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in UPDATE_QUANTITY function')


def update_price(connection, product):
    try:
        sql = '''UPDATE  products SET quantity=?, WHERE id=?'''
        cursor = connection.cursor()
        cursor.execute(sql, product)
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in UPDATE_PRICE function')


def delete_by_id(connection, id):
    try:
        sql = '''DELETE FROM products WHERE id=?'''
        cursor = connection.cursor()
        cursor.execute(sql, (id,))
        connection.commit()
    except sqlite3.Error as error:
        print(f'{error} in DELETE_BY_ID function')


def select_all(connection):
    try:
        sql = '''SELECT * FROM products'''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_ALL function')


def select_by_price_quantity(connection, limit):
    try:
        sql = '''SELECT * FROM products
    WHERE price <= ? AND quantity >= ?'''
        cursor = connection.cursor()
        cursor.execute(sql, limit)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_BY_PRICE_QUANTITY function')


def select_by_name(connection):
    try:
        sql = '''SELECT * FROM products
        WHERE product_title LIKE '%KURUT%'
        '''
        cursor = connection.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print(f'{error} in SELECT_BY_NAME function')


sql_to_create_products_title = '''
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
'''

def create_table(db_name, sql):

    try:
        with sqlite3.connect (db_name) as connection:
            cursor = connection.cursor()
            cursor.execute(sql)
    except sqlite3.Error as error:
        print(f'{error} in CREATE_TABLE function')


my_connection = create_connection('products.db')
if my_connection:
    print('Connected successfully')
    create_table(my_connection, sql_to_create_products_title)
    insert_products(my_connection, ('Classic Chocolate', 120.50, 7))
    insert_products(my_connection, ('Milk Chocolate', 129.99, 3))
    insert_products(my_connection, ('White Chocolate', 143.99, 6))
    insert_products(my_connection, ('Black Chocolatr', 99.99, 10))
    insert_products(my_connection, ('Salted Chocolatr', 150.40, 8))
    insert_products(my_connection, ('Classic Marmalade', 145.50, 5))
    insert_products(my_connection, ('Berry Marmalade', 89.90, 12))
    insert_products(my_connection, ('Fruit Marmalade', 100.00, 7))
    insert_products(my_connection, ('Classic Kurut', 30.30, 15))
    insert_products(my_connection, ('Smoked Kurut', 35.50, 4))
    insert_products(my_connection, ('Mint Gum', 45.80, 3))
    insert_products(my_connection, ('Fruit Gum', 120.50, 7))
    insert_products(my_connection, ('Cheese Chips', 150.70, 4))
    insert_products(my_connection, ('Spisy Chips', 145.99, 7))
    insert_products(my_connection, ('Saldet Chips', 120.00, 2))
    update_price(my_connection, (200, 1))
    update_quantity(my_connection, (15,  11))
    delete_by_id(my_connection, 7)
    select_all(my_connection)
    select_by_price_quantity(my_connection, (90, 3))
    select_by_name(my_connection)

create_table(my_connection, sql_to_create_products_title)
