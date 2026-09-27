# Aplicación API de Ingresos/Gastos 

**Aplicación realizada con FastAPI y base de datos con SQLite**

Realiza consultas SQL a una tabla llamada "movimiento" de una base de datos ""bd_ingresos_gastos.db" creada con "DB Browser for SQLite" 

Se pueden hacer consultas de los registros de toda la tabla, un registro en particular pasando como parámetro el id, eliminar registro, actualizar y agregar. 

Tambien suma los gastos y las ingresos de la tabla "movimiento". 


## Acerca de las herramientas usadas:

**FastAPI:**   

(Descarga FastAPI) [https://fastapi.tiangolo.com/]



Framework web moderno, Open Source, rápido, de alto rendimiento. Facilita la creación rápida de APIs modernas en Python con validación automática de datos y documentación interactiva. Buscar ser lo más intuitivo y eficiente posible.

La clave de su diseño es la simplicidad a través de la estandarización basada en estándares abiertos como OpenAPI y JSON Schema, y explota al máximo las anotaciones de tipo de Python y Pydantic.

El creador de FastAPI es el desarrollador colombiano Sebastián Ramírez, conocido en la comunidad de programación y en GitHub bajo el seudónimo de *tiangolo*.

**SQlite:**   
(Descarga SQLite) [https://www.sqlite.org/]

Sistema de gestión de bases de datos relacional. Crea un único archivo ordinario en disco que se puede guardar en cualquier carpeta del equipo. 

Sus características principales: de código abierto, sin servidor (Serverless), embedida (Embedded), un solo archivo, muy ligera. 

Creado por el desarrollador estadounidense D. Richard Hipp en el año 2000.

**DB Browser for SQLite:** 

Programa muy popular para trabajar con BBDD: ver tablas, buscar datos y ejecutar comandos SQL como si fuera una hoja de cálculo. Compatible con Windows, Mac y Linux. Muy sencillo de usar. 

## Detalles para ejecutar el backend:


## Instalación y Ejecución

1. Clona o descarga el repositorio en tu equipo.
2. Abre la carpeta del proyecto en Visual Studio Code.
3. Crea y activa un entorno virtual:
   ```bash
    # Para crear el entorno: 
    # En Windows: 
    python -m venv entorno
    
    #Otra opción: 
    py -m venv entorno 

    # En MacOS: 
    python3 -m venv entorno

    # Para activar el entorno: 
    # En Windows:
    .\entorno\Scripts\activate

    # En macOS/Linux:
    source entorno/bin/activate
   ```
4. Instala las librerías necesarias ejecutando:
   ```bash
   # En Windows:
   pip install -r requirements.txt

   # En macOS/Linux:
   pip3 install -r requirements.txt
   ```

## Requerimientos
Instala requirements.txt o ten en cuenta estas librerías: 

- agent-detector==2.0.0
- annotated-doc==0.0.5
- annotated-types==0.8.0
- anyio==4.15.1
- certifi==2026.7.22
- click==8.5.0
- detect-installer==0.2.1
- dnspython==2.8.0
- email-validator==2.3.0
- fastapi==0.141.1
- fastapi-cli==0.0.32
- fastapi-cloud-cli==0.26.0
- fastar==0.12.0
- h11==0.16.0
- httpcore==1.0.9
- httptools==0.8.0
- httpx==0.28.1
- idna==3.20
- Jinja2==3.1.6
- markdown-it-py==4.2.0
- MarkupSafe==3.0.3
- mdurl==0.1.2
- pydantic==2.13.5
- pydantic-extra-types==2.11.1
- pydantic-settings==2.15.0
- pydantic_core==2.46.5
- Pygments==2.21.0
- python-dotenv==1.2.3
- python-multipart==0.0.32
- PyYAML==6.0.3
- rich==15.0.0
- rich-toolkit==0.20.5
- rignore==0.8.1
- sentry-sdk==2.70.0
- shellingham==1.5.4
- starlette==1.7.0
- typer==0.27.2
- typing-inspection==0.4.4
- typing_extensions==4.16.0
- urllib3==2.8.0
- uvicorn==0.54.0
- uvloop==0.22.1
- watchfiles==1.3.0
- websockets==17.1


## Licencia

Autor = Keepcoding España S.L.U.