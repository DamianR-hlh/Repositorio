# Haz un desarrollo en Python que mediante una base de datos SQLITE 3 realice una gestión completa de almacén, sabiendo que:
# Los productos tienen:
# -	Un ID que es un entero auto incrementable (PK)
# -	Un Nombre, que es un texto 
# -	Un Precio, que es un real
# -	Una Cantidad, que es un entero
# Quiero destacar que no se permiten nulos en ninguno de los campos.
# Además, nos debe permitir
# -	Insertar productos
# -	Actualizar productos
# -	Eliminar productos
# -	Seleccionar productos
# Debemos de realizar estas opciones dentro de funciones independientes. 
# Seguidamente indico posibles definiciones de dichas funciones:
import sqlite3
try:
    conexion = sqlite3.connect("bbddProd.db")
    cursor = conexion.cursor()
    cursor.execute("DROP TABLE IF EXISTS Productos")
    cursor.execute("CREATE TABLE IF NOT EXISTS Productos(ID INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, precio INTEGER NOT NULL, cantidad INTEGER NOT NULL)")
    conexion.commit()
    conexion.close()
    print("Base de datos creada")
except sqlite3.Error as e:
    print(f"Error al crear o iniciar la BD: {e}")

def mostrar_productos():
    conexion = sqlite3.connect("bbddProd.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Productos")
    productos = cursor.fetchall()
    for i in productos:
        print(i)
    conexion.close()
    
def insertar_producto(nombre, precio, cantidad):
    try:
        conexion = sqlite3.connect("bbddProd.db")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Productos(nombre, precio, cantidad) VALUES (?, ?, ?)", (nombre, precio, cantidad))
        conexion.commit()
        conexion.close()
        print(f"Producto: {nombre}, insertado correctamente.")
    except sqlite3.Error as e:
        print(f"Error al insertar datos en BD: {e}")

def actualizar_producto(nombre, precio, cantidad):
    try:
        conexion = sqlite3.connect("bbddProd.db")
        cursor = conexion.cursor()
        cursor.execute("UPDATE Productos SET precio=?, cantidad=? WHERE nombre=?", (precio, cantidad, nombre))
        conexion.commit()
        print(f"Producto {nombre}. Precio: {precio}. Cantidad: {cantidad}, actualizado correctamente.")
        conexion.close()
    except sqlite3.Error as error:
        print("Error al actualizar el producto:", error)

def eliminar_producto_x_ID(ID):
    try:
        conexion = sqlite3.connect("bbddProd.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Productos where ID = ?", (ID,))
        conexion.commit()
        conexion.close()
        print("Producto eliminado con éxito")
    except sqlite3.Error as e:
        print(f"Error al eliminar productos en BD: {e}")

insertar_producto("tornillo", 25, 100)
insertar_producto("martillo", 7, 5)
insertar_producto("llave", 2, 10)
mostrar_productos()
print("...........")
actualizar_producto("martillo", 7, 2)
print("............")
eliminar_producto_x_ID(1)
print("............")
mostrar_productos()
print("............")

