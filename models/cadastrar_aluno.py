from pymongo import MongoClient
from ..config.conexao import Conexao

class CadastrarCurso:
    
    def __init__(self):
        self.Conexao = Conexao()
        self.mongo = MongoClient(self.Conexao.string_connection())
    
    def salvarCurso(self):
        
        return 