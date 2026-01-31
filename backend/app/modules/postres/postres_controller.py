from .postres_model import PostresModel


class PostresController:

    @staticmethod
    def get_all():
        postres = PostresModel.getall()
        return postres

    @staticmethod
    def get_one(id):
        postre = PostresModel.get_by_id(id=id)
        return postre

    @staticmethod
    def create(data: dict):
        postres = PostresModel(nombre=data['nombre'], descripcion=data['descripcion'],
                               categoria_id=data['categoria_id'], precio=data['precio'], img=data['img'])
        return postres.create()

    @staticmethod
    def update(data: dict):
        postres = PostresModel(
            id=data['id'], nombre=data['nombre'], descripcion=data['descripcion'],
            categoria_id=data['categoria_id'], precio=data['precio'], img=data['img'])
        return postres.update()

    @staticmethod
    def eliminar(id):
        resultado = PostresModel.eliminar(id)
        return resultado
