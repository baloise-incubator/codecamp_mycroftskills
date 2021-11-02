from mycroft import MycroftSkill, intent_file_handler

from .einkaufsliste_persistence import persistence

class Einkaufsliste(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('einkaufsliste.intent')
    def handle_einkaufsliste(self, message):
        item = message.data.get('item')
        response = persistence.createItem(item)
        self.speak_dialog('einkaufsliste', data={
            'item': response
        })
        
    @intent_file_handler('loescheeinkaufsliste.intent')
    def handle_loescheinkaufsliste(self, message):
        item = message.data.get('item')

        self.speak_dialog('loescheinkaufsliste', data={
            'item': item
        })   


def create_skill():
    return Einkaufsliste()

