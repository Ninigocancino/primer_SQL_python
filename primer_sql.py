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


#CONSULTA 01: AGREGAR DATOS A LA BASE DE DATOS
#cursor.execute("INSERT INTO usuarios (nombre,edad) VALUES ('Juan', 23)")
#cursor.execute("INSERT INTO usuarios (nombre,edad) VALUES ('Matias', 22)")
#cursor.execute("INSERT INTO usuarios (nombre,edad) VALUES ('Laura', 25)")
cursor.execute("INSERT INTO usuarios (nombre,edad) VALUES ('Sara', 32)")
#conn.commit()

#CONSULTA 02: USUARIOS CON EDAD IGUAL 30 AÑOS
cursor.execute("SELECT * FROM usuarios WHERE edad = 30")
usuarios_30 = cursor.fetchall()

#IMPRIME el resultado de la consulta 02
print("Usuarios con edad 30:")
for usuario in usuarios_30:
    print(usuario)

#Imprime el resultado de la consulta 01 
print("")
print("Todos los registros")
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

for usuario in usuarios:
    print(usuario)

cursor.close()
conn.close()