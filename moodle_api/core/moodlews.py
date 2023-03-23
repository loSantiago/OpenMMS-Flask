from .wsfunction import WSFunction
from ..controllers.controle_datas import ControleData
from ..controllers.requisicoes import WSRequest
class MoodleWS:

    def __init__(self):
        self.WSRequest = WSRequest()
        self.WSFunction = WSFunction()
        self.CData = ControleData()
        
    def obter_lista_salas(self, dados):
        #string para enviar ao moodle
        query_string = self.WSFunction.diciplinas_matriculadas(dados['moodleID'])
                                                               
        #Faz a requisição ao
        resposta = self.WSRequest.get(query_string)

        resposta = self.WSRequest.json(resposta)

        #Lista de disciplinas matriculadas do aluno, captura somente o ID
        grade = []
        for value in resposta:
            #grade.update({value['id']:value['fullname']})
            grade.append(value['id'])
        
        return grade

    def ocultar_salas(self, dados):

        grade = [979, 441, 478, 479, 978, 977, 268, 969, 372, 1137, 378, 214, 1136, 1138, 257]

        #Realiza a chama para obter as disciplinas cadastradas do aluno.
        lista_salas = self.obter_lista_salas(dados)
        
        #Loop Time é a ordem de execução do loop, em qual ciclo ele esta.
        loop_time = 1

        #Para escopo de função.
        resposta = None

        for id_curso in lista_salas:
            #montagem da query para enviar ao moodle.
            query_string = self.WSFunction.descadastrar_curso(dados['moodleID'], 
                                                              id_curso)
            resposta = self.WSRequest.get(query_string)
            resposta = self.WSRequest.json(resposta)

        #
        for id_curso in grade:
            qtd_disciplina = len(grade)

            #montagem da query para enviar ao moodle.
            query_string = self.WSFunction.cadastrar_curso(dados['moodleID'],
                                            id_curso,
                                            int(self.CData.moodle_time(dados['dataMatricula'],
                                            dados['cronograma'], qtd_disciplina, loop_time)),
                                            dados['matriculaAtiva'])
            
            print("STRING:", query_string)

            loop_time += 1
            resposta = self.WSRequest.get(query_string)
            
        resposta = self.WSRequest.json(resposta)

        return resposta
            