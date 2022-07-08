from flask import Flask
from flask_cors import CORS
from mysql import connector
from api.routes import main_blueprint

CREDENTIALS = {'host': 'db',
               'port': 3306,
               'user': 'pinner',
               'database': 'pinterest',
               'password': 'pintastic'}


def create_connector():
    return connector.connect(**CREDENTIALS)


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(main_blueprint)

    return app


app = create_app()

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=3000, debug=True)