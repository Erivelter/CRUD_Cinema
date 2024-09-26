from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sessao(db.Model):
    __tablename__ = 'sessao'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  
    hora_inicio = db.Column(db.DateTime)  
    hora_final = db.Column(db.DateTime)  
    disponibilidade = db.Column(db.Integer)
    sala = db.Column(db.String(60))
    filme_id = db.Column(db.Integer, db.ForeignKey('filme.id'))
    filme = db.relationship('Filme', backref='sessoes', lazy='dynamic')  

# Sessão:
# ID
# Filme (referência ao ID do filme)
# Sala
# Horário de Início
# Horário de Fim
# Disponibilidade (quantidade de assentos disponíveis)
