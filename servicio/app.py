# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware

# # from autenticacionConexion.login import Login
# from main import ejecutar_modelo


# app = FastAPI()
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:4200"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # JWT almacenado en memoria mientras la API esté ejecutándose
# jwt_actual = None


# class LoginRequest(BaseModel):
#     email: str
#     password: str


# @app.post("/login")
# def login(datos: LoginRequest):

#     global jwt_actual

#     try:

#         autenticacion = Login()

#         jwt_actual = autenticacion.iniciar_sesion(
#             datos.email,
#             datos.password
#         )

#         return {
#             "autenticado": True,
#             "mensaje": "Inicio de sesión exitoso"
#         }

#     except Exception as e:

#         jwt_actual = None

#         raise HTTPException(
#             status_code=401,
#             detail=str(e)
#         )


# @app.post("/ejecutar")
# def ejecutar():

#     global jwt_actual

#     if jwt_actual is None:

#         raise HTTPException(
#             status_code=401,
#             detail="Debe iniciar sesión primero."
#         )

#     try:

#         resultado = ejecutar_modelo(jwt_actual)

#         return resultado

#     except Exception as e:

#         raise HTTPException(
#             status_code=500,
#             detail=str(e)
#         )


# @app.post("/logout")
# def logout():

#     global jwt_actual

#     jwt_actual = None

#     return {
#         "autenticado": False,
#         "mensaje": "Sesión finalizada."
#     }



from fastapi import FastAPI, Header, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from main import ejecutar_modelo


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/ejecutar")
def ejecutar(
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

        return ejecutar_modelo(jwt)

    except Exception as error:

        raise HTTPException(
            status_code=500,
            detail=str(error)
        )

