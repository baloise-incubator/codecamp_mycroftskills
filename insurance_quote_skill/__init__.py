from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number, match_one, extract_datetime

from .apiConnector import baloiseApiConnector

class InsurancePremiumSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    cantonDict = {
        'Basel Stadt' : 'BS',
        'Basel Land' : 'BL',
        'Zürich' : 'ZH',
        'Bern' : 'BE',
        'Freiburg' : 'FR'
    }

    @intent_file_handler('praemie_reise.intent')
    def handle_praemie(self, message):

        cantonResponse = self.get_response('canton')
        canton, confidence = match_one(cantonResponse, self.cantonDict)
        postalCodeResponse = self.get_response('postalCode')
        postalCode = extract_number(postalCodeResponse, lang='de-de')
        city = self.get_response('city')
        dateOfBirthResponse = self.get_response('dateOfBirth')
        dateofBirth = extract_datetime(dateOfBirthResponse, lang='de-de')
        self.log.info('Date of Birth' + dateofBirth)
        personsUnder14Response = self.get_response('personsUnder14')
        personsUnder14 = extract_number(personsUnder14Response, lang='de-de')
        personsOver14Response = self.get_response('personsOver14')
        personsOver14 = extract_number(personsOver14Response, lang='de-de')

        connector = baloiseApiConnector()
        response = connector.calculateTravelPremium(postalCode, city, canton, dateofBirth, personsUnder14, personsOver14, self.log)
        self.speak_dialog('praemie_reise', data={
            'premium': response
        })

def create_skill():
    return InsurancePremiumSkill()

