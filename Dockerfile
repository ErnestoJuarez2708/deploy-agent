FROM python:3.11-slim

# Evita archivos .pyc y buffer de logs
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos dependencias
COPY requirements.txt .

# Instalamos dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el backend y templates
COPY backend ./backend
COPY templates ./templates

# Exponemos el puerto de Flask
EXPOSE 5000

# Comando de arranque
CMD ["python", "backend/app.py"]