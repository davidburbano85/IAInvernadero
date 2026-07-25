from sklearn.preprocessing import StandardScaler


def escalar(datos):

    datos = datos.copy()

    columnas = datos.select_dtypes(
        include=["number"]
    ).columns

    datos[columnas] = datos[columnas].astype(float)

    escalador = StandardScaler()

    datos[columnas] = escalador.fit_transform(
        datos[columnas]
    )

    return datos