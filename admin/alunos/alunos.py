from flask import Blueprint, render_template as render
from flask import request

alunos_bp = Blueprint("alunos_bp", __name__)

@alunos_bp.route('/admin')
def index_admin():
    return render('navbar.html')

@alunos_bp.route('/cadastrar-aluno')
def cadastrar_aluno():
    return render('admin/alunos/cadastrar.html')

@alunos_bp.route('/editar-aluno')
def editar_aluno():
    return render('admin/alunos/editar.html')

@alunos_bp.route('/visualizar-alunos')
def visualizar_aluno():
    return render('admin/alunos/visualizar.html')

#Rotas de dados
@alunos_bp.route('/ocultar-aluno', methods=["GET", "POST"])
def ocultar_aluno():
    if request.method == "POST":
        recebe(request.body)
        return render('admin/alunos/ocultar.html', fui="OK")
    else:
        return render('admin/alunos/ocultar.html', fui="0")