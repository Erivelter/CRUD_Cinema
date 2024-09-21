from flask import Blueprint, render_template, request

cliente_route = Blueprint("cliente",__name__)

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

@cliente_route.route("/")
def listar_clientes():
    
    clientes = []
    return render_template('cadastro_cliente.html', clientes=clientes)
    

@cliente_route.route("/create", methods=['POST'])
def inserir_cliente():
    nome_cliente = request.form.get("nome") 
    email_cliente = request.form.get("email")  
    if nome_cliente and email_cliente:
        
        return f'Cliente {nome_cliente} cadastrado com sucesso!', 201
    return 'Dados do cliente não fornecidos', 400

@cliente_route.route("/<int:cliente_id>/edit", methods=['PUT'])
def update_cliente():
    pass

@cliente_route.route("/<int:cliente_id>/delete", methods=['DELETE'])
def delete_cliente():
    pass

