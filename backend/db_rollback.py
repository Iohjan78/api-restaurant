import psycopg2
from psycopg2 import sql, errors
import os
from dotenv import load_dotenv

load_dotenv()

DB_CONFIG = {
    'host': os.getenv("DB_HOST", "db"),
    'port': int(os.getenv("DB_PORT", 5432)),
    'user': os.getenv("DB_USER", "tpfinal"),
    'password': os.getenv("DB_PASSWORD", "tpfinalpass"),
    'database': os.getenv("DB_NAME", "tpfinaldb")
}

# Orden importante: primero las que tienen FK, después las independientes
TABLES_TO_DROP = [
    'bebidas',      # Tiene FK a categorias
    'postres',      # Tiene FK a categorias
    'platos',       # Tiene FK a categorias
    'categorias'    # No tiene FK, va última
]


def drop_tables(conn, tables):
    """Elimina todas las tablas en orden"""
    cursor = conn.cursor()
    
    for table_name in tables:
        try:
            print(f"Dropping table {table_name}: ", end="")
            cursor.execute(f"DROP TABLE IF EXISTS {table_name} CASCADE")
            print("OK")
        except Exception as err:
            print(f"Error: {err}")
    
    cursor.close()


if __name__ == "__main__":
    try:
        # Conectar a PostgreSQL
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = True
        
        print("🗑️  Conectado a PostgreSQL - Iniciando rollback...\n")
        
        # Confirmar antes de borrar
        confirm = input("⚠️  ¿Estás seguro que querés borrar TODAS las tablas? (si/no): ")
        
        if confirm.lower() in ['si', 's', 'yes', 'y']:
            drop_tables(conn, TABLES_TO_DROP)
            print("\n✅ Rollback completado - Todas las tablas eliminadas")
        else:
            print("\n❌ Rollback cancelado")
        
        conn.close()
        
    except Exception as e:
        print(f"❌ Error: {e}")