from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number

from .apiConnector import baloiseApiConnector

class InsurancePremiumSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('praemie_reise.intent')
    def handle_praemie(self, message):
        canton = 'BS' #self.get_response('canton')
        postalCode =  '4001' #self.get_response('postalCode')
        city = self.get_response('city')
        dateofBirth = '21-10-1990' # self.get_response('dateOfBirth')
        personsUnder14 = extract_number(self.get_response('personsUnder14'),  lang='de-de')
        personsOver14 = extract_number(self.get_response('personsOver14'),  lang='de-de')

        connector = baloiseApiConnector()
        response = connector.calculateTravelPremium(postalCode, city, canton, dateofBirth, personsUnder14, personsOver14, self.log)
        self.speak_dialog('praemie_reise', data={
            'premium': response
        })

def create_skill():
    return InsurancePremiumSkill()

