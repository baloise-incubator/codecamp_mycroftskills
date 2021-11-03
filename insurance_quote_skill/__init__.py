from mycroft import MycroftSkill, intent_file_handler

from .einkaufsliste_persistence import persistence

from .apiConnector import baloiseApiConnector

class Einkaufsliste(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('praemie_reise.intent')
    def handle_praemie(self, message):
        canton = self.get_response('canton')
        postalCode = self.get_response('postalCode')
        city = self.get_response('city')
        dateofBirth = self.get_response('dateOfBirth')
        personsUnder14 = self.get_response('personsUnder14')
        personsOver14 = self.get_response('personsOver14')

        connector = baloiseApiConnector()
        response = connector.calculateTravelPremium(postalCode, city, canton, dateofBirth, personsUnder14, personsOver14)
        self.speak_dialog('praemie_reise', data={
            'premium': response
        })

def create_skill():
    return Einkaufsliste()

