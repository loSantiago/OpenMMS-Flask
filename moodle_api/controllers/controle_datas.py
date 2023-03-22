from datetime import datetime

class ControleData:

    def __init__(self):
        pass

    def time_stamp(self, data):
        dt = datetime.strptime(data, '%Y-%m-%d')
        ts = dt.timestamp()
        return ts

    def moodle_time(self, data):
        time = self.time_stamp(data)
        time = time * 1000
        return time
    

