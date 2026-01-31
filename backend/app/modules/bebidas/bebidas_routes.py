from .bebidas_controller import BebidasController
from flask import jsonify, request, Blueprint  # type: ignore

bebidas_bp = Blueprint("bebidas", __name__)


@bebidas_bp.route("/bebidas")
def get_all():
    try:
        bebidas = BebidasController.get_all()
        if bebidas:
            return jsonify(bebidas), 200
        else:
            return jsonify({"mensaje": "no se encontraron bebidas"}), 404
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@bebidas_bp.route("/bebidas/<int:id>")
def get_one(id):
    try:
        bebida = BebidasController.get_one(id)
        if bebida:
            return jsonify(bebida), 200
        else:
            return jsonify({"mensaje": "no se encontro la bebida"}), 404
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@bebidas_bp.route("/bebidas", methods=["POST"])
def create():
    try:
        data = request.get_json()

        # validar que llegó data
        if not data:
            return jsonify({"mensaje": "No se recibieron datos"}), 400

        # validar nombre
        if 'nombre' in data:
            nombre = data['nombre']

            if not nombre or not nombre.strip():
                return jsonify({"mensaje": "El nombre es obligatorio"}), 400

            if len(nombre.strip()) < 3:
                return jsonify({"mensaje": "El nombre debe tener al menos 3 caracteres"}), 400

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

        bebidas = BebidasController.create(data)
        if bebidas:
            return jsonify({'mensaje': 'bebida creada correctamente'}), 201
        else:
            return jsonify({"mensaje": "error al crear el bebida"}), 400
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@bebidas_bp.route("/bebidas/<int:id>", methods=["PUT"])
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

            if not nombre or not nombre.strip():
                return jsonify({"mensaje": "El nombre es obligatorio"}), 400

            if len(nombre.strip()) < 3:
                return jsonify({"mensaje": "El nombre debe tener al menos 3 caracteres"}), 400

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

        bebidas = BebidasController.update(data)
        if bebidas:
            return jsonify({'mensaje': 'bebida editada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al editar la bebida"}), 400
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@bebidas_bp.route("/bebidas/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        bebidas = BebidasController.eliminar(id)
        if bebidas:
            return jsonify({'mensaje': 'bebida eliminada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al eliminar el bebida"}), 500
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500
