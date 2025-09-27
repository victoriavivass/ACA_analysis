# Programación para la Ciencia de Datos - PEC4

**Autora:** María Victoria Vivas Gutiérrez  
**Fecha de entrega:** junio de 2025

## Descripción
Este proyecto forma parte de la evaluación continuada de la asignatura y tiene como objetivo desarrollar un paquete de Python modular para analizar el volumen de agua del Pantano de la Baells. Se estructura en cinco módulos que contienen distintos análisis y funcionalidades.

## Instalación
Para instalar y ejecutar el proyecto, sigue los siguientes pasos:

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
pip install -r requirements.txt
```
Para ejecutar el análisis completo:

```bash
python main.py
```
También puedes ejecutar módulos específicos: 

 ```bash
 python main.py -ex 3  # Ejecuta hasta el módulo 3
```
## Estructura del proyecto

PythonProject/
│── .idea/                   # Archivos de configuración de PyCharm
│── .venv/                   # Entorno virtual de Python
│── img/                     # Carpeta donde se almacenan las imágenes generadas
│── test/                    # Carpeta de pruebas unitarias
│   ├── test_modulo1.py      # Test para módulo 1
│   ├── test_modulo2.py      # Test para módulo 2
│   ├── test_modulo3.py      # Test para módulo 3
│   ├── test_modulo4.py      # Test para módulo 4
│   ├── test_modulo5.py      # Test para módulo 5
│── modulo1.py               # Carga y exploración de datos
│── modulo2.py               # Limpieza y filtrado de datos
│── modulo3.py               # Transformaciones temporales y visualización
│── modulo4.py               # Suavizado de datos y tendencias
│── modulo5.py               # Identificación de periodos de sequía
│── main.py                  # Archivo principal que ejecuta todo el análisis
│── requirements.txt          # Archivo de dependencias necesarias
│── README.md                 # Documentación del proyecto

## Ejercicios Realizados

### 1. Carga y Exploración de Datos (Modulo 1)
Este módulo descarga el dataset desde la API y lo carga en un `DataFrame` de Pandas utilizando `requests`. Además:
- Se muestran las primeras cinco filas para obtener una vista preliminar de los datos.
- Se imprime la estructura general de las columnas.
- Se proporciona un resumen de la información del DataFrame mediante `df.info()`.

### 2. Limpieza y Filtrado de Datos (Modulo 2)
En este módulo se realiza la limpieza y organización de los datos:
- Se renombran las columnas utilizando un diccionario para mayor claridad.
- Se normalizan los nombres de los pantanos usando expresiones regulares.
- Se filtran los datos exclusivamente para el Pantano de **La Baells**.

### 3. Transformaciones Temporales y Visualización (Modulo 3)
Aquí se trabaja con el manejo de fechas y la primera visualización de datos:
- Se convierte la columna `dia` a tipo `datetime` para un mejor análisis.
- Se ordena el dataset cronológicamente para facilitar la interpretación.
- Se identifica la fecha más antigua y la más reciente en el dataset.
- Se crea la columna `dia_decimal`, transformando las fechas a valores decimales para análisis matemáticos.
- Se genera una gráfica mostrando la evolución del volumen de agua del pantano y se guarda la imagen en `img/`.

### 4. Suavizado de Datos y Tendencias (Modulo 4)
Este módulo se enfoca en el procesamiento y visualización de tendencias:
- Se aplica el filtro `savgol_filter` de `scipy` para suavizar la variabilidad del volumen de agua.
- Se compara gráficamente la señal original con la versión suavizada.
- Se guarda la imagen generada en `img/` con el nombre del alumno.

### 5. Identificación de Periodos de Sequía (Modulo 5)
En este módulo se identifican los periodos de sequía en función de los datos suavizados:
- Se implementa la función `calcula_periodos()` para detectar los periodos de sequía en los datos.
- Se definen los periodos de sequía cuando el porcentaje embalsado cae por debajo del 60%.
- Se imprimen los periodos detectados en formato de lista con fechas de inicio y fin.


