from flask import Flask, Blueprint
from routes.index import index_bp
from admin.alunos.alunos import alunos_bp
from admin.cursos.cursos import cursos_bp
from admin.configuracoes.config import config_bp


app = Flask(__name__, static_folder="public", static_url_path="")

#index
app.register_blueprint(index_bp)

#Alunos routes and configs
app.register_blueprint(alunos_bp, url_prefix='/admin')

#Cursos routes and configs
app.register_blueprint(cursos_bp, url_prefix='/admin')

#Cursos routes and configs
app.register_blueprint(config_bp, url_prefix='/admin')

#Seguraça;
if __name__ == "__main__":
    app.run()