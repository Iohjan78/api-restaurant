from .platos_controller import PlatosController
from flask import jsonify, request, Blueprint

platos_bp = Blueprint("platos", __name__)


@platos_bp.route("/platos")
def get_all():
    try:
        platos = PlatosController.get_all()
        if platos:
            return jsonify(platos), 200
        else:
            return jsonify({"mensaje": "no se encontraron platos"}), 404
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@platos_bp.route("/platos/<int:id>")
def get_one(id):
    try:
        plato = PlatosController.get_one(id)
        if plato:
            return jsonify(plato), 200
        else:
            return jsonify({"mensaje": "no se encontro el plato"}), 404
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@platos_bp.route("/platos", methods=["POST"])
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
            if len(nombre.strip()) < 5:
                return jsonify({"mensaje": "El nombre debe tener al menos 5 caracteres"}), 400

        # validar precio
        if 'precio' in data:
            try:
                precio = float(data['precio'])
                if precio <= 0:
                    return jsonify({"mensaje": "El precio debe ser mayor a 0"}), 400
            except (ValueError, TypeError):
                return jsonify({"mensaje": "El precio debe ser un número válido"}), 400

        # validar categoria_id
        if not data.get('categoria_id'):
            return jsonify({"mensaje": "La categoria_id es obligatoria"}), 400

        # validar descripcion
        if not data.get('descripcion'):
            return jsonify({"mensaje": "La descripción es obligatoria"}), 400

        if len(data.get('descripcion')) < 5:
            return jsonify({"mensaje": "La descripción debe tener al menos 5 caracteres"}), 400

        platos = PlatosController.create(data)
        if platos:
            return jsonify({'mensaje': 'plato creada correctamente'}), 201
        else:
            return jsonify({"mensaje": "error al crear el plato"}), 400
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@platos_bp.route("/platos/<int:id>", methods=["PUT"])
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
            if len(nombre.strip()) < 5:
                return jsonify({"mensaje": "El nombre debe tener al menos 5 caracteres"}), 400

        # validar precio
        if 'precio' in data:
            try:
                precio = float(data['precio'])
                if precio <= 0:
                    return jsonify({"mensaje": "El precio debe ser mayor a 0"}), 400
            except (ValueError, TypeError):
                return jsonify({"mensaje": "El precio debe ser un número válido"}), 400

        # validar categoria_id
        if not data.get('categoria_id'):
            return jsonify({"mensaje": "La categoria_id es obligatoria"}), 400

        # validar descripcion
        if not data.get('descripcion'):
            return jsonify({"mensaje": "La descripción es obligatoria"}), 400

        if len(data.get('descripcion')) < 5:
            return jsonify({"mensaje": "La descripción debe tener al menos 5 caracteres"}), 400
        platos = PlatosController.update(data)
        if platos:
            return jsonify({'mensaje': 'plato editada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al editar la plato"}), 400
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@platos_bp.route("/platos/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        platos = PlatosController.eliminar(id)
        if platos:
            return jsonify({'mensaje': 'plato eliminada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al eliminar el plato"}), 500
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500
