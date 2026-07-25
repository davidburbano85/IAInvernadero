from getpass import getpass

from supabase import create_client


SUPABASE_URL = "https://rritlxjwzrjqbmpfurbt.supabase.co"
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InJyaXRseGp3enJqcWJtcGZ1cmJ0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODQxNDI2MzQsImV4cCI6MjA5OTcxODYzNH0.1pbkRBSxvZyDMlvlGR9XhAZPZFdejdyjOpRXwASjBA8"


class Login:

    def __init__(self):
        self._cliente = create_client(
            SUPABASE_URL,
            SUPABASE_ANON_KEY
        )

    def iniciar_sesion(self, email: str, password: str) -> str:

        respuesta = self._cliente.auth.sign_in_with_password(
            {
                "email": email,
                "password": password
            }
        )

        return respuesta.session.access_token



    def iniciar_sesion_consola(self) -> str:

        email = input("Correo: ").strip()
        password = getpass("Contraseña: ")

        return self.iniciar_sesion(email, password)