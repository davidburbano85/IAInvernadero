from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from main import ejecutar_modelo


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SolicitudInteligencia(BaseModel):
    invernaderoId: int


@app.post("/ejecutar")
def ejecutar(
    solicitud: SolicitudInteligencia,
    authorization: str | None = Header(default=None)
):

    if not authorization:
        raise HTTPException(
            status_code=401,
            detail="Token de autenticación requerido."
        )

    if not authorization.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Formato de autenticación inválido."
        )

    jwt = authorization.removeprefix("Bearer ").strip()

    if not jwt:
        raise HTTPException(
            status_code=401,
            detail="Token de autenticación vacío."
        )

    try:

        return ejecutar_modelo(
            jwt,
            solicitud.invernaderoId
        )

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )