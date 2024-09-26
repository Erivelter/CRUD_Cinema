from flask import Flask
from config import Config  
from models.__init__ import db
from models.cliente import Cliente
from models.filme import Filme
from models.ingresso import Ingressos
from models.sessao import Sessao
from routes.cliente import cliente_route 

app = Flask(__name__)
app.config.from_object(Config) 

db.init_app(app)
app.register_blueprint(cliente_route, url_prefix='/cliente')

@app.route("/", methods=['GET'])
def test():
    return "FUNCIONANDO"

with app.app_context():
    db.create_all()  # Cria todas as tabelas

if __name__ == "__main__":
    app.run(debug=True)
