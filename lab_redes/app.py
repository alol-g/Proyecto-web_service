from flask import Flask, jsonify

app = Flask(__name__)

# Base de datos simulada (Laboratorio de Redes)
ADEUDOS = {
    "2020001": {"adeudo": True, "detalle": "Cable de red no devuelto"},
    "2020002": {"adeudo": False, "detalle": "Equipo entregado correctamente"},
    "2020003": {"adeudo": True, "detalle": "Router asignado pendiente de entrega"},
    "2020004": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020005": {"adeudo": True, "detalle": "Daño en switch del laboratorio"}
}

@app.route('/check/<matricula>', methods=['GET'])
def consultar(matricula):
    res = ADEUDOS.get(matricula, {
        "adeudo": False,
        "detalle": "Sin adeudos en laboratorio de redes"
    })

    return jsonify({
        "departamento": "Lab. Redes",
        "adeudo": res["adeudo"],
        "mensaje": res["detalle"]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)