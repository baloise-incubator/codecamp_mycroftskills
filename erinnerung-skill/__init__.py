from mycroft import MycroftSkill, intent_file_handler

class Erinnerung(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('erinnerung.intent')
    def handle_erinnerung(self, zeit):
        timedict = {
            "Zeit": zeit
        }
        self.schedule_event(self.wecker, timedict)

    def wecker(self):
        self.speak(timedict)

def create_skill():
    return Erinnerung()

