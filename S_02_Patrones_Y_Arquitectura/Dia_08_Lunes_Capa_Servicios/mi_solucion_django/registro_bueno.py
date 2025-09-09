class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        print(f"MODELO: Usuario {email} creado en memoria.")


def send_welcome_email(email):
    # Logica de envio email
    print(f"Email: Enviando bienvenida a {email}.")

class UserService:

    def register_user(self, data: dict):
        email = data.get("email")
        pwd = data.get("password")
        if not email or not pwd or "@" not in email:
            return {"error": "Datos inválidos.", "status_code": 400}

        try:
            user = User(email, pwd)
        except Exception as e:
            return {"error": f"Error de base de datos: {e}", "status_code": 500}

        send_welcome_email(user.email)

        return {"message": "Usuario registrado con éxito.", "status_code": 201}


def register_user_view(data: dict):
    user_service = UserService()
    return user_service.register_user(data)

# Pruebas
if __name__ == "__main__":
    request_data = {"email": "test@example.com", "password": "password123"}
    response = register_user_view(request_data)
    print(f"RESPUESTA: {response}")