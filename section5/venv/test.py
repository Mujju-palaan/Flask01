import sqlite3

Connection = sqlite3.connect('data.db')

cursor = Connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)

user = (1, 'thuss', 'lol')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)

users = [
    (2, 'salman', 'noob'),
    (3, 'mujju', 'yoyo')
]
cursor.execute(insert_query, users)

select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)

Connection.commit()

Connection.close()


