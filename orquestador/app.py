import requests
from flask import Flask, jsonify

app = Flask(__name__)

# --- CONFIGURACIÓN DE LA RED LAN ---
# IMPORTANTE: En el laboratorio, cambia las 'XX' por las IPs 
# reales de las computadoras de tus compañeros.
NODOS = {
    "biblioteca": "http://192.168.1.XX:5001",
    "escolares": "http://192.168.1.YY:5002",
    "lab_redes": "http://192.168.1.ZZ:5003",
    "lab_electronica": "http://192.168.1.WW:5004"
}

@app.route('/constancia/<matricula>', methods=['GET'])
def orquestar(matricula):
    reporte = []
    aprobado = True

    # Consultar cada nodo periférico
    for dep, url in NODOS.items():
        try:
            # Se realiza la petición GET al microservicio
            # Usamos un timeout de 2 segundos para no bloquearnos 
            respuesta = requests.get(f"{url}/check/{matricula}", timeout=2)
            data = respuesta.json()
            reporte.append(data) 
            
            # Si algún departamento reporta adeudo, no se puede aprobar 
            if data.get("adeudo"):
                aprobado = False
        except Exception as e:
            # Si el nodo no responde o está apagado 
            reporte.append({
                "departamento": dep, 
                "error": "Nodo fuera de línea (Offline)",
                "detalle": str(e)
            })
            aprobado = False

    # Veredicto final del sistema 
    resultado = "LISTO" if aprobado else "RECHAZADO"
    
    return jsonify({
        "estatus": resultado,
        "matricula_consultada": matricula,
        "detalles": reporte
    })

if __name__ == '__main__':
    # host='0.0.0.0' permite que otros te vean en la LAN 
    # port=8000 es el puerto asignado al Orquestador 
    app.run(host='0.0.0.0', port=8000, debug=True)