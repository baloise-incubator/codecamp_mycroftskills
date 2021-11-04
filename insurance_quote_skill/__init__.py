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

    booleanDict = {

    }

    @intent_file_handler('premium_travel.intent')
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
        self.speak_dialog('premium_travel', data={
            'premium': nice_response
        }, Wait=True)
        adapt_response = self.ask_yesno('premium_adapt')

        if adapt_response == 'yes':
            annullment_costs = self.ask_yesno('annullment_costs')
            assistance_baggage = self.ask_yesno('assistance_and_baggage')
            drive_coverage = self.ask_yesno('drive_coverage')
            try:
                response = connector.updateCoverages(annullment_costs, assistance_baggage, drive_coverage)
                nice_response = nice_number(response, lang='de-de')
                self.speak_dialog('premium_travel', data={
                    'premium': nice_response
                }, Wait=True)
            except:
                self.speak('Ein Fehler ist aufgetreten - bitte versuche es später erneut', Wait=True)

        self.speak_dialog('finished')



def create_skill():
    return InsurancePremiumSkill()
