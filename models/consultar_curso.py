from pymongo import MongoClient
from ..config.conexao import Conexao

class CadastrarCurso:
    
    def __init__(self):
        self.Conexao = Conexao()
        self.db = self.Conexao.database()
    
    def consultar_curso(self, id):
        Data = datetime()
        disciplinas = dict()        
        
        self.db.cursos.find_one({'id' : id})