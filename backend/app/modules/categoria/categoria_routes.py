from .categoria_controller import CategoriaController
from flask import jsonify, request, Blueprint

categoria_bp = Blueprint("categoria", __name__)


@categoria_bp.route("/categorias")
def get_all():
    try:
        categorias = CategoriaController.get_all()
        if categorias:
            return jsonify(categorias), 200
        else:
            return jsonify({"mensaje": "no se encontraron categorias"}), 404
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@categoria_bp.route("/categorias/<int:id>")
def get_one(id):
    try:
        categoria = CategoriaController.get_one(id)
        if categoria:
            return jsonify(categoria), 200
        else:
            return jsonify({"mensaje": "no se encontro la categoria"}), 404
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@categoria_bp.route("/categorias", methods=["POST"])
def create():
    try:
        data = request.get_json()
        # validar que llegó data
        if not data:
            return jsonify({"mensaje": "No se recibieron datos"}), 400

        # validar nombre
        if 'nombre' in data:
            nombre = data['nombre']

        # Validar que no sea None, vacío o solo espacios
            if not nombre or not nombre.strip():
                return jsonify({"mensaje": "El nombre es obligatorio"}), 400

        # Validar longitud mínima
            if len(nombre.strip()) < 3:
                return jsonify({"mensaje": "El nombre debe tener al menos 3 caracteres"}), 400

        # validar tipo
        if not data.get('tipo'):
            return jsonify({"mensaje": "El tipo es obligatorio"}), 400

        tipo_valido = ['plato', 'postre', 'bebida']
        if data.get('tipo') not in tipo_valido:
            return jsonify({"mensaje": f"El tipo debe ser: {', '.join(tipo_valido)}"}), 400

        categoria = CategoriaController.create(data)

        if categoria:
            return jsonify({
                'mensaje': 'Categoría creada correctamente',
                'data': categoria
            }), 201
        else:
            return jsonify({"mensaje": "Error al crear categoría"}), 400

    except Exception as e:
        return jsonify({"mensaje": f"Error: {str(e)}"}), 500


@categoria_bp.route("/categorias/<int:id>", methods=["PUT"])
def update(id):
    try:
        data = request.get_json()
        data['id'] = id

        # validar que llegó data
        if not data:
            return jsonify({"mensaje": "No se recibieron datos"}), 400

        # validar nombre
        if 'nombre' in data:
            nombre = data['nombre']

        # Validar que no sea None, vacío o solo espacios
            if not nombre or not nombre.strip():
                return jsonify({"mensaje": "El nombre es obligatorio"}), 400

        # Validar longitud mínima
            if len(nombre.strip()) < 3:
                return jsonify({"mensaje": "El nombre debe tener al menos 3 caracteres"}), 400

        # validar tipo
        if not data.get('tipo'):
            return jsonify({"mensaje": "El tipo es obligatorio"}), 400

        categorias = CategoriaController.update(data)
        if categorias:
            return jsonify({'mensaje': 'categoria editada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al editar la categoria"}), 400
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@categoria_bp.route("/categorias/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        categorias = CategoriaController.eliminar(id)
        if categorias:
            return jsonify({'mensaje': 'categoria eliminada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al eliminar la categorias"}), 500
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500
