class Conexao:
    
    def __init__(self):
        self.mongo = 'mongodb+srv://'
        self.dbuser = ''
        self.dbpass = ''
        self.host = ''
        self.dbname = ''
        self.dbport = ''
        
    def string_connection():
        
        stringdb = self.mongo + self.dbuser + self.mdbpass + self.host + '/' + \
                   self.dbname + 'retryWrites=true&w=majority'
                   
        return stringdb