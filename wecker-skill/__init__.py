from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number, match_one, extract_datetime

class Wecker(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wecker.intent')
    def handle_wecker(self, message):
        
        zahl = int(extract_number(message.data.get('zahl'), lang='de-de'))
        zeit = message.data.get('zeit')
        if zeit == 'Stunden':
            zahlSekunden = getSekundenVonStunden(zahl)
        elif zeit == 'Minuten' or zeit == 'Minute':
            zahlSekunden = getSekundenVonMinuten(zahl)
        else:
            zahlSekunden = zahl
            
        elementFürDenSatz = str(zahl) + ' ' + zeit
            
        self.schedule_event(self.wecker, int(zahlSekunden), elementFürDenSatz)

    def wecker(self, message):
        self.speak(f'{message.data}' + ' sind um')

def create_skill():
    return Wecker()

def getSekundenVonMinuten(zahl):
    return zahl * 60

def getSekundenVonStunden(zahl):
    return zahl * 3600