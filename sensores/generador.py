# from __future__ import annotations

# import requests


# BACKEND_URL = "https://agroinvernaderobackend.onrender.com/api"

# SUPABASE_ANNON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJyaXRseGp3enJqcWJtcGZ1cmJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODQxNDI2MzQsImV4cCI6MjA5OTcxODYzNH0.1pbkRBSxvZyDMlvlGR9XhAZPZFdejdyjOpRXwASjBA8"


# class BackendClient:

#     def __init__(self, jwt: str):

#         self._session = requests.Session()

#         self._session.headers.update(
#             {
#                 "Authorization": f"Bearer {jwt}",
#                 "apikey": SUPABASE_ANNON_KEY,
#                 "Content-Type": "application/json",
#             }
#         )

#     def obtener_instrumentos(self) -> list[dict]:

#         respuesta = self._session.get(
#     f"{BACKEND_URL}/Instrumento",
#     timeout=30
#         )

        

#         respuesta.raise_for_status()

#         return respuesta.json()

#     def obtener_mediciones(self) -> list[dict]:

#         respuesta = self._session.get(
#             f"{BACKEND_URL}/Medicion",
#             timeout=30
#         )

        

#         respuesta.raise_for_status()

#         return respuesta.json()


# class Generador:

#     def __init__(self, jwt: str):

#         self.backend = BackendClient(jwt)

#     def generar(self) -> dict:

#         instrumentos = {
#             instrumento["id"]: instrumento
#             for instrumento in self.backend.obtener_instrumentos()
#         }

#         mediciones = self.backend.obtener_mediciones()

#         resultado = []

#         for medicion in mediciones:

#             instrumento_id = medicion["instrumentoId"]

#             instrumento = instrumentos.get(instrumento_id)

#             if instrumento is None:
#                 print(f"Instrumento {instrumento_id} no encontrado.")
#                 continue

#             referencia = instrumento["referencia"].strip().lower()

#             if referencia.startswith("actuador"):
#                 continue

#             tipo = instrumento["tipoInstrumento"]

#             resultado.append(
#                 {
#                     "instrumento_id": instrumento_id,
#                     "coordenada_x": medicion["coordenadaX"],
#                     "coordenada_y": medicion["coordenadaY"],
#                     "cantidad": medicion["cantidad"],
#                     "fecha_hora": medicion["fechaHora"],
#                     "magnitud": tipo["nombre"],
#                     "unidad_medicion": tipo["unidadMedida"],
#                 }
#             )

#         return {
#             "instrumentos": list(instrumentos.values()),
#             "mediciones": resultado,
#         }

    
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

    def obtener_instrumentos(self) -> list[dict]:

        respuesta = self._session.get(
            f"{BACKEND_URL}/Instrumento",
            timeout=30
        )

        respuesta.raise_for_status()

        return respuesta.json()

    def obtener_mediciones(self) -> list[dict]:

        respuesta = self._session.get(
            f"{BACKEND_URL}/Medicion",
            timeout=30
        )

        respuesta.raise_for_status()

        return respuesta.json()


class Generador:

    def __init__(self, jwt: str):

        self.backend = BackendClient(jwt)

    def generar(self) -> dict:

        instrumentos = {
            instrumento["id"]: instrumento
            for instrumento in self.backend.obtener_instrumentos()
        }

        mediciones = self.backend.obtener_mediciones()

        resultado = []

        for medicion in mediciones:

            instrumento_id = medicion["instrumentoId"]

            instrumento = instrumentos.get(instrumento_id)

            if instrumento is None:
                print(
                    f"Instrumento {instrumento_id} no encontrado."
                )
                continue

            referencia = (
                instrumento["referencia"]
                .strip()
                .lower()
            )

            if referencia.startswith("actuador"):
                continue

            tipo = instrumento["tipoInstrumento"]

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
            "instrumentos": list(instrumentos.values()),
            "mediciones": resultado,
        }

