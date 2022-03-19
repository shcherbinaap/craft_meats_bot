import sqlite3
from craft_meats_bot.my_data import db
db = "../" + db




# =========================================================
# category
def category_creare_table():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS category(\n"
                   "    category_id INTEGER PRIMARY KEY NOT NULL,\n"
                   "    category_name VARCHAR,\n"
                   "    category_short_name VARCHAR, \n"
                   "    category_decription VARCHAR, \n"
                   "    category_active BIT, \n"
                   "    category_active_storege BIT \n"
                   ")")
    connect.commit()
    connect.close()


def category_write_default_data():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    category_list = [
        ["Cыровяленое", "sv", "Сыровяленые изделия", 0, 1],
        ["Сырокопченое", "sk", "Сырокопченые изделия", 1, 1],
        ["Копчено-вареное", "kv", "Копчено-вареные изделия", 0, 1],
    ]

    for category in category_list:
        cursor.execute(f"""INSERT INTO category VALUES (NULL, ?, ?, ?, ?, ?);""", category)

    connect.commit()
    connect.close()

# TODO
def category_add_new():
    pass


def category_update_active_field(category_name, category_active):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    cursor.execute(
        f"""UPDATE category SET (category_active)  = ({category_active}) WHERE category_name = {category_name}""")
    connect.commit()
    connect.close()


def category_get_short_name_list():
    category_list = []
    i = 0
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute("""SELECT category_short_name FROM category """)
    result = cursor.fetchall()

    for category in result:
        category_list.append(category[0])
    # print(category_list)
    return category_list

# TODO
def activate_category_for_orders():
    pass

# TODO
def deactivate_category_for_orders():
    pass


# =========================================================
# product

def product_create_table():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    # TODO перенести информацию с meat_info
    cursor.execute("CREATE TABLE IF NOT EXISTS products(\n"
                   "    product_id INTEGER PRIMARY KEY NOT NULL,\n"
                   "    product_name VARCHAR,\n"
                   "    product_short_name VARCHAR, \n"
                   "    product_decription VARCHAR, \n"
                   "    category_id INTEGER, \n"
                   "    product_active BIT \n"
                   ")")

    connect.commit()
    connect.close()


def product_write_default():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    product_list = [
        ["Cвиная шейка", "svneck", "Сыровяленная свиная шейка",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Cыровяленое'""").fetchall()[0][0],
         1],
        ["Cвиной карбонад", "svback", "Сыровяленный свинй карбонад",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Cыровяленое'""").fetchall()[0][0],
         1],
        ["Свиная вырезка", "svloin", "Сыровяленная свиная вырезка",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Cыровяленое'""").fetchall()[0][0],
         1],
        ["Грудка индейки", "svgobbler", "Сыровяленная грудка индейки",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Cыровяленое'""").fetchall()[0][0],
         1],
        ["Говядина", "svbeef", "Сыровяленая говядина",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Cыровяленое'""").fetchall()[0][0],
         1],

        ["Свиная вырезка", "skloin", "Сырокопченая свиная вырезкаа",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Сырокопченое'""").fetchall()[0][0],
         1],
        ["Грудка индейки", "skgobbler", "Сырокопченая грудка индейки",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Сырокопченое'""").fetchall()[0][0],
         1],

        ["Свиной карбона", "kvloin", "Копчено-вареный свиной карбона",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Копчено-вареное'""").fetchall()[0][
             0],
         1],
        ["Грудка индейки", "kvgobbler", "Копчено-вареная грудка индейки",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Копчено-вареное'""").fetchall()[0][
             0],
         1],
    ]

    for product in product_list:
        cursor.execute(f"""INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?);""", product)

    connect.commit()
    connect.close()


def product_get_short_name_list():
    product_list = []
    i = 0
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute("""SELECT product_short_name FROM products """)
    result = cursor.fetchall()

    for product in result:
        product_list.append(product[0])
    # print(category_list)
    return product_list

# TODO
def activate_product_for_orders():
    pass

# TODO
def deactivate_product_for_orders():
    pass

# =========================================================
# status

def status_create_table():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS status(\n"
                   "    status_id INTEGER PRIMARY KEY NOT NULL,\n"
                   "    status_name VARCHAR,\n"
                   "    status_short_name VARCHAR, \n"
                   "    status_decription VARCHAR, \n"
                   "    status_active BIT \n"
                   ")")
    connect.commit()
    connect.close()


def status_write_default():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    status_list = [
        ["Заказ принят", "order_accept", "Заказ принят и скоро будет в обработан", 1],
        ["Заказ в производстве", "order_in_production", "Заказ в производстве", 1],
        ["Заказ готов к отгрузке", "", "", 1],
        ["Заказ оплачен", "", "", 1],
        ["Заказ выполнен", "", "", 1],
    ]

    for status in status_list:
        cursor.execute(f"""INSERT INTO status VALUES (NULL, ?, ?, ?, ?);""", status)

    connect.commit()
    connect.close()


def status_insert_new(status_list):
    pass


def status_update(status_list):
    pass


# =========================================================
# users
def users_create_table():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users(\n"
                   "    user_id INTEGER,\n"
                   "    first_name VARCHAR, \n"
                   "    username VARCHAR \n"
                   ")")

    connect.commit()
    connect.close()


def users_insert_new(user_list):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    result = cursor.execute(f"""SELECT user_id FROM users WHERE user_id = {user_list[0]}""")
    result = result.fetchall()
    if len(result) == 0:
        cursor.execute(f"""INSERT INTO users VALUES (?, ?, ?);""", user_list)
        connect.commit()
    connect.close()







# =========================================================
# metro_station

def metro_station_create_table():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS metro_stations(\n"
                   "    metro_station_id INTEGER PRIMARY KEY NOT NULL,\n"
                   "    metro_station_name VARCHAR,\n"
                   "    metro_station_active BIT \n"
                   ")")
    connect.commit()
    connect.close()


def metro_station_write_default():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    metro_station_list = [
        ["Планерная", 1],
        ["Сходненская", 1],
        ["Октябрьское поле", 1],

    ]

    for metro_station in metro_station_list:
        cursor.execute(f"""INSERT INTO metro_stations VALUES (NULL, ?, ?);""", metro_station)

    connect.commit()
    connect.close()


# =========================================================
# meats_info

def meats_info_create_table():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    # TODO: Внешний ключ для product_id
    cursor.execute("CREATE TABLE IF NOT EXISTS meats_info(\n"
                   "    product_id INTEGER KEY NOT NULL,\n"
                   "    meat_info MESSAGE_TEXT ,\n"
                   "    meat_price REAL\n"
                   "    meat_time_cook INTEGER \n"
                   "FOREIGN KEY (product_id) REFERENCES products(product_id)"
                   ")")
    connect.commit()
    connect.close()


def meats_info_write_default():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    # TODO: Добавить описание мяса
    meats_info_list = [
        [""]

    ]

    for meat_info in meats_info_list:
        cursor.execute(f"""INSERT INTO meats_info VALUES (NULL, ?, ?);""", meat_info)

    connect.commit()
    connect.close()


if __name__ == '__main__':
    # category_creare_table()
    # category_write_default_data()
    # product_create_table()
    # product_write_default()
    # users_create_table()
    # status_create_table()
    # status_write_default()
    # metro_station_create_table()
    # metro_station_write_default()






    pass
