from .bebidas_model import BebidasModel


class BebidasController:

    @staticmethod
    def get_all():
        bebidas = BebidasModel.getall()
        return bebidas

    @staticmethod
    def get_one(id):
        bebidas = BebidasModel.get_by_id(id=id)
        return bebidas

    @staticmethod
    def create(data: dict):
        bebidas = BebidasModel(
            nombre=data['nombre'], categoria_id=data['categoria_id'], precio=data['precio'], img=data['img'])
        return bebidas.create()

    @staticmethod
    def update(data: dict):
        bebidas = BebidasModel(
            id=data['id'], nombre=data['nombre'], categoria_id=data['categoria_id'], precio=data['precio'], img=data['img'])
        return bebidas.update()

    @staticmethod
    def eliminar(id):
        resultado = BebidasModel.eliminar(id)
        return resultado
