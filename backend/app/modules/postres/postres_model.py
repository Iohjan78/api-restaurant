from app.database.connect_db import connectDB
import psycopg2
from psycopg2.extras import RealDictCursor
import os


class PostresModel:

    def __init__(self, id: int = 0, nombre: str = "", descripcion: str = "", categoria_id: int = 0, precio: float = 0.0, img: str = ""):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.categoria_id = categoria_id
        self.precio = precio
        self.img = img

    def serializar(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "descripcion": self.descripcion,
            "categoria_id": self.categoria_id,
            "precio": self.precio,
            "img": self.img
        }

    @staticmethod
    def deserializar(data: dict):
        return PostresModel(
            id=data.get("id", 0),
            nombre=data.get("nombre", ""),
            descripcion=data.get("descripcion", ""),
            categoria_id=data.get("categoria_id", 0),
            precio=data.get("precio", 0.0),
            img=data.get("img", "")
        )

    @staticmethod
    def getall():
        cxn = connectDB.get_connect()
        if not cxn:
            print("❌ No se pudo conectar")
            return False

        try:
            from psycopg2.extras import RealDictCursor
            with cxn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("""
                    SELECT 
                        p.id,
                        p.nombre,
                        p.descripcion,
                        p.precio,
                        p.categoria_id,
                        c.nombre AS categoria_nombre,
                        c.tipo AS categoria_tipo
                    FROM postres p
                    INNER JOIN categorias c ON p.categoria_id = c.id
                """)
                rows = cursor.fetchall()

                postres = [dict(row) for row in rows] if rows else []
                return postres if postres else False

        except Exception as exc:
            print(f"❌ Error al listar postres: {exc}")
            import traceback
            traceback.print_exc()
            return False
        finally:
            cxn.close()

    @staticmethod
    def get_by_id(id: int):
        cxn = connectDB.get_connect()
        if not cxn:
            return False

        try:
            from psycopg2.extras import RealDictCursor
            with cxn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute(
                    """
                SELECT 
                    p.id,
                    p.nombre,
                    p.descripcion,
                    p.precio,
                    p.img,
                    p.categoria_id,
                    c.nombre AS categoria_nombre,
                    c.tipo AS categoria_tipo
                FROM postres p
                INNER JOIN categorias c ON p.categoria_id = c.id
                WHERE p.id = %s
            """, (id,))
                row = cursor.fetchone()
                return dict(row) if row else False

        except Exception as exc:
            print(f"Error al obtener el postre: {exc}")
            return False
        finally:
            cxn.close()

    def create(self):
        print("🌐 MODEL: Creando nuevo postre en la BD...")
        cxn = connectDB.get_connect()
        if not cxn:
            return False

        try:
            with cxn.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO postres (
                    nombre, 
                    descripcion, 
                    categoria_id, 
                    precio, 
                    img) 
                    VALUES (%s,%s,%s,%s,%s) RETURNING id""",
                    (self.nombre, self.descripcion,
                     self.categoria_id, self.precio, self.img)
                )

                result = cursor.fetchone()
                if result:
                    self.id = result[0]

                cxn.commit()
                return True if result else False

        except Exception as exc:
            cxn.rollback()
            print(f"Error al crear el postre: {exc}")
            return False
        finally:
            cxn.close()

    def update(self):
        cxn = connectDB.get_connect()
        if not cxn:
            return False

        try:
            with cxn.cursor() as cursor:
                cursor.execute(
                    """UPDATE postres SET 
                    nombre = %s, 
                    descripcion = %s, 
                    categoria_id =%s, 
                    precio= %s,
                    img= %s 
                    WHERE id = %s""",
                    (self.nombre, self.descripcion, self.categoria_id,
                     self.precio, self.img, self.id)
                )

                result = cursor.rowcount
                cxn.commit()
                return True if result > 0 else False

        except Exception as exc:
            cxn.rollback()
            print(f"Error al actualizar el postre: {exc}")
            return False
        finally:
            cxn.close()

    @staticmethod
    def eliminar(id: int):
        cxn = connectDB.get_connect()
        if not cxn:
            return False

        try:
            with cxn.cursor() as cursor:
                cursor.execute("DELETE FROM postres WHERE id = %s", (id,))
                result = cursor.rowcount
                cxn.commit()
                return True if result > 0 else False

        except Exception as exc:
            cxn.rollback()
            print(f"Error al eliminar el postre: {exc}")
            return False
        finally:
            cxn.close()
