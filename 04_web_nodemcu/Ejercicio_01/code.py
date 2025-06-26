import datetime
from flask import Flask, request, jsonify, make_response
from functools import wraps

app = Flask(__name__)

USERS = {
    "usuario": "contraseña_segura"
}

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not auth.username or not auth.password or \
           auth.username not in USERS or USERS[auth.username] != auth.password:
            return make_response('Credenciales requeridas. Acceso denegado.', 401, {'WWW-Authenticate': 'Basic realm="Login Requerido"'})
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def home():
    """
    Endpoint raíz.
    Devuelve un mensaje de bienvenida y código de estado 200 OK.
    """
    return make_response("Web dummy para pruebas - Lenguajes Electrónicos", 200)

@app.route('/secret')
@auth_required
def secret():
    """
    Endpoint secreto.
    Requiere autenticación básica (usuario:contraseña_segura).
    Devuelve un mensaje secreto y código de estado 200 OK si las credenciales son correctas.
    """
    return make_response("Esto es un secreto", 200)

@app.route('/time')
def get_time():
    """
    Endpoint de tiempo.
    Devuelve la fecha y hora actuales y código de estado 200 OK.
    """
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return make_response(f"Fecha y hora actuales: {current_time}", 200)

@app.route('/error')
def simulate_error():
    """
    Endpoint de error.
    Devuelve un mensaje de error y código de estado 500 Internal Server Error.
    """
    return make_response("Error de servidor", 500)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
