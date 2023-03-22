import requests

from .wsfunction import WSFunction
from .token.wstoken import WSTOKEN
class WS:

    def __init__(self):
        self.WSToken = WSTOKEN()
        self.WSFunction = WSFunction()
        
    def obter_lista_salas(self, dados):

        id = dados['moodleID']
        
        query = self.WSFunction.diciplinas_matriculadas(self.WSToken.token(), id)

        response = requests.get(WSTOKEN.url(), query)

        return response