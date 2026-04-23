from flask import Flask, jsonify

app = Flask(__name__)

# Tu "Base de Datos" de control escolar 
ADEUDOS = {
    "2020001": {"adeudo": False, "detalle": "Documentación completa"},
    "2020002": {"adeudo": True, "detalle": "Falta certificado de bachillerato"},
    "2020003": {"adeudo": False, "detalle": "Sin adeudos"}
}

# Endpoint que consultará el Orquestador 
@app.route('/check/<matricula>', methods=['GET'])
def consultar(matricula):
    # Si la matrícula no existe, asumimos que está "Limpio" 
    res = ADEUDOS.get(matricula, {"adeudo": False, "detalle": "No registrado / Sin adeudos"})
    
    return jsonify({
        "departamento": "Escolares",
        "adeudo": res["adeudo"],
        "mensaje": res["detalle"]
    })

if __name__ == '__main__':
    # Importante: host '0.0.0.0' para que sea visible en la red LAN 
    app.run(host='0.0.0.0', port=5002)