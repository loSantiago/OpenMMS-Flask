from pymongo import MongoClient
from ..config.conexao import Conexao

class CadastrarCurso:
    
    def __init__(self):
        self.Conexao = Conexao()
        
        try:
            self.mongo = MongoClient(self.Conexao.string_connection())
        except Exception:
            self.exception = Exception
            return self.exception
    
    def salvarCurso(self):
        
        return 