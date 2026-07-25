import pandas as pd


def crear_dataframe(datos):

    return pd.DataFrame(datos)

def preparar_datos(df):

    unidades = {
        "°C": 1,
        "%": 2,
        "lux": 3,
        "pH": 4
    }

    df["unidad_medicion"] = df["unidad_medicion"].map(unidades)

    df["fecha_hora"] = (
        pd.to_datetime(df["fecha_hora"])
        .astype("int64")
        // 10**9
    )

    return df


def clasificar_mediciones(df):

    rangos = {
        1: (18, 30),
        2: (40, 85),
        3: (2000, 10000),
        4: (5.8, 7.2)
    }

    def clasificar(fila):

        minimo, maximo = rangos.get(
            fila["unidad_medicion"],
            (None, None)
        )

        if minimo is None:
            return -1

        return 1 if minimo <= fila["cantidad"] <= maximo else -1

    df["Clase"] = df.apply(
        clasificar,
        axis=1
    )

    return df
    