# 1. Usa la imagen base ligera de Python 3.9 sugerida [cite: 64]
FROM python:3.9-slim

# 2. Define el directorio de trabajo dentro del contenedor [cite: 65]
WORKDIR /app

# 3. Instala las dependencias necesarias (flask para el API y requests para consultar nodos) [cite: 66]
RUN pip install flask requests

# 4. Copia el archivo app.py (y cualquier otro archivo de la carpeta) al contenedor [cite: 67]
COPY . .

# 5. Informa que el contenedor escuchará en el puerto 8000 (el del Orquestador) [cite: 61, 68]
EXPOSE 8000

# 6. Comando para ejecutar tu nodo principal al iniciar el contenedor [cite: 69]
CMD ["python", "app.py"]