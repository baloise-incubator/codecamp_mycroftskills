from mycroft import MycroftSkill, intent_file_handler
from mycroft.util.parse import extract_number, match_one, extract_datetime
from mycroft.util.format import nice_number

from .apiConnector import baloiseApiConnector


class InsurancePremiumSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    cantonDict = {
        'Basel Stadt': 'BS',
        'Basel Land': 'BL',
        'Zürich': 'ZH',
        'Bern': 'BE',
        'Freiburg': 'FR',
        'Aargau': 'AG'
    }

    @intent_file_handler('praemie_reise.intent')
    def handle_praemie_reise(self, message):

        cantonResponse = self.get_response('canton')
        canton, confidence = match_one(cantonResponse, self.cantonDict)
        postalCodeResponse = self.get_response('postalCode')
        postalCode = int(extract_number(postalCodeResponse, lang='de-de'))
        city = self.get_response('city').capitalize()
        try:
            date_of_birth_response = self.get_response('dateOfBirth')
            date_time = extract_datetime(date_of_birth_response, lang='de-de')
            date_of_birth = date_time.strftime('%Y-%m-%d')
        except:
            date_of_birth = '1990-10-10'

        persons_under14_response = self.get_response('personsUnder14')
        persons_under14 = int(extract_number(persons_under14_response, lang='de-de'))
        persons_over14_response = self.get_response('personsOver14')
        persons_over14 = int(extract_number(persons_over14_response, lang='de-de'))

        connector = baloiseApiConnector()
        response = connector.calculateTravelPremium(postalCode, city, canton, date_of_birth, persons_under14,
                                                    persons_over14, self.log)
        nice_response = nice_number(response, lang='de-de')
        self.speak_dialog('praemie_reise', data={
            'premium': nice_response
        })


def create_skill():
    return InsurancePremiumSkill()
