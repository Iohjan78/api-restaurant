import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()


class connectDB:

    @staticmethod
    def get_connect():
        try:
            database_url = os.getenv("DATABASE_URL")

            if database_url:
                # Railway proporciona DATABASE_URL
                url = urlparse(database_url)
                cxn = psycopg2.connect(
                    user=url.username,
                    password=url.password,
                    database=url.path[1:],
                    host=url.hostname,
                    port=url.port
                )
            else:
                # Desarrollo local con variables separadas
                cxn = psycopg2.connect(
                    user=os.getenv("POSTGRES_USER"),
                    password=os.getenv("POSTGRES_PASSWORD"),
                    database=os.getenv("POSTGRES_DB"),
                    host=os.getenv("DB_HOST", "db"),
                    port=int(os.getenv("DB_PORT", 5432))
                )
            return cxn
        except Exception as ex:
            print(f"Error al conectar: {ex}")
            return None
