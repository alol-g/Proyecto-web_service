from flask import Flask, jsonify

app = Flask(__name__)

# Base de datos simulada - Lab de Electrónica
ADEUDOS = {
    "2020001": {"adeudo": False, "detalle": "Sin pendientes"},
    "2020002": {"adeudo": True,  "detalle": "Kit de componentes SMD pendiente de devolución"},
    "2020003": {"adeudo": True,  "detalle": "Osciloscopio prestado sin devolver"},
    "2020004": {"adeudo": False, "detalle": "Limpio"},
    "2020005": {"adeudo": True,  "detalle": "Fuente de poder dañada sin reporte"},
}

@app.route('/check/<matricula>', methods=['GET'])
def consultar(matricula):
    res = ADEUDOS.get(matricula, {"adeudo": False, "detalle": "Sin registro - Limpio"})
    return jsonify({
        "departamento": "Lab. Electronica",
        "adeudo": res["adeudo"],
        "mensaje": res["detalle"]
    })

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "online", "departamento": "Lab. Electronica"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)