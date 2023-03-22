import requests

from .wsfunction import WSFunction
from .token.wshost import WSHost
from ..controllers.controle_datas import ControleData
class WS:

    def __init__(self):
        self.WSHost = WSHost()
        self.WSFunction = WSFunction()
        self.CData = ControleData()
        
    def obter_lista_salas(self, dados):

        grade = []

        #string para enviar ao moodle
        query_string = self.WSFunction.diciplinas_matriculadas(self.WSHost.token(), dados['moodleID'])

        resposta = requests.get(self.WSHost.url(), query_string)
        resposta = resposta.json()

        print(query_string)
        
        for value in resposta:
            #grade.update({value['id']:value['fullname']})
            grade.append(value['id'])
        
        return grade

    def ocultar_salas(self, dados):

        lista_salas = self.obter_lista_salas(dados)
        grade = [979, 441, 478, 479, 978, 977, 268, 969, 372, 1137, 378, 214, 1136, 1138, 257]

        '''for id_curso in lista_salas:
            query_string = self.WSFunction.descadastrar_curso(self.WSHost.token(), dados['moodleID'],
                                                id_curso)
            resposta = requests.get(self.WSHost.url(), query_string)
            #resposta = resposta.json()'''

        '''for id_curso in grade:
            query_string = self.WSFunction.cadastrar_curso(self.WSHost.token(), dados['moodleID'],
                                            id_curso,
                                            self.CData.moodle_time(dados['dataMatricula']),
                                            dados['matriculaAtiva'])
            resposta = requests.get(self.WSHost.url(), query_string)'''
            
        #resposta = resposta.json()
        return "Oi"
            