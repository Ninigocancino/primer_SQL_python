import sqlite3

conn = sqlite3.connect('Primer_SQL_python.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT,
    edad INTEGER
)
''')

cursor.execute("INSERT INTO usuarios (nombre,edad) VALUES ('Juan',23)")

conn.commit()

cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)

conn.close()