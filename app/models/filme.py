from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Filme(db.Model):
    __tablename__ = 'filme'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(120), nullable=False)  
    diretor = db.Column(db.String(100))
    elenco = db.Column(db.Text)
    genero = db.Column(db.Text)
    sinopse = db.Column(db.Text)
    data_de_lancamento = db.Column(db.Date)
    duracao = db.Column(db.Integer)
    classificacao_etaria = db.Column(db.Integer)
    poster = db.Column(db.String(200))

   

# Filme:

# ID
# Título
# Diretor
# Elenco
# Gênero
# Sinopse
# Data de Lançamento
# Duração (em minutos)
# Classificação Etária
# Imagem do Cartaz
# Trailer (link para um vídeo ou URL)
