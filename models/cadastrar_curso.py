from pymongo import MongoClient
from datetime import datetime
from config.conexao import Conexao

class CadastrarCurso:
    
    def __init__(self):
        self.Conexao = Conexao()  
        self.db = self.Conexao.database()
    
    def salvarCurso(self, dados):
        Data = datetime()
        
        disciplinas = dict()
        
        for i in range(1, int(dados['qtd-disciplinas'])):
            disciplinas.update({
                'id-disciplina' : dados['id-disciplina-' + i],
                'nome-disciplina' : dados['nome-disciplina-' + i]
            })
            
        novo_curso = { 
            'id' : int(dados['id-curso']),
            'nome' : dados['nome-curso'],
            'data-cadastro' : dados['data-cadastro'],
            'quantidade-disciplinas' : dados['qtd-disciplinas'],
            'carga-horaria' : dados['carga-horaria'],
            'disciplinas' : disciplinas,
            'observacoes' : {
                'data' : Data.now(),
                'observacao' : dados['observacoes']
            }
        }
        
        resultado = self.db.cursos.insert_one(novo_curso)
        
        return resultado