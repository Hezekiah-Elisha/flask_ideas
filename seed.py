import sqlite3

connection = sqlite3.connect('flask_intro.db', check_same_thread = False)
cursor = connection.cursor()

cursor.execute(
    """INSERT INTO users(
        username,
        password,
        favorite_color
    ) VALUES (
        'Hezekiah',
        'elisha',
        'blue'
    );"""
)
cursor.execute(
    """INSERT INTO users(
        username,
        password,
        favorite_color
    ) VALUES (
        'Reuben',
        'olefa',
        'red'
    );"""
)
connection.commit()
cursor.close()
connection.close()

# sqlite> select * from users;
# 1|Hezekiah|elisha|blue
# 2|Reuben|olefa|red
