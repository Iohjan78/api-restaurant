from .categoria_model import CategoriaModel


class CategoriaController:

    @staticmethod
    def get_all():
        categorias = CategoriaModel.getall()
        print(f"entre en el controller")
        return categorias

    @staticmethod
    def get_one(id):
        categoria = CategoriaModel.get_by_id(id=id)
        return categoria

    @staticmethod
    def create(data: dict):
        categoria = CategoriaModel(nombre=data['nombre'], tipo=data['tipo'])
        return categoria.create()

    @staticmethod
    def update(data: dict):
        categoria = CategoriaModel(
            id=data['id'], nombre=data['nombre'], tipo=data['tipo'])
        return categoria.update()

    @staticmethod
    def eliminar(id):
        resultado = CategoriaModel.eliminar(id)
        return resultado
