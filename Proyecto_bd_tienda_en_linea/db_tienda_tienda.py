#Conexión de de Python con SQLite
import sqlite3

conexion = sqlite3.connect("tienda_tienda.db")

cursor = conexion.cursor()