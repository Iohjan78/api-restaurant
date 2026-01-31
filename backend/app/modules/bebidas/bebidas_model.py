from app.database.connect_db import connectDB
import psycopg2
from psycopg2.extras import RealDictCursor
import os


class BebidasModel:

    def __init__(self, id: int = 0, nombre: str = "", categoria_id: int = 0, precio: float = 0.0, img: str = ""):
        self.id = id
        self.nombre = nombre
        self.categoria_id = categoria_id
        self.precio = precio
        self.img = img

    def serializar(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria_id": self.categoria_id,
            "precio": self.precio,
            "img": self.img
        }

    @staticmethod
    def deserializar(data: dict):
        return BebidasModel(
            id=data.get("id", 0),
            nombre=data.get("nombre", ""),
            categoria_id=data.get("categoria_id", 0),
            precio=data.get("precio", 0.0),
            img=data.get("img", "")
        )

    @staticmethod
    def getall():
        cxn = connectDB.get_connect()
        if not cxn:
            return False

        try:
            from psycopg2.extras import RealDictCursor
            with cxn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("""
                    SELECT 
                        p.id,
                        p.nombre,
                        p.precio,
                        p.categoria_id,
                        c.nombre AS categoria_nombre,
                        c.tipo AS categoria_tipo
                    FROM bebidas p
                    INNER JOIN categorias c ON p.categoria_id = c.id
                """)
                rows = cursor.fetchall()

                bebidas = [dict(row) for row in rows] if rows else []
                return bebidas if bebidas else False

        except Exception as exc:
            print(f"❌ Error al listar bebidas: {exc}")
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
                    p.precio,
                    p.img,
                    p.categoria_id,
                    c.nombre AS categoria_nombre,
                    c.tipo AS categoria_tipo
                FROM bebidas p
                INNER JOIN categorias c ON p.categoria_id = c.id
                WHERE p.id = %s
            """, (id,))
                row = cursor.fetchone()
                return dict(row) if row else False

        except Exception as exc:
            print(f"Error al obtener el bebida: {exc}")
            return False
        finally:
            cxn.close()

    def create(self):
        cxn = connectDB.get_connect()
        if not cxn:
            return False

        try:
            with cxn.cursor() as cursor:
                cursor.execute(
                    """INSERT INTO bebidas (
                    nombre, 
                    categoria_id, 
                    precio, 
                    img) 
                    VALUES (%s,%s,%s,%s) RETURNING id""",
                    (self.nombre,
                     self.categoria_id, self.precio, self.img)
                )
                result = cursor.fetchone()
                if result:
                    self.id = result[0]

                cxn.commit()
                return True if result else False

        except Exception as exc:
            cxn.rollback()
            print(f"Error al crear el bebida: {exc}")
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
                    """UPDATE bebidas SET 
                    nombre = %s, 
                    categoria_id =%s, 
                    precio= %s,
                    img= %s 
                    WHERE id = %s""",
                    (self.nombre, self.categoria_id,
                     self.precio, self.img, self.id)
                )

                result = cursor.rowcount
                cxn.commit()
                return True if result > 0 else False

        except Exception as exc:
            cxn.rollback()
            print(f"Error al actualizar la bebida: {exc}")
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
                cursor.execute("DELETE FROM bebidas WHERE id = %s", (id,))
                result = cursor.rowcount
                cxn.commit()
                return True if result > 0 else False

        except Exception as exc:
            cxn.rollback()
            print(f"Error al eliminar la bebida: {exc}")
            return False
        finally:
            cxn.close()
