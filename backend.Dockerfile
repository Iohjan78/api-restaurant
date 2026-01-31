FROM python:3.11-alpine

WORKDIR /app

# Instalar dependencias del sistema si son necesarias
RUN apk add --no-cache gcc musl-dev linux-headers

# Copiar solo requirements para aprovechar cache
COPY backend/requirements.txt .

# Instalar dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000