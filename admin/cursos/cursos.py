from flask import Blueprint, render_template as render
from flask import request

cursos_bp = Blueprint("cursos_bp", __name__)

@cursos_bp.route('/cadastrar-curso', methods=['GET', 'POST'])
def cadastrar_curso():
    if request.method == 'POST':
        resultado = dict(request.form)
        return render('admin/cursos/cadastrar.html', resultado=resultado)
        
    return render('admin/cursos/cadastrar.html', resultado='')

@cursos_bp.route('/editar-curso')
def editar_curso():
    return render('admin/cursos/editar.html')

@cursos_bp.route('/visualizar-cursos')
def visualizar_curso():
    return render('admin/cursos/visualizar.html')