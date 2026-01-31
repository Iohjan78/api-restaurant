from app.database.connect_db import connectDB
import psycopg2
from psycopg2.extras import RealDictCursor
import os


class CategoriaModel:

    def __init__(self, id: int = 0, nombre: str = "", tipo: str = ""):
        self.id = id
        self.nombre = nombre
        self.tipo = tipo

    def serializar(self) -> dict:
        return {
            "id": self.id,
            "nombre": self.nombre,
            "tipo": self.tipo
        }

    @staticmethod
    def deserializar(data: dict):
        return CategoriaModel(
            id=data.get("id", 0),
            nombre=data.get("nombre", ""),
            tipo=data.get("tipo", "")
        )

    @staticmethod
    def getall():
        cxn = connectDB.get_connect()
        if not cxn:
            return False

        try:
            from psycopg2.extras import RealDictCursor
            with cxn.cursor(cursor_factory=RealDictCursor) as cursor:
                cursor.execute("SELECT * FROM categorias")
                rows = cursor.fetchall()
                categorias = [dict(row) for row in rows] if rows else []
                return categorias if categorias else False

        except Exception as exc:

            print(f"Error al listar categorías: {exc}")
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
                cursor.execute("SELECT * FROM categorias WHERE id = %s", (id,))
                row = cursor.fetchone()
                return dict(row) if row else False

        except Exception as exc:
            print(f"Error al obtener categoría: {exc}")
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
                    "INSERT INTO categorias (nombre, tipo) VALUES (%s, %s) RETURNING id",
                    (self.nombre, self.tipo)
                )
                result = cursor.fetchone()
                if result:
                    self.id = result[0]

                cxn.commit()
                return True if result else False

        except Exception as exc:
            cxn.rollback()
            print(f"Error al crear categoría: {exc}")
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
                    "UPDATE categorias SET nombre = %s, tipo = %s WHERE id = %s",
                    (self.nombre, self.tipo, self.id)
                )

                result = cursor.rowcount
                cxn.commit()
                return True if result > 0 else False

        except Exception as exc:
            cxn.rollback()
            print(f"Error al actualizar categoría: {exc}")
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
                cursor.execute("DELETE FROM categorias WHERE id = %s", (id,))
                result = cursor.rowcount
                cxn.commit()
                return True if result > 0 else False

        except Exception as exc:
            cxn.rollback()
            print(f"Error al eliminar categoría: {exc}")
            return False
        finally:
            cxn.close()
