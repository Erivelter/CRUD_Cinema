from flask import Blueprint, render_template, request, redirect, url_for
from models import db
from models.cliente import Cliente

cliente_route = Blueprint("cliente",__name__)

@cliente_route.route("/")
def listar_clientes():
    lista_clientes = Cliente.query.all()  # Busca todos os clientes no banco de dados
    return render_template('cadastro_cliente.html', clientes=lista_clientes)
    

@cliente_route.route("/create", methods=['POST'])
def inserir_cliente():
    nome_cliente = request.form.get("nome") 
    email_cliente = request.form.get("email") 
    senha_cliente = request.form.get("senha") 

    if nome_cliente and email_cliente and senha_cliente:
        db.session.add(Cliente(nome=nome_cliente, email=email_cliente))
        db.session.commit()
        return redirect(url_for('cliente.listar_clientes'))  # Redireciona para listar clientes
    return 'Dados do cliente não fornecidos', 400

# @cliente_route.route("/<int:cliente_id>/edit", methods=['PUT'])
# def update_cliente():
#     pass

# @cliente_route.route("/<int:cliente_id>/delete", methods=['DELETE'])
# def delete_cliente():
#     pass




"""
Create: Permitir que novos usuários se registrem (se você estiver implementando um sistema de login).
Read: Consultar informações do usuário (se necessário).
Update: Permitir que o usuário atualize suas informações.
Delete: Permitir que o usuário exclua sua conta (se aplicável).

/cliente/ (POST) - Criar cliente
/cliente/ (GET) - listar todos os clientes
/cliente/<id>/update (PUT) - atualizar informações do cliente
/cliente/<id>/delete (DELETE) - deletar cliente
"""