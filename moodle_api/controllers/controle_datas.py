from datetime import datetime, timedelta
import math

class ControleData:

    def __init__(self):
        pass

    def time_stamp(self, data):
        dt = data
        ts = dt.timestamp()
        return ts

    def format_data(self, data):
        dt = datetime.strptime(data, '%Y-%m-%d')
        return dt
    
    def moodle_time(self, data, prazo, qtd_disciplina, loop_time):
        dias_diciplinas = self.contagem_dias(prazo, qtd_disciplina, loop_time)
        
        nova_data = self.format_data(data)
        
        if loop_time > 1:
            nova_data = nova_data + timedelta(days=dias_diciplinas)
        
        data_timestamp = self.time_stamp(nova_data)
        
        return data_timestamp
    
    def contagem_dias(self, prazo, qtd_disciplinas, loop_time):
        prazo = int(prazo)
        qtd_disciplinas = int(qtd_disciplinas)
        loop_time = int(loop_time)

        qtd_dias = math.floor(((30 * prazo) / qtd_disciplinas) * loop_time)

        return qtd_dias


