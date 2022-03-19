import sqlite3
from craft_meats_bot.storageapp import storage

from craft_meats_bot.my_data import db

db = "../" + db


def storage_create_table():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    # TODO проставить внешние ключи
    cursor.execute("CREATE TABLE IF NOT EXISTS storages(\n"
                   "    storage_id INTEGER PRIMARY KEY NOT NULL,\n"
                   "    category_id INTEGER, \n"
                   "    product_id INTEGER, \n"
                   "    quantity INTEGER, \n"
                   "    weight REAL, \n"
                   "    storage_cost REAL, \n"
                   "    data_production DATA, \n"
                   "    user_id INTEGER, \n"
                   "    data_sale DATA, \n"
                   "    sale_bit BIT, \n"
                   "    order_id INTEGER \n"
                   ")")

    connect.commit()
    connect.close()


def storege_example():
    storage_list = [
        [1, 1, 1, 100, 160, "2022-03-10"],
        [1, 2, 2, 100, 160, "2022-03-10"],
        [1, 3, 1, 160, 240, "2022-03-10"],
        [1, 4, 1, 220, 350, "2022-03-10"],
        [2, 6, 1, 220, 220, "2022-03-10"],
        [3, 8, 1, 220, 220, "2022-03-10"]
    ]

    for stor in storage_list:
        storage_insert_new(stor)


def storage_insert_new(storage_list):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    cursor.execute(f"""INSERT INTO storages VALUES (NULL, ?, ?, ?, ?, ?, ?, NULL, NULL, 0, NULL);""", storage_list)
    connect.commit()


def storage_update(storage_update_list):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    cursor.execute(
        f"""
        UPDATE storages SET 
        (user_id, data_sale, sale_bit, order_id) = 
        ({storage_update_list[1]}, {storage_update_list[2]}, {storage_update_list[3]}, {storage_update_list[4]}) WHERE 
        storage_id = {storage_update_list[0]}
        """)

    connect.commit()


def get_cat_name(category_id):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    result = \
        cursor.execute(f"""SELECT category_name FROM category WHERE category_id == {category_id}""").fetchall()[0][0]
    connect.close()
    return result


def get_prod_name(product_id):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    result = \
        cursor.execute(f"""SELECT product_name FROM products WHERE product_id = {product_id}""").fetchall()[0][0]
    connect.close()
    return result


def get_weight(call):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    result = \
        cursor.execute(f"""SELECT weight FROM storages WHERE storage_id = {storage.get_storage_id(call)}""").fetchall()[
            0][0]
    connect.close()
    return result


def storage_cost(call):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    result = \
        cursor.execute(
            f"""SELECT storage_cost FROM storages WHERE storage_id = {storage.get_storage_id(call)}""").fetchall()[
            0][0]
    connect.close()
    return result


def get_storage_categories():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute("""SELECT DISTINCT category_id FROM storages WHERE sale_bit = 0""")
    categories = cursor.fetchall()
    connect.close()
    return categories


def get_storage_products(call):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute(
        f"""SELECT DISTINCT product_id FROM storages WHERE 
            category_id = ({storage.get_cat_id(call)}) and sale_bit = 0""")
    result = cursor.fetchall()
    connect.close()
    return result


def get_storage_meats_quantity(call):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute(
        f"""SELECT storage_id, weight, storage_cost FROM storages WHERE 
            category_id = {storage.get_cat_id(call)} AND 
            product_id = {storage.get_prod_id(call)}  AND 
            sale_bit = 0""")
    stor_info = cursor.fetchall()
    connect.close()
    return stor_info


def get_storage_confirm_orders(call):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute(
        f"""SELECT weight, storage_cost FROM storages WHERE storage_id = {storage.get_storage_id(call)}""")
    result = cursor.fetchall()[0]
    connect.close()
    return result
