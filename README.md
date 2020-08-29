

# Desafío Ingeniero de Datos

## Requerimientos

Notas sobre los requerimientos:

* La solución está en un jupyter notebook con el nombre *main.ipnb*

* Sólo se han utilizado las librerías `pandas` y `matplotlib`

* para instalar las dependencias ejecutar el comando:

  ​	`pip install -r requirements.txt`

## Puntos a realizar 

###  Obligatorios

Para completar los análisis pedidos se han construido las clases `DataReader` y `Analyzer`:

* **DataReader**: Es un a clase que ofrece los métodos `append_year_data` para importar los datos que vienen separados por años  y `get_data` para obtener los datos importados y tabulados

* **Analizar**: Clase que contiene los métodos necesarios para realizar los análisis requeridos. 

  | Punto                         |     Realizado      |
  | ----------------------------- | :----------------: |
  | Histograma tiempos de viaje   | :heavy_check_mark: |
  | Top estaciones más utilizadas | :heavy_check_mark: |
  | Top trayectos                 | :heavy_check_mark: |
  | Horas punta                   | :heavy_check_mark: |

### Deseables

| Punto                                             |     Realizado      |
| ------------------------------------------------- | :----------------: |
| Pruebas unitarias                                 | :heavy_check_mark: |
| Comparación de utilización del sistema entre años | :heavy_check_mark: |
| Capacidad instalada                               |        :x:         |
| Comparación capacidad instalada entre años        |        :x:         |

### Ideales

| Punto                | Realizado |
| -------------------- | :-------: |
| Ampliación cobertura |    :x:    |
| Comparación densidad |    :x:    |
| Velocidad promedio   |    :x:    |
| Total bicicletas     |    :x:    |