from flask import Flask
from routes.cliente import cliente_route

app = Flask(__name__)

app.register_blueprint(cliente_route, url_prefix='/cliente') 

@app.route("/", methods=['GET'])
def test():
    return"FUNCIONADO"

if __name__ == "__main__":
    app.run(debug=True)