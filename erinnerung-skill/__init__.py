from mycroft import MycroftSkill, intent_file_handler

class Erinnerung(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('erinnerung.intent')
    def handle_erinnerung(self, message):
        zeit = message.data.get('zeit')
        self.schedule_event(self.wecker, int(zeit), zeit)

    def wecker(self, message):
        self.speak(f'{message.data}' + ' sind um')

def create_skill():
    return Erinnerung()

