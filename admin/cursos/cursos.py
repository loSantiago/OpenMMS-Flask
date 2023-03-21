from flask import Blueprint, render_template as render

cursos_bp = Blueprint("cursos_bp", __name__)

@cursos_bp.route('/cadastrar-curso')
def cadastrar_curso():
    return render('admin/cursos/cadastrar.html')

@cursos_bp.route('/editar-curso')
def editar_curso():
    return render('admin/cursos/editar.html')

@cursos_bp.route('/visualizar-cursos')
def visualizar_curso():
    return render('admin/cursos/visualizar.html')