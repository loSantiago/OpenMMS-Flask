from datetime import datetime, timedelta
import math

class ControleData:

    def __init__(self): #ss
        pass

    def time_stamp(self, data):
        dt = datetime.strptime(data, '%Y-%m-%d')
        ts = dt.timestamp()
        return ts

    def format_data(self, data):
        dt = datetime.strptime(data, '%Y-%m-%d')
        return dt
    
    def moodle_time(self, data, prazo, qtd_disciplina, loop_time):
        if loop_time > 1:
            qtd_dias = int(self.contagem_dias(prazo, 
                                    qtd_disciplina, 
                                    loop_time))
            
            nova_data = self.format_data(data) + timedelta(days=qtd_dias)
            print(nova_data)
            data_timestamp = self.time_stamp(nova_data)
        else:
            data_timestamp = self.time_stamp(data)

        return data_timestamp
    
    def contagem_dias(self, prazo, qtd_disciplinas, loop_time):
        prazo = int(prazo)
        qtd_disciplinas = int(qtd_disciplinas)

        total = math.floor(((30 * prazo) / qtd_disciplinas) * loop_time)

        return total


