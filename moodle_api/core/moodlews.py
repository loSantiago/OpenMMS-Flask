import requests

from .wsfunction import WSFunction
from .token.wstoken import WSTOKEN
class WS:

    def __init__(self):
        pass

    
    wsf = WSFunction(WSTOKEN.token())


    def obter_lista_salas(self, dados):

        id = dados['moodleID']
        
        query = wsf.diciplinas_matriculadas(id)

        response = requests.get(WSTOKEN.url(), query)

        return response
