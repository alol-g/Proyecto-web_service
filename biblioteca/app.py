from flask import Flask, jsonify

app = Flask(__name__)

# Base de datos simulada
ADEUDOS = {
    "2020001": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020002": {"adeudo": False, "detalle": "Derechos informaticos"},
    "2020003": {"adeudo": True, "detalle": "Libro Sistemas"
    "Distribuidos' pendiente"}
}
@app.route('/check/<matricula>', methods=['GET'])

def consultar(matricula):
    res = ADEUDOS.get(matricula, {"adeudo": False, "detalle": "Limpio"
        })
    return jsonify({
        "departamento": "Biblioteca",
        "adeudo": res["adeudo"],
        "mensaje": res["detalle"]
    })
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)