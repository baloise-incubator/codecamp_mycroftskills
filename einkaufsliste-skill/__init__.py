from mycroft import MycroftSkill, intent_file_handler

from .einkaufsliste_persistence import persistence

class Einkaufsliste(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('einkaufsliste.intent')
    def handle_einkaufsliste(self, message):
        item = message.data.get('item')
        persistenceInstance = persistence()
        response = persistenceInstance.createItem(item,self.file_system.path)
        self.speak_dialog('einkaufsliste', data={
            'item': response
        })
        
    @intent_file_handler('loescheeinkaufsliste.intent')
    def handle_loescheinkaufsliste(self, message):
        item = message.data.get('item')
        persistenceInstance = persistence()
        response = persistenceInstance.removeItem(item,self.file_system.path)
        if response != "Fehlgeschlagen":
            self.speak_dialog('loescheinkaufsliste', data={
            'item': response
        })
        else:
            self.speak_dialog('error', data={
            'item': response
        })   


def create_skill():
    return Einkaufsliste()

