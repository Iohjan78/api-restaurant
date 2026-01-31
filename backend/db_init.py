import psycopg2
from psycopg2 import sql, errors
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()

database_url = os.getenv("DATABASE_URL")

if database_url:
    # Railway
    url = urlparse(database_url)
    DB_CONFIG = {
        'host': url.hostname,
        'port': url.port,
        'user': url.username,
        'password': url.password,
        'database': url.path[1:]
    }
else:
    # Local
    DB_CONFIG = {
        'host': os.getenv("DB_HOST", "db"),
        'port': int(os.getenv("DB_PORT", 5432)),
        'user': os.getenv("POSTGRES_USER", "user"),
        'password': os.getenv("POSTGRES_PASSWORD", "password"),
        'database': os.getenv("POSTGRES_DB", "mydatabase")
    } 

TABLES = {}
SEEDS = {}


TABLES['CATEGORIAS'] = """
    CREATE TABLE IF NOT EXISTS categorias (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        tipo VARCHAR(20) NOT NULL CHECK (tipo IN ('plato', 'postre', 'bebida'))
    )
"""


TABLES['PLATOS'] = """
    CREATE TABLE IF NOT EXISTS platos (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        descripcion TEXT,
        categoria_id INTEGER NOT NULL REFERENCES categorias(id) ON DELETE CASCADE,
        precio DECIMAL(10,2) NOT NULL,
        img VARCHAR(255)
    )
"""


TABLES['POSTRES'] = """
    CREATE TABLE IF NOT EXISTS postres (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        descripcion TEXT,
        categoria_id INTEGER NOT NULL REFERENCES categorias(id) ON DELETE CASCADE,
        precio DECIMAL(10,2) NOT NULL,
        img VARCHAR(255)
    )
"""


TABLES['BEBIDAS'] = """
    CREATE TABLE IF NOT EXISTS bebidas (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        categoria_id INTEGER NOT NULL REFERENCES categorias(id) ON DELETE CASCADE,
        precio DECIMAL(10,2) NOT NULL,
        img VARCHAR(255)
    )
"""


SEEDS['CATEGORIAS'] = (
    "INSERT INTO categorias (nombre, tipo) VALUES (%s, %s) ON CONFLICT DO NOTHING",
    [
        ('Carnes', 'plato'),
        ('Pastas', 'plato'),
        ('Pescados', 'plato'),
        ('Vegetarianos', 'plato'),
        ('Helados', 'postre'),
        ('Tortas', 'postre'),
        ('Tartas', 'postre'),
        ('Con alcohol', 'bebida'),
        ('Sin alcohol', 'bebida'),
        ('con gas', 'bebida'),
        ('sin gas', 'bebida')
    ]
)


SEEDS['PLATOS'] = (
    "INSERT INTO platos (nombre, descripcion, precio, categoria_id) VALUES (%s, %s, %s, %s)",
    [
        ('Bife de Chorizo', 'Bife de 400g con guarnición a elección', 4500.00, 1),
        ('Milanesa Napolitana', 'Con jamón, tomate y queso', 3200.00, 1),
        ('Asado de Tira', 'Costillar asado a la parrilla', 4000.00, 1),
        ('Ravioles de Ricota', 'Pasta casera con salsa a elección', 2800.00, 2),
        ('Sorrentinos', 'Rellenos de jamón y queso', 3000.00, 2),
        ('Ñoquis', 'Con salsa bolognesa', 2500.00, 2),
        ('Salmón Grillado', 'Con vegetales salteados', 5200.00, 3),
        ('Merluza al Limón', 'Con papas al horno', 3800.00, 3),
        ('Ensalada Completa', 'Mix de vegetales frescos', 2200.00, 4),
        ('Hamburguesa Vegana', 'Medallón de lentejas', 2600.00, 4)
    ]
)


SEEDS['POSTRES'] = (
    "INSERT INTO postres (nombre, descripcion, precio, categoria_id) VALUES (%s, %s, %s, %s)",
    [
        ('Helado de Chocolate', '2 bochas de helado artesanal', 1200.00, 5),
        ('Helado de Frutilla', '2 bochas con crema', 1200.00, 5),
        ('Copa Helada', '3 bochas con salsa y crema', 1800.00, 5),
        ('Tiramisu', 'Postre italiano tradicional', 1500.00, 6),
        ('Cheesecake', 'Con frutos rojos', 1600.00, 6),
        ('Brownie', 'Con helado de vainilla', 1400.00, 6),
        ('Tarta de Manzana', 'Con canela', 1300.00, 7),
        ('Lemon Pie', 'Con merengue italiano', 1400.00, 7)
    ]
)


SEEDS['BEBIDAS'] = (
    "INSERT INTO bebidas (nombre, categoria_id, precio) VALUES (%s, %s, %s)",
    [
        ('Vino Tinto', 8, 1200.00),
        ('Cerveza Artesanal', 8, 1500.00),
        ('Fernet con Cola', 8, 1400.00),
        ('Coca Cola', 9, 600.00),
        ('Agua Mineral', 9, 500.00),
        ('Jugo Natural de Naranja', 9, 800.00),
        ('Limonada', 9, 700.00),
    ]
)


def create_tables(conn, tables):
    """Crea todas las tablas"""
    cursor = conn.cursor()
    for table_name, table_sql in tables.items():
        try:
            print(f"Creating table {table_name}: ", end="")
            cursor.execute(table_sql)
            print("OK")
        except errors.DuplicateTable:
            print("already exists.")
        except Exception as err:
            print(f"Error: {err}")
    cursor.close()


def seed_tables(conn, seeds):
    """Inserta datos iniciales"""
    cursor = conn.cursor()
    for table_name, (sql_query, data) in seeds.items():
        try:
            print(f"Seeding table {table_name}: ", end="")
            cursor.executemany(sql_query, data)
            print("OK")
        except Exception as err:
            print(f"Error: {err}")
    cursor.close()


if __name__ == "__main__":
    try:
        #conectar a postgres
        conn = psycopg2.connect(**DB_CONFIG)
        conn.autocommit = True
        
        print("Conectado a PostgreSQL")
        
        #crear tablas
        create_tables(conn, TABLES)
        
        #insertar datos
        seed_tables(conn, SEEDS)
        
        conn.commit()
        conn.close()
        
        print("\n✅ Base de datos inicializada correctamente!")
        
    except Exception as e:
        print(f"❌ Error: {e}")