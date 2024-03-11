from flask import Flask, jsonify
from contractual.conf.errors import ApiError
from contractual.conf.db import init_db
from .contratos import ab

app = Flask(__name__)
app.secret_key = '1D7FC7F9-3B7E-4C40-AF4D-141ED3F6013A'
init_db()
app.register_blueprint(ab)


@app.errorhandler(ApiError)
def handle_exception(err):
    response = {
        "msg": err.description
    }
    return jsonify(response), err.code


def comenzar_consumidor():
    import threading
    import contractual.modulos.contratos.infraestructura.consumidores as contratos

    # Suscripción a eventos
    threading.Thread(target=contratos.suscribirse_a_eventos).start()
    threading.Thread(target=contratos.suscribirse_a_eventos,
                     args=[app]).start()

    # Suscripción a comandos
    threading.Thread(target=contratos.suscribirse_a_comandos, args=[app]).start()
    threading.Thread(target=contratos.suscribirse_a_compensacion, args=[app]).start()


comenzar_consumidor()
