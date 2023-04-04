from pymongo import MongoClient

class Conexao:
    
    def __init__(self):
        self.mongo = 'mongodb+srv://'
        self.dbuser = 'admin'
        self.dbpass = ''
        self.host = 'localhost'
        self.dbname = 'EthosOnline'
        self.dbport = '27017'
        
    # Monta a string de conexão com o mongodb
    def string_connection(self):
        stringdb = self.mongo + self.dbuser + self.mdbpass + self.host + ':' + \
                   self.port
                   
        return stringdb
    
    # Realiza a conexão com o banco. 
    def try_connection(self):
        try:
            self.mongo = MongoClient(self.Conexao.string_connection())
        except Exception:
            self.exception = Exception
            return self.exception
        
        return self.mongo
    
    #Mude 'teste' para o nome da sua database.
    # Retorna esta conexão.
    def database(self):
        conexao = self.try_connection()
        return conexao.teste