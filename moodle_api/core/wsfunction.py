class WSFunction:

    def __init__(self):
        pass

    def descadastrar_curso(self, token, usuarioID, cursoID):
        descadastrar = {
            'wstoken': token,
            'wsfuntion' : 'enrol_manual_unenrol_users',
            'enrolments[0][userid]' : usuarioID,
            'enrolments[0][courseid]' : cursoID,
            'enrolments[0][roleid]' : 5, #5 para aluno
            'moodlewsrestformat' : 'json'
        }

        return descadastrar
    
    def diciplinas_matriculadas(self, token, usuarioID):
        todas_disciplinas_matriculadas = {
            'wstoken': token,
            'wsfuntion' : 'core_enrol_get_users_courses',
            'userid' : usuarioID,
            'moodlewsrestformat' : 'json'
        }

        return todas_disciplinas_matriculadas
    
    def cadastrar_curso(self, token, usuarioID, cursoID, timestamp_matricula, suspenso = 0):
        cadastrar = {
            'wstoken': token,
            'wsfuntion' : 'enrol_manual_enrol_users',
            'enrolments[0][userid]' : usuarioID,
            'enrolments[0][courseid]' : cursoID,
            'enrolments[0][timestart]' : timestamp_matricula, #em milisenconds, data de inicio
            'enrolments[0][suspend]' : suspenso, # 1 é suspenso e 0 ativo.
            'enrolments[0][roleid]' : 5, #5 para aluno
            'moodlewsrestformat' : 'json'
        }

        return cadastrar