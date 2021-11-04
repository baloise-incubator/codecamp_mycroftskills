from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number, match_one, extract_datetime
from mycroft.util.format import nice_number

from .apiConnector import baloiseApiConnector

class InsurancePremiumSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    cantonDict = {
        'Basel Stadt' : 'BS',
        'Basel Land' : 'BL',
        'Zürich' : 'ZH',
        'Bern' : 'BE',
        'Freiburg' : 'FR',
        'Aargau' : 'AG'
    }

    @intent_file_handler('praemie_reise.intent')
    def handle_praemie_reise(self, message):

        cantonResponse = self.get_response('canton')
        canton, confidence = match_one(cantonResponse, self.cantonDict)
        postalCodeResponse = self.get_response('postalCode')
        postalCode = int(extract_number(postalCodeResponse, lang='de-de'))
        city = self.get_response('city')
        #dateOfBirthResponse = self.get_response('dateOfBirth')
        #dateofBirth = extract_datetime(dateOfBirthResponse, lang='de-de')
        personsUnder14Response = self.get_response('personsUnder14')
        personsUnder14 = int(extract_number(personsUnder14Response, lang='de-de'))
        personsOver14Response = self.get_response('personsOver14')
        personsOver14 = int(extract_number(personsOver14Response, lang='de-de'))

        connector = baloiseApiConnector()
        response = connector.calculateTravelPremium(postalCode, city, canton, '1990-10-10', personsUnder14, personsOver14, self.log)
        nice_response = nice_number(response, lang='de-de')
        self.speak_dialog('praemie_reise', data={
            'premium': nice_response
        })

def create_skill():
    return InsurancePremiumSkill()

