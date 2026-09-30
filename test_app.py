from app import process_user_data

def test_process_user_data_minor():
    resultado = process_user_data("Juan", 17, "juan@email.com")
    assert resultado == "Error: El usuario es menor de edad"

def test_process_user_data_success():
    resultado = process_user_data("Maria", 25, "maria@email.com")
    assert resultado == "Éxito: Maria registrada correctamente"

def test_process_user_data_missing_email():
    resultado = process_user_data("Pedro", 30, "")
    assert resultado == "Error: Falta el correo electrónico"

def test_process_user_data_admin():
    resultado = process_user_data("admin", 22, "admin@empresa.com")
    assert resultado == "Error: No se puede registrar al administrador"