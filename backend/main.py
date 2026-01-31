# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return {'message': 'Hello from Flask!'}

# @app.route('/api/test')
# def test():
#     return {'status': 'ok', 'data': 'Backend funcionando'}

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000, debug=True)

from app import create_app
import os

app = create_app()

if __name__ == '__main__':                                                    
    port = int(os.environ.get("PORT", 8000))                                
    debug = os.environ.get("FLASK_DEBUG", "False").lower() == "true"        
    app.run(host='0.0.0.0', port=port, debug=debug)  
