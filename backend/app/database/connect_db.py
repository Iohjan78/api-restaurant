import psycopg
import os
from dotenv import load_dotenv

load_dotenv()


class connectDB:

    @staticmethod
    def get_connect():
        try:
            database_url = os.getenv("DATABASE_URL")

            if database_url:
                # Railway
                cxn = psycopg.connect(database_url)
            else:
                # Local
                cxn = psycopg.connect(
                    user=os.getenv("POSTGRES_USER"),
                    password=os.getenv("POSTGRES_PASSWORD"),
                    dbname=os.getenv("POSTGRES_DB"),
                    host=os.getenv("DB_HOST", "db"),
                    port=int(os.getenv("DB_PORT", 5432))
                )
            return cxn
        except Exception as ex:
            print(f"Error al conectar: {ex}")
            return None
