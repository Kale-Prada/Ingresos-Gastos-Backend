#Trabajamos nuestras rutas con FastAPI 
#Separamos la lógica MVC (Modelo-Vista-Controlador)
# Vista Controlador (C): Recibe las peticiones del usuario, pide los datos al modelo y 
# decide qué vista mostrar


#Activo el entorno 
from fastapi import FastAPI
from consultas import *
from pydantic import BaseModel

#Declaro calse para usar libreria de pydantic: BaseModel 
#Se usa para pasar el formato como "Body" y sea interpretado
#en Yaak, por ejemplo. 
class ModelMovimiento(BaseModel):
    date:str
    concept:str
    quantity:float


#Declarar variable - objeto de la clase FastAPI llamada "app" y la igualamos a la clase FasAPI. 
app = FastAPI()

#Detrás de ese objeto creamos rutas que vayamos a usar

#Para enrutar como petición HTTP, llamo a la variable con decorador @ y luego método HTTP "get" 
#Creo la ruta "/movimientos" será a donde me voy en la URL. 
#@app.get("/movimientos",tags=['Movimiento'])  #"tags" es para que muestre la documentación por secciones. 
#def index():
#    return "hola" 

#Consulta todos los registros de la tabla "movimientos" 
@app.get("/movimientos",tags=['Movimiento'])  #"tags" es para que muestre la documentación por secciones. 
def index():
    return select_all()

#Consulta de ingresos (muestra la suma) en la tabla "movimientos"
@app.get("/movimientos/ingresos",tags=['Movimiento'])  #"tags" es para que muestre la documentación por secciones. 
def movimiento_ingresos():
    return mostrar_ingresos()

#Consulta de gastos (muestra el total de gastos) en la tabla "movimientos"
@app.get("/movimientos/gastos",tags=['Movimiento'])  #"tags" es para que muestre la documentación por secciones. 
def movimiento_gastos():
    return mostrar_gastos()

#Consulta registros a través del "id"
@app.get("/movimientos/{id}",tags=['Movimiento'])
def movimiento_by_id(id:int):
    return select_by_id(id)

#Insertar registro en la tabla "movimiento" de la BBDD
@app.post("/movimientos",tags=['Movimiento'])
def movimiento_registro(body:ModelMovimiento):
    #Método para transformar todo a diccinario (el cuerpo)
    #print("Aqui: ",body.model_dump()) #Me lo muestra como un diccionario 
    #return body.model_dump()

    #Para mostrar campo por campo, pasando los objetos directamente
    #print("Aqui :",body.date)
    #print("Aqui :",body.concept)
    #print("Aqui :",body.quantity)

    #Controlamos con try except 
    try:
        insert_data([body.date,body.concept,body.quantity])
        return {'mensaje':'Registro correcto'}

    except Exception as ex:
        print(ex)
        return {'error':'Ha fallado el registro'}


#Actualizar un registro con el método PUT
@app.put("/movimientos/{id}",tags=['Movimiento'])
#En BBDD en ningún caso se envía el ID por eso solo usamos un 
#La BBDD ya crea su ID incremental 
def movimiento_update(id:int,body:ModelMovimiento):
    try:
        update_data(id,[body.date,body.concept,body.quantity])
        return {'Mensaje':'Registro actualizado correctamente'}

    except Exception as ex:
        print(ex)
        return {'Error':'Ha fallado la actualización'}


#Borrar un registro con el método DELETE
@app.delete("/movimientos/{id}",tags={'Movimiento'})
def movimiento_borrado(id:int):
    try:
        delete_data(id)
        return {'Mensaje':'Registro borrado correctamente'}

    except Exception as ex: 
        print(ex)
        return {'Error':'Ha fallado la eliminación del registro'}

