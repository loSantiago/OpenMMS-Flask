import requests

from .wsfunction import WSFunction
from .token.wstoken import WSTOKEN
class WS:

    def __init__(self):
        self.WSToken = WSTOKEN()
        self.WSFunction = WSFunction()
        self.token = '630a8a74add6feca08e10597be94e404'
        
    def obter_lista_salas(self, id):

        grade = dict()
        #id = dados['moodleID']
        token = '630a8a74add6feca08e10597be94e404'

        #string para enviar ao moodle
        query_string = self.WSFunction.diciplinas_matriculadas(token, id)

        resposta = requests.get('https://ava.ethoson.com.br/webservice/rest/server.php', query_string)
        resposta = resposta.json()

        for value in resposta:
            grade.update({value['id']:value['fullname']})

        print('Resposta Moodle', resposta)
        return grade

    def ocultar_salas(self, dados):

        lista_salas = self.obter_lista_salas(dados['id'])

        for key in lista_salas:
            query_string = (self.WSFunction.descadastrar_curso(self, id, key))

            query_string = self.WSFunction.cadastrar_curso(self.token, id, )