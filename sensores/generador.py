from __future__ import annotations

import requests


BACKEND_URL = "https://agroinvernaderobackend.onrender.com/api"

SUPABASE_ANON_KEY = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJpc3MiOiJzdXBhYmFzIiwicm9sZSI6ImFub24i"
    # ...
)


class BackendClient:

    def __init__(self, jwt: str):

        self._session = requests.Session()

        self._session.headers.update(
            {
                "Authorization": f"Bearer {jwt}",
                "apikey": SUPABASE_ANON_KEY,
                "Content-Type": "application/json",
            }
        )

    def obtener_instrumentos(self) -> list[dict]:

        respuesta = self._session.get(
            f"{BACKEND_URL}/Instrumento",
            timeout=30
        )

        respuesta.raise_for_status()

        return respuesta.json()

    def obtener_mediciones(self, instrumento_id: int) -> list[dict]:

        respuesta = self._session.get(
            f"{BACKEND_URL}/Medicion/instrumento/{instrumento_id}",
            timeout=30
        )

        respuesta.raise_for_status()

        return respuesta.json()


class Generador:

    def __init__(self, jwt: str, controlador_id: int):

        self.backend = BackendClient(jwt)
        self.controlador_id = controlador_id

    def generar(self) -> dict:

        instrumentos = [
            instrumento
            for instrumento in self.backend.obtener_instrumentos()
            if instrumento["controladorId"] == self.controlador_id
        ]

        resultado = []

        for instrumento in instrumentos:

            tipo = instrumento["tipoInstrumento"]
            nombre_tipo = tipo["nombre"].strip().lower()

            if "sensor" not in nombre_tipo:
                continue

            mediciones = self.backend.obtener_mediciones(
                instrumento["id"]
            )

            for medicion in mediciones:

                resultado.append(
                    {
                        "instrumento_id": instrumento["id"],
                        "coordenada_x": medicion["coordenadaX"],
                        "coordenada_y": medicion["coordenadaY"],
                        "cantidad": medicion["cantidad"],
                        "fecha_hora": medicion["fechaHora"],
                        "magnitud": tipo["nombre"],
                        "unidad_medicion": tipo["unidadMedida"],
                    }
                )

        return {
            "instrumentos": instrumentos,
            "mediciones": resultado,
        }