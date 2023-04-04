from pymongo import MongoClient
from config.conexao import Conexao
from moodle_api.controllers.controle_datas import ControleData

class CasdastroAluno:
    
    def __init__(self):
        #self.Conexao = Conexao()
        #self.db = self.Conexao.database()
        self.data = ControleData()
    
    def cadastrar_aluno(self, dados):
        disciplinas = dict()   
        qtd_disciplinas = 15   
        
        loop_time = 1
        for i in range(1, int(qtd_disciplinas)):
            data_timestamp_temp = self.data.moodle_time(
                dados['data-matricula'],
                dados['cronograma'],
                qtd_disciplinas,
                loop_time
            )
            
            '''disciplinas.update({
                'id-disciplina' : dados['id-disciplina-' + i],
                'nome-disciplina' : dados['nome-disciplina-' + i],
                'data-liberacao' : data_timestamp_temp
            })'''
            
            disciplinas.update({
                'data-liberacao' : data_timestamp_temp
            })
            
            loop_time += 1
            
        novo_aluno = { 
            'id' : int(dados['id-curso']),
            'nome-completo' : dados['nome-aluno'],
            'data-matricula' : dados['data-cadastro'],
            #'nome-curso' : dados['qtd-disciplinas'],
            'id-curso' : dados['qtd-disciplinas'],
            'cronograma' : dados['cronograma'],
            'disciplinas' : disciplinas,
            'observacoes' : {
                'observacao' : dados['observacoes']
            }
        }
        
        #resultado = self.db.cursos.insert_one(novo_curso)
        
        return novo_aluno