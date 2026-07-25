from modelo.recomendacion import generar_recomendacion


def generar_predicciones(
    modelo,
    mediciones
):

    predicciones = []

    ultimas_mediciones = (
        mediciones
        .sort_values("fecha_hora")
        .groupby("instrumento_id")
        .tail(1)
    )

    for _, medicion in ultimas_mediciones.iterrows():

        instrumento_id = int(
            medicion["instrumento_id"]
        )

        datos_modelo = (
            medicion
            .drop(
                labels=[
                    "Clase",
                    "magnitud"
                ],
                errors="ignore"
            )
            .to_frame()
            .T
        )

        predicciones.append(
            generar_recomendacion(
                modelo,
                datos_modelo,
                instrumento_id
            )
        )

    return predicciones