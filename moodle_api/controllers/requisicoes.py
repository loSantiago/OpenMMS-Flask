import requests
from ..core.token.wshost import WSHost

class WSRequest:

    def __init__(self):
        self.WSHost = WSHost()

    def get(self, query_string):
        reposta = requests.get(self.WSHost.url(), query_string)

        return reposta
    
    def json(self, string):
        string = string.json()
        
        return string