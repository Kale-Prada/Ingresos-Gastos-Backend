#Este archivo es la capa donde están las conexiones a la BBDD
#Separamos la lógica MVC (Modelo-Vista-Controlador)
#Modelo (M): Maneja los datos, la base de datos y la lógica de negocio-programa

from conexion import Conexion
import sqlite3

#Método "formato" Recibe una fila y la va recorriendo. Devuelve todos los valor con "fetchall"

def formato(respuesta):
    """
    Formato de salida de las consultas a la BBDD
    """
    lista_final=[]
    
    for fila in respuesta.fetchall():
        #con dict se convierte cada sqlite3.Row en un diccionario
        lista_final.append(dict(fila))
    return lista_final    

def select_all():
    """
    Función para consultar todos los registro en la tabla "movimiento" de la 
    BBDD "bd_ingresos_gastos.db"
        
    """
    conexionSelect = Conexion('SELECT * FROM movimiento;')
    respuesta = conexionSelect.res
    resp = formato(respuesta)
    conexionSelect.con.close()
    return resp

def select_by_id(id:int):
    """
    Función para consultar registro en la tabla "movimiento" de la BBDD "bd_ingresos_gastos.db"
    pasando como parámetro en el navegador el "id". 
    
    """
    conexionSelectBy = Conexion(f'SELECT * FROM movimiento WHERE id={id}')
    respuesta=conexionSelectBy.res
    resp = formato(respuesta)
    conexionSelectBy.con.close()
    return resp

def insert_data(data):
    """
    Función para insertar un nuevo registro en la tabla "movimiento" de 
    la BBDD "bd_ingresos_gastos.db"
    """
    try:
        conexionInsert=Conexion('INSERT INTO movimiento(date,concept,quantity) VALUES (?,?,?);',data)
        conexionInsert.res
        conexionInsert.con.commit()#para confirmar guardado
    except sqlite3.Error as error:
        print('Error: ',error)

    conexionInsert.con.close()

def update_data(id,data):
    """
    Función para actualizar un registro en la tabla "movimiento" pasándole el ID de la BBDD 
    como parámetro de la base de datos "bd_ingresos_gastos.db"
    """
    try:
        conexionUpdate=Conexion(f'UPDATE movimiento SET date=?,concept=?,quantity=? WHERE id={id};',data)
        conexionUpdate.res
        conexionUpdate.con.commit()#confirmar el update
    except sqlite3.Error as error:
            print('Error: ',error)
    conexionUpdate.con.close()

def delete_data(id:int):
    """
    Función para borrar registros en la tabla "movimiento" pasando como parámetro 
    en el navegador el ID del registro que quiero eliminar.
    """
    try:
        conexionDelete=Conexion(f'DELETE FROM movimiento WHERE id={id};')
        conexionDelete.res
        conexionDelete.con.commit()#confirmar el borrado
    except sqlite3.Error as error:
        print('Error: ',error)    
    conexionDelete.con.close()    

#Mostrar ingresos 
#Al recibir solo un dato se llama con "fetchone".Solo queremos el total de ingresos
def mostrar_ingresos():
    """
    Función para consultar a BBDD SQlite los ingresos de la tabla "movimiento" en
    la BBDD "bd_ingresos_gastos.db"
    """
    #Suma los ingresos con SUM
    conexionIngresos = Conexion('SELECT sum(quantity) from movimiento WHERE quantity > 0;')
    respuesta = conexionIngresos.res.fetchone()
    #Importante cerrar la conexión a la BBDD
    conexionIngresos.con.close() 
    if respuesta and respuesta[0] is not None:
        valor = respuesta [0]
    else:
        valor = 0
    return str(valor)
    
   
    return resp

#Mostrar gastos 
#Al recibir solo un dato se llama con "fetchone". Solo queremos el total de gastos
def mostrar_gastos():
    """
    Función para consultar a BBDD SQlite los gastos de la tabla "movimiento" en
    la BBDD "bd_ingresos_gastos.db"
    """
    #Suma los gastos con SUM
    conexionGastos = Conexion('SELECT sum(quantity) from movimiento WHERE quantity < 0;')
    respuesta = conexionGastos.res.fetchone()
    #Cierro la conexión a la base de datos
    conexionGastos.con.close() 
    if respuesta and respuesta[0] is not None:
        valor = respuesta[0]
    else:
        valor = 0
    return str(valor)