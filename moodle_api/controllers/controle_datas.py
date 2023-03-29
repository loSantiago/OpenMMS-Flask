from datetime import datetime, timedelta
import math

'''
    Classe responsavel por todo controle de datas,
    existente dentro da logica e regra de negocios.
'''
class ControleData:

    def __init__(self):
        self.data_corrente = list()

    #Gera o timestamp baseado na data.
    def time_stamp(self, data):
        dt = data
        ts = dt.timestamp()
        return ts

    #Realiza a transformação da data da view para a datetime
    def format_data(self, data):
        dt = datetime.strptime(data, '%Y-%m-%d')
        return dt
    
    #Recebe os dados de moodlews e retonar, a data em timestemp
    def moodle_time(self, data, prazo, qtd_disciplina, loop_time):
        dias_diciplinas = self.contagem_dias(prazo, qtd_disciplina, loop_time)
        
        nova_data = self.format_data(data)        
        
        if loop_time > 1:
            nova_data = nova_data + timedelta(days=dias_diciplinas)
        
        self.data_corrente.append(nova_data.strftime('%d/%m/%Y'))
        data_timestamp = self.time_stamp(nova_data)
        
        return data_timestamp
    
    #Realiza a contagem de dias entre disciplinas,
    #baseado no prazo e qtd da matriz.
    def contagem_dias(self, prazo, qtd_disciplinas, loop_time):
        prazo = int(prazo)
        qtd_disciplinas = int(qtd_disciplinas)
        loop_time = int(loop_time)

        qtd_dias = math.floor(((30 * prazo) / qtd_disciplinas) * loop_time)

        return qtd_dias
    
    #responsavel apenas pelo retorno das datas atuais.
    def grade_datas(self):
        return self.data_corrente


