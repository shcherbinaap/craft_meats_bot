import sqlite3
from craft_meats_bot.my_data import db
db = "../" + db

def get_orders(call):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute(f"""SELECT * FROM orders WHERE user_id = ({call.message.chat.id}) and status_id in (1, 2, 3)""")
    result= cursor.fetchall()
    connect.close()
    return (result)


def get_cat_name(category_id):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute(f"""SELECT category_name FROM category WHERE category_id = {category_id}""")
    result= cursor.fetchall()[0][0]
    connect.close()
    return (result)

def get_prod_name(product_id):
    connect = sqlite3.connect(db)
    cursor = connect.cursor()

    cursor.execute(f"""SELECT product_name FROM products WHERE product_id = {product_id}""")
    result= cursor.fetchall()[0][0]
    connect.close()
    return (result)