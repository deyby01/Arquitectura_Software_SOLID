# codigo_ejemplo/registro_malo.py

# --- Simulación de Modelos y Emails ---
class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        print(f"MODELO: Usuario {email} creado en memoria.")

def send_welcome_email(email):
    print(f"EMAIL: Enviando bienvenida a {email}.")

# --- La Vista Gorda (Viola SRP) ---
def register_user_view(data: dict):
    """
    Esta función simula una vista de Django.
    Recibe datos de una petición y hace de todo.
    """
    print("VISTA: Petición de registro recibida.")
    
    # 1. Lógica de validación
    email = data.get("email")
    password = data.get("password")
    if not email or not password or "@" not in email:
        return {"error": "Datos inválidos.", "status_code": 400}
    
    # 2. Lógica de creación de usuario (hablar con el modelo)
    try:
        user = User(email, password)
    except Exception as e:
        return {"error": f"Error de base de datos: {e}", "status_code": 500}
    
    # 3. Lógica de notificación
    send_welcome_email(user.email)
    
    # 4. Lógica de respuesta HTTP
    print("VISTA: Proceso completado.")
    return {"message": "Usuario registrado con éxito.", "status_code": 201}

# --- Uso ---
request_data = {"email": "test@example.com", "password": "password123"}
response = register_user_view(request_data)
print(f"RESPUESTA: {response}")