from __future__ import annotations

import requests


BACKEND_URL = "https://agroinvernaderobackend.onrender.com/api"

SUPABASE_ANON_KEY = (
    "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9."
    "eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJyaXRs"
    "eGp3enJqcWJtcGZ1cmJ0Iiwicm9sZSI6ImFub24i"
    "LCJpYXQiOjE3ODQxNDI2MzQsImV4cCI6MjA5OTcx"
    "ODYzNH0.1pbkRBSxvZyDMlvlGR9XhAZPZFdejdy"
    "jOpRXwASjBA8"
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

    def obtener_instrumentos(
        self,
        invernadero_id: int
    ) -> list[dict]:

        respuesta = self._session.get(
            f"{BACKEND_URL}/Instrumento",
            params={
                "invernaderoId": invernadero_id
            },
            timeout=30
        )

        respuesta.raise_for_status()

        return respuesta.json()

    def obtener_mediciones(
        self,
        instrumento_id: int
    ) -> list[dict]:

        respuesta = self._session.get(
            f"{BACKEND_URL}/Medicion/instrumento/{instrumento_id}",
            timeout=30
        )

        respuesta.raise_for_status()

        return respuesta.json()


class Generador:

    def __init__(self, jwt: str):

        self.backend = BackendClient(jwt)

    def generar(
        self,
        invernadero_id: int
    ) -> dict:

        instrumentos = self.backend.obtener_instrumentos(
            invernadero_id
        )

        resultado = []

        for instrumento in instrumentos:

            tipo = instrumento.get("tipoInstrumento")

            if not tipo:
                continue

            nombre_tipo = (
                tipo.get("nombre") or ""
            ).strip().lower()

            # SOLO instrumentos cuyo tipo sea un sensor
            if not nombre_tipo.startswith("sensor"):
                continue

            instrumento_id = instrumento["id"]

            mediciones = self.backend.obtener_mediciones(
                instrumento_id
            )

            for medicion in mediciones:

                resultado.append(
                    {
                        "instrumento_id": instrumento_id,
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