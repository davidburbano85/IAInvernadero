import requests

from config.configuracion import (
    BACKEND_URL,
    ENDPOINT_SENSORES
)


def obtener_datos_backend():
    url = BACKEND_URL + ENDPOINT_SENSORES
    respuesta = requests.get(url,timeout=10)
    respuesta.raise_for_status()
    datos = respuesta.json()
    return datos