from flask import Flask, jsonify


def create_app() -> Flask:
    app = Flask(__name__)
    init_app(app)

    return app


def init_app(app: Flask):
    @app.route("/")
    def index():
        return jsonify({})
