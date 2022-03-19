import sqlite3
from craft_meats_bot.my_data import db


def category_creare_table():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS category(\n"
                   "    category_id INTEGER PRIMARY KEY NOT NULL,\n"
                   "    category_name VARCHAR,\n"
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
        ["Cыровяленое", "Сыровяленые изделия", 0, 1],
        ["Сырокопченое", "Сырокопченые изделия", 1, 1],
        ["Копчено-вареное", "Копчено-вареные изделия", 0, 1],
    ]

    for category in category_list:
        cursor.execute(f"""INSERT INTO category VALUES (NULL, ?, ?, ?, ?, ?);""", category)

    connect.commit()
    connect.close()


def product_create_table():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS products(\n"
                   "    product_id INTEGER PRIMARY KEY NOT NULL,\n"
                   "    product_name VARCHAR,\n"
                   "    product_decription VARCHAR, \n"
                   "    category_id INTEGER, \n"
                   "    product_active BIT, \n"
                   "    product_price REAL, \n"
                   "    product_time_cook INTEGER \n"
                   ")")

    connect.commit()
    connect.close()


def product_write_default():
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    product_list = [
        ["Cвиная шейка", "Сыровяленная свиная шейка",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Cыровяленое'""").fetchall()[0][0],
         1],
        ["Cвиной карбонад", "Сыровяленный свинй карбонад",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Cыровяленое'""").fetchall()[0][0],
         1],
        ["Свиная вырезка", "Сыровяленная свиная вырезка",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Cыровяленое'""").fetchall()[0][0],
         1],
        ["Грудка индейки", "Сыровяленная грудка индейки",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Cыровяленое'""").fetchall()[0][0],
         1],
        ["Говядина", "Сыровяленая говядина",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Cыровяленое'""").fetchall()[0][0],
         1],

        ["Свиная вырезка", "Сырокопченая свиная вырезкаа",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Сырокопченое'""").fetchall()[0][0],
         1],
        ["Грудка индейки", "Сырокопченая грудка индейки",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Сырокопченое'""").fetchall()[0][0],
         1],

        ["Свиной карбона", "Копчено-вареный свиной карбона",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Копчено-вареное'""").fetchall()[0][
             0],
         1],
        ["Грудка индейки", "Копчено-вареная грудка индейки",
         cursor.execute("""SELECT category_id FROM category WHERE category_name = 'Копчено-вареное'""").fetchall()[0][
             0],
         1],
    ]

    for product in product_list:
        cursor.execute(f"""INSERT INTO products VALUES (NULL, ?, ?, ?, ?, ?);""", product)

    connect.commit()
    connect.close()


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


if __name__ == '__main__':
    # category_creare_table()
    # category_write_default_data()
    # product_create_table()
    # product_write_default()
    pass
