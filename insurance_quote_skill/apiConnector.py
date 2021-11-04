

import requests
from datetime import datetime

from .__init__ import InsurancePremiumSkill


class baloiseApiConnector:

    travelAPIUrl = 'https://www.baloise.ch/mybaloise-api/public/api/traveloffering/v2/createTravelOffering'

    def calculateTravelPremium(self, postalCode, city, canton, dateofBirth, personsUnder14, personsOver14, skill : InsurancePremiumSkill):
        startDate = datetime.now().strftime('%d-%m-%Y')
        json = {'riskRelevantData':
            {
                'postalCode':f'{postalCode}',
                'city':f'{city}',
                'canton':f'{canton}',
                'dateOfBirth':f'{dateofBirth}',
                'periodStartDate':f'{startDate}',
                'personsUnder14':int(personsUnder14),
                'personsOver14':int(personsOver14)
            },
            'language':'DE'}
        skill.log.info(json)
        response = requests.post(self.travelAPIUrl, json=json)
        premium = response.json()['payload']['baseData']['premium']
        return premium + " Franken"

if __name__ == '__main__':

    url = 'https://www.baloise.ch/mybaloise-api/public/api/traveloffering/v2/createTravelOffering'
    json = {'riskRelevantData':
                 {
                     'postalCode':'4001',
                     'city':'Basel',
                     'canton':'BS',
                     'dateOfBirth':'1990-12-22',
                     'periodStartDate':'2021-11-04',
                     'personsUnder14':0,
                     'personsOver14':1
                 },
        'language':'DE'}

    response = requests.post(url, json=json)
    print(response.request.body)
    print(response.json())
    print(datetime.now().strftime('%d-%m-%Y'))