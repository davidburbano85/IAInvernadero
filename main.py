# import numpy as np

# from config.configuracion import SEMILLA

# from autenticacionConexion.login import Login
# from sensores.generador import Generador

# from datos.procesamiento import (
#     crear_dataframe,
#     preparar_datos,
#     clasificar_mediciones
# )

# from datos.escalamiento import escalar

# from modelo.entrenamiento import entrenar
# from modelo.predicciones import generar_predicciones
# from modelo.evaluacion import evaluar

# from analisis.estadistica import obtener_estadisticas


# np.random.seed(SEMILLA)


# def ejecutar_modelo(jwt: str):

#     generador = Generador(jwt)

#     datos_backend = generador.generar()

#     mediciones = datos_backend["mediciones"]

#     datos = crear_dataframe(mediciones)

#     datos = preparar_datos(datos)

#     datos = clasificar_mediciones(datos)

#     print(datos["Clase"].value_counts())

#     estadisticas = obtener_estadisticas(datos)

#     datos_escalados = datos.copy()

#     columnas = [
#         "coordenada_x",
#         "coordenada_y",
#         "cantidad",
#         "fecha_hora",
#         "unidad_medicion"
#     ]

#     datos_escalados[columnas] = escalar(
#         datos_escalados[columnas]
#     )

#     modelo, x_prueba, y_prueba, datos_prueba = entrenar(
#         datos_escalados
#     )

#     metricas = evaluar(
#         modelo,
#         x_prueba,
#         y_prueba
#     )

#     predicciones = generar_predicciones(
#         modelo,
#         datos_prueba
#     )

#     return {
#         "estadisticas": estadisticas,
#         "metricas": metricas,
#         "predicciones": predicciones
#     }


# def main():

#     login = Login()

#     email = ""
#     password = ""

#     jwt = login.iniciar_sesion(
#         email,
#         password
#     )

#     return ejecutar_modelo(jwt)


# if __name__ == "__main__":

#     resultado = main()

#     print()
#     print(resultado["estadisticas"])

#     print()
#     print(resultado["metricas"])

#     print()

#     for prediccion in resultado["predicciones"]:
#         print(prediccion)



import numpy as np

from config.configuracion import SEMILLA

from sensores.generador import Generador

from datos.procesamiento import (
    crear_dataframe,
    preparar_datos,
    clasificar_mediciones
)

from datos.escalamiento import escalar

from modelo.entrenamiento import entrenar
from modelo.predicciones import generar_predicciones
from modelo.evaluacion import evaluar

from analisis.estadistica import obtener_estadisticas


np.random.seed(SEMILLA)


def ejecutar_modelo(jwt: str):

    generador = Generador(jwt)

    datos_backend = generador.generar()

    mediciones = datos_backend["mediciones"]

    datos = crear_dataframe(mediciones)

    datos = preparar_datos(datos)

    datos = clasificar_mediciones(datos)

    print(datos["Clase"].value_counts())

    estadisticas = obtener_estadisticas(datos)

    datos_escalados = datos.copy()

    columnas = [
        "coordenada_x",
        "coordenada_y",
        "cantidad",
        "fecha_hora",
        "unidad_medicion"
    ]

    datos_escalados[columnas] = escalar(
        datos_escalados[columnas]
    )

    modelo, x_prueba, y_prueba, datos_prueba = entrenar(
        datos_escalados
    )

    metricas = evaluar(
        modelo,
        x_prueba,
        y_prueba
    )

    predicciones = generar_predicciones(
        modelo,
        datos_prueba
    )

    return {
        "estadisticas": estadisticas,
        "metricas": metricas,
        "predicciones": predicciones
    }

