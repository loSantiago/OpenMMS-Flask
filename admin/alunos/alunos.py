from flask import Blueprint, render_template as render
from flask import request

from moodle_api.core.moodlews import WS

ws = WS()

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
        
        dados = dict(request.form)
        print(dados)
        fui = ws.obter_lista_salas(dados)
        return render('admin/alunos/ocultar.html', fui=fui)
    else:
        return render('admin/alunos/ocultar.html', fui="void")