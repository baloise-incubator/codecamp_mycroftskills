from mycroft import MycroftSkill, intent_file_handler


class Tremplate(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('tremplate.intent')
    def handle_tremplate(self, message):
        self.speak_dialog('tremplate')


def create_skill():
    return Tremplate()

