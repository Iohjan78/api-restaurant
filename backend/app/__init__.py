# from flask import Flask
# from app.modules.marca.marca_routes import marca_bp
# from app.modules.categorias.categoria_routes import categoria_bp
# from app.modules.proveedores.proveedores_routes import proveedores_bp
# from app.modules.articulos.articulo_routes import articulos_bp
# from flask_cors import CORS


# def create_app():
#     app = Flask(__name__)
#     CORS(app, origins=["http://localhost:5173"], supports_credentials=True, methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"], allow_headers=["Content-Type", "Authorization"])
#     app.register_blueprint(marca_bp)
#     app.register_blueprint(categoria_bp)
#     app.register_blueprint(proveedores_bp)
#     app.register_blueprint(articulos_bp)
#     @app.route("/")
#     def home():
#         return "<h1>Hola Mundo!</h1>"
#     return app

# ------------------------------------------------------------------------------

# from flask import Flask
# from flask_cors import CORS

# from app.modules.categoria.categoria_routes import categoria_bp
# # from app.modules.platos.plato_routes import plato_bp
# # from app.modules.postres.postre_routes import postre_bp
# # from app.modules.bebidas.bebida_routes import bebida_bp


# def create_app():
#     """Factory function para crear y configurar la aplicación Flask"""

#     app = Flask(__name__)

#     # Configurar CORS
#     CORS(
#         app,
#         origins=["http://localhost:5173", "http://localhost:3000"],  # Vue dev server
#         supports_credentials=True,
#         methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
#         allow_headers=["Content-Type", "Authorization"]
#     )
#     app.register_blueprint(categoria_bp)
#     # app.register_blueprint(plato_bp)
#     # app.register_blueprint(postre_bp)
#     # app.register_blueprint(bebida_bp)

#     @app.route("/")
#     def home():
#         return {
#             "mensaje": "API Menú Digital - Restaurante",
#             "endpoints": {
#                 "categorias": "/categorias",
#                 "platos": "/platos",
#                 "postres": "/postres",
#                 "bebidas": "/bebidas"
#             }
#         }

#     @app.route("/health")
#     def health():
#         return {"status": "ok"}, 200

#     return app

from flask import Flask  # type: ignore
from flask_cors import CORS  # type: ignore
from app.modules.categoria.categoria_routes import categoria_bp
from app.modules.platos.platos_routes import platos_bp
from app.modules.bebidas.bebidas_routes import bebidas_bp
from app.modules.postres.postres_routes import postres_bp


def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    app.config['JSON_SORT_KEYS'] = False
    app.json.ensure_ascii = False
    CORS(app)
    app.register_blueprint(categoria_bp)
    app.register_blueprint(platos_bp)
    app.register_blueprint(bebidas_bp)
    app.register_blueprint(postres_bp)

    @app.route("/")
    def home():
        return {"mensaje": "API funcionando"}

    return app
