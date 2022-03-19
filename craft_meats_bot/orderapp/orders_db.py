import sqlite3

from craft_meats_bot.my_data import db

db = "../" + db


def order_create_table():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS orders(\n"
                   "    order_id INTEGER PRIMARY KEY NOT NULL,\n"
                   "    user_id INTEGER ,\n"
                   "    category_id INTEGER , \n"
                   "    product_id INTEGER , \n"
                   "    quantity INTEGER, \n"
                   "    weight REAL , \n"
                   "    order_cost REAL , \n"
                   "    metro_station_id INTEGER, \n"
                   "    status_id INTEGER, \n"
                   "    data_create DATA, \n"
                   "    data_update DATA, \n"
                   "    data_close DATA, \n"
                   "    data_close_real DATA \n"
                   ")")

    connect.commit()
    connect.close()


def order_insert_new(order_list):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    cursor.execute(f"""INSERT INTO orders VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, NULL, NULL, NULL);""", order_list)
    connect.commit()
    return cursor.lastrowid


# TODO написать функцию обновления заказа
def order_update():
    pass


def get_categories():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    cursor.execute("""SELECT * FROM category""")
    result = cursor.fetchall()
    connect.close()
    return (result)


def get_prod_in_cat(cat_id):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute(f"""SELECT * FROM products WHERE category_id = ({cat_id})""")
    result = cursor.fetchall()
    connect.close()
    return result


def get_cat_name(cat_id):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    result = \
        cursor.execute(f"""SELECT category_name FROM category WHERE category_id = {cat_id}""").fetchall()[0][
            0]
    connect.close()
    return (result)

def get_prod_name(product_id):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    result = \
        cursor.execute(f"""SELECT product_name FROM products WHERE product_id = {product_id}""").fetchall()[0][0]
    connect.close()
    return (result)


if __name__ == '__main__':
    order_create_table()
