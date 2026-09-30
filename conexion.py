#Separamos la lógica MVC (Modelo-Vista-Controlador)
#Clase "Conexion" para conectarnos a la base de datos

import sqlite3

class Conexion:
    def __init__(self,sql_query,parametro=[]): #Inicializo clase y lista vacía [] por default. 
        #conectar a la BBDD
        self.con=sqlite3.connect("bd_ingresos_gastos.db") 
        #row factory para poder formatearlo 
        self.con.row_factory = sqlite3.Row  
        #creo el objeto de clase "cursor" para poder ejecutar las consultas contra SQlite a través de este método.  
        self.cur = self.con.cursor()
        #Le paso la query "sql_query" y "parametro" en el caso que quiera hacer un INSERT / UPDATW, por ejemplo, en una lista. 
        self.res = self.cur.execute(sql_query,parametro)