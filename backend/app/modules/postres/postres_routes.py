from .postres_controller import PostresController
from flask import jsonify, request, Blueprint

postres_bp = Blueprint("postres", __name__)


@postres_bp.route("/postres")
def get_all():
    try:
        postres = PostresController.get_all()
        print(f"🌐 ROUTES: Resultado del controller: {postres}")
        if postres:
            return jsonify(postres), 200
        else:
            return jsonify({"mensaje": "no se encontraron postres"}), 404
    except Exception as e:
        print(f"🌐 ROUTES: ERROR: {e}")
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@postres_bp.route("/postres/<int:id>")
def get_one(id):
    try:
        postre = PostresController.get_one(id)
        if postre:
            return jsonify(postre), 200
        else:
            return jsonify({"mensaje": "no se encontro el postre"}), 404
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@postres_bp.route("/postres", methods=["POST"])
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

        postres = PostresController.create(data)
        if postres:
            return jsonify({'mensaje': 'postre creado correctamente'}), 201
        else:
            return jsonify({"mensaje": "error al crear el postre"}), 400
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@postres_bp.route("/postres/<int:id>", methods=["PUT"])
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

        postres = PostresController.update(data)
        if postres:
            return jsonify({'mensaje': 'postre editado correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al editar el postre"}), 400
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500


@postres_bp.route("/postres/<int:id>", methods=["DELETE"])
def eliminar(id):
    try:
        postres = PostresController.eliminar(id)
        if postres:
            return jsonify({'mensaje': 'postre eliminada correctamente'}), 200
        else:
            return jsonify({"mensaje": "error al eliminar el postre"}), 500
    except Exception as e:
        return jsonify({"mensaje": f"error : {str(e)}"}), 500
