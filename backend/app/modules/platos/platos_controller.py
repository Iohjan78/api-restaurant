from .platos_model import PlatosModel


class PlatosController:

    @staticmethod
    def get_all():
        platos = PlatosModel.getall()
        print(f"entre en el controller")
        return platos

    @staticmethod
    def get_one(id):
        platos = PlatosModel.get_by_id(id=id)
        return platos

    @staticmethod
    def create(data: dict):
        platos = PlatosModel(nombre=data['nombre'], descripcion=data['descripcion'],
                             categoria_id=data['categoria_id'], precio=data['precio'], img=data['img'])
        return platos.create()

    @staticmethod
    def update(data: dict):
        platos = PlatosModel(
            id=data['id'], nombre=data['nombre'], descripcion=data['descripcion'],
            categoria_id=data['categoria_id'], precio=data['precio'], img=data['img'])
        return platos.update()

    @staticmethod
    def eliminar(id):
        resultado = PlatosModel.eliminar(id)
        return resultado
