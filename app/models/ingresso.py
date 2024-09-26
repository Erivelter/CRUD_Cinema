from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Ingressos(db.Model):
    __tablename__ = 'ingressos'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True) 
    assento = db.Column(db.Integer, nullable=False)
    data_compra = db.Column(db.Date, nullable=False)

    sessao = db.relationship('Sessao', backref='ingressos', lazy='dynamic') 
    comprador = db.relationship('Cliente', backref='ingressos', lazy='dynamic')  
