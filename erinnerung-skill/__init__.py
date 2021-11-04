from mycroft import MycroftSkill, intent_file_handler

from .erinnerungen import erinnerungen

class Erinnerung(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('erinnerung.intent')
    def handle_einkaufsliste(self):
        erinnerungInstance = erinnerungen()
        schedule_event(self, erinnerungInstance.erstelleErinnerung() ,5)

def create_skill():
    return Erinnerung()

