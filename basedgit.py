
import sqlite3
#Creamos la tabla en la base de datos
try:
    conexion = sqlite3.connect("BaseDatosUsuarios.db")
    cursor = conexion.cursor()
    cursor.execute("DROP TABLE IF EXISTS Usuarios")
    cursor.execute("CREATE TABLE IF NOT EXISTS Usuarios(codigo INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT NOT NULL, edad INTEGER)")
    conexion.commit()
    conexion.close()
    print("Base de datos creada o ya existente")
except sqlite3.Error as e:
    print(f"Error al crear o iniciar la BBDD: {e}")

def mostrar_todos_usuarios(): #Muestra todos los usuarios
    conexion = sqlite3.connect("BaseDatosUsuarios.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM Usuarios")
    usuario = cursor.fetchall()
    for i in usuario:
        print(i)
    conexion.close()

def insertar_usuarios(nombre, edad): #Insertar nuevos usuarios
    try:
        conexion = sqlite3.connect("BaseDatosUsuarios.db")
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO Usuarios(nombre, edad) VALUES (?, ?)", (nombre, edad))
        conexion.commit()
        conexion.close()
        print("Usuario creado con éxito.")
    except sqlite3.Error as e:
        print(f"Error al insertar datos en BBDD: {e}")

def modificar_usuarios(edad, nombre): #Modificamos usuarios
    try:
        conexion = sqlite3.connect("BaseDatosUsuarios.db")
        cursor = conexion.cursor()
        cursor.execute("UPDATE Usuarios SET edad=? where nombre= ?", (nombre, edad))
        conexion.commit()
        conexion.close()
        print("Usuario modificado con éxito.")
    except sqlite3.Error as e:
        print(f"Error al modificar datos en BBDD: {e}")

def consulta_usuarios_nombre(nombre=()): #Consulta usuarios por nombre.
    try:
        conexion = sqlite3.connect("BaseDatosUsuarios.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE nombre = ?",(nombre,))
        usuarios = cursor.fetchall()
        if usuarios:
            for i in usuarios:
                print(i)
        else:
            print(f"El usuario {nombre} no existe")
        conexion.close()
    except sqlite3.Error as e:
        print(f"Error en la consulta de BBDD: {e}")

def consulta_usuarios_edad(edad=()): #Consulta por edad
    try:
        conexion = sqlite3.connect("BaseDatosUsuarios.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE edad = ?",(edad,))
        usuarios = cursor.fetchall()
        for i in usuarios:
            print(i)        
        conexion.close()
    except sqlite3.Error as e:
        print(f"Error al mostrar datos en BBDD: {e}")

def eliminar_por_nombre(nombre): #Elimina al usuario por el nombre
    try:
        conexion = sqlite3.connect("BaseDatosUsuarios.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Usuarios WHERE nombre = ?", (nombre,))
        conexion.commit()
        conexion.close()
        print("Usuario eliminado con éxito.")
    except sqlite3.Error as e:
        print(f"Error al eliminar datos de la BBDD: {e}")

insertar_usuarios("Damian", "38")
insertar_usuarios("Jorge", "45")
insertar_usuarios("Maria", "24")
insertar_usuarios("Lucia", "22")

consulta_usuarios_edad("24")
consulta_usuarios_nombre("Damian")
eliminar_por_nombre("Lucia")
consulta_usuarios_nombre("Lucia")
modificar_usuarios("Jorge", "21")

mostrar_todos_usuarios()