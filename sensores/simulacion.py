import random
from datetime import datetime, timedelta


SENSORES = {
    1: {
        "unidad": "°C",
        "normal": (22, 28),
        "anomalo": (10, 40)
    },
    2: {
        "unidad": "%",
        "normal": (50, 75),
        "anomalo": (15, 95)
    },
    3: {
        "unidad": "lux",
        "normal": (3000, 9000),
        "anomalo": (500, 12000)
    },
    4: {
        "unidad": "pH",
        "normal": (6.0, 7.0),
        "anomalo": (4.5, 8.5)
    }
}


def generar_mediciones(
    cantidad_registros=1000,
    cantidad_instrumentos=20
):

    mediciones = []

    fecha_inicial = datetime.now() - timedelta(days=30)

    for _ in range(cantidad_registros):

        instrumento_id = random.randint(
            1,
            cantidad_instrumentos
        )

        sensor_id = random.choice(list(SENSORES.keys()))

        sensor = SENSORES[sensor_id]

        fecha = fecha_inicial + timedelta(
            minutes=random.randint(0, 30 * 24 * 60)
        )

        if random.random() < 0.70:

            valor = random.uniform(
                sensor["normal"][0],
                sensor["normal"][1]
            )

        else:

            if random.random() < 0.5:

                valor = random.uniform(
                    sensor["anomalo"][0],
                    sensor["normal"][0]
                )

            else:

                valor = random.uniform(
                    sensor["normal"][1],
                    sensor["anomalo"][1]
                )

        mediciones.append({
            "instrumento_id": instrumento_id,
            "sensor_id": sensor_id,
            "coordenada_x": round(random.uniform(0, 100), 2),
            "coordenada_y": round(random.uniform(0, 100), 2),
            "cantidad": round(valor, 2),
            "unidad_medicion": sensor["unidad"],
            "fecha_hora": fecha.strftime("%Y-%m-%d %H:%M:%S")
        })

    return mediciones