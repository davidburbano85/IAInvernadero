def obtener_estadisticas(datos):

    cantidad = datos["cantidad"]

    return {
        "cantidad_registros": int(len(datos)),
        "promedio": round(float(cantidad.mean()), 2),
        "minimo": round(float(cantidad.min()), 2),
        "maximo": round(float(cantidad.max()), 2),
        "desviacion": round(float(cantidad.std()), 2),
        "mediana": round(float(cantidad.median()), 2)
    }