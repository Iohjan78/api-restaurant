compose con la creacion, actualizacion de paquetes y levantamiento de proyecto automatico

services:
  vue-app:
    build: .
    container_name: vue-dev
    ports:
      - "3000:3000"
    volumes:
      - .:/app
    working_dir: /app
    command: sh -c "
      if [ ! -f ./vue/package.json ]; then
        echo '🟢 Creando proyecto Vue (vue)...';
        npm create vue@latest vue -- --default;
        cd vue;
        npm install;
      else
        cd vue;
      fi &&
      echo '🚀 Iniciando servidor de desarrollo...' &&
      npm run dev -- --host 0.0.0.0 --port 3000
      "

# backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# frontend
npm install