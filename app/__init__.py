from flask import Flask


def create_app() -> Flask:
    """Assembles and returns application."""
    app = Flask(__name__)

    @app.route("/")
    def hello_world():
        return "<p>Hello, World!</p>"

    return app
