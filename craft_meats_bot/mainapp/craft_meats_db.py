import sqlite3
from craft_meats_bot.my_data import db

db = "../" + db


def users_insert_new(user_list):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()
    result = cursor.execute(f"""SELECT user_id FROM users WHERE user_id = {user_list[0]}""")
    result = result.fetchall()
    if len(result) == 0:
        cursor.execute(f"""INSERT INTO users VALUES (?, ?, ?);""", user_list)
        connect.commit()
    connect.close()


# TODO
def category_add_new():
    pass


# =========================================================
# status

# def status_create_table():
#     connect = sqlite3.connect(db)
#     cursor = connect.cursor()
#
#     cursor.execute("CREATE TABLE IF NOT EXISTS status(\n"
#                    "    status_id INTEGER PRIMARY KEY NOT NULL,\n"
#                    "    status_name VARCHAR,\n"
#                    "    status_active BIT \n"
#                    ")")
#     connect.commit()
#     connect.close()
#
#
# def status_write_default():
#     connect = sqlite3.connect(db)
#     cursor = connect.cursor()
#
#     status_list = [
#         ["Заказ принят", 1],
#         ["Заказ в производстве", 1],
#         ["Заказ готов к отгрузке", 1],
#         ["Заказ оплачен", 1],
#         ["Заказ выполнен", 1],
#     ]
#
#     for status in status_list:
#         cursor.execute(f"""INSERT INTO status VALUES (NULL, ?, ?, ?, ?);""", status)
#
#     connect.commit()
#     connect.close()
#
#
# def status_insert_new(status_list):
#     pass
#
#
# def status_update(status_list):
#     pass


if __name__ == '__main__':
    # users_create_table()
    # status_create_table()
    # status_write_default()
    # metro_station_create_table()
    # metro_station_write_default()

    pass
