from flask import Blueprint, render_template as render

config_bp = Blueprint("config_bp", __name__)

@config_bp.route('/usuarios')
def usuarios():
    return render('admin/config/usuarios.html')