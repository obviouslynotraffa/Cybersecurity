import sqlite3

connection=sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur=connection.cursor()

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('029ee67de769468bf1596fb3fcef8179', '7c6a180b36896a0a8c02787eeafb0e4c'))

cur.execute("INSERT INTO users (username, password) VALUES (?, ?)",
            ('c72e2158c941635b8ab6c33abcadf6da', '6cb75f652a9b52798eb6cf2201057c73'))

connection.commit()
connection.close()
