ESTADOS = {
    1: "Normal",
    -1: "Advertencia"
}


MOTIVOS = {
    "Normal": "El comportamiento reciente coincide con el historial.",
    "Advertencia": "El comportamiento reciente difiere del historial.",
    "Desconocido": "No fue posible determinar el estado."
}


def generar_recomendacion(
    modelo,
    medicion,
    instrumento_id
):

    medicion = medicion.copy()

    probabilidades = modelo.predict_proba(medicion)[0]

    prediccion = modelo.predict(medicion)[0]

    confianza = round(
        float(max(probabilidades) * 100),
        2
    )

    estado = ESTADOS.get(
        prediccion,
        "Desconocido"
    )

    return {
        "instrumento_id": int(instrumento_id),
        "estado": estado,
        "confianza": confianza,
        "motivo": MOTIVOS[estado]
    }