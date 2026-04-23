from flask import Flask, jsonify

app = Flask(__name__)

# Base de datos simulada
ADEUDOS = {
    "2020001": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020002": {"adeudo": True, "detalle": "Derechos informaticos"},
    "2020003": {"adeudo": True, "detalle": "Sistema Operativos"},
    "2020004": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020005": {"adeudo": True, "detalle": "Libro java para programadores"
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