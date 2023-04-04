from models.cadastrar_aluno import CasdastroAluno

class CadastrarAluno:
    
    def __init__(self):
        self.alunoModel = CasdastroAluno()
        
    def controle_cadastro(self, dados):
        dados = self.alunoModel.cadastrar_aluno(dados)
        return dados