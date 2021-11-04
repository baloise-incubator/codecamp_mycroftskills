import requests
from datetime import datetime


class baloiseApiConnector:

    travelAPIUrl = 'https://www.baloise.ch/mybaloise-api/public/api/traveloffering/v2/createTravelOffering'

    def calculateTravelPremium(self, postalCode, city, canton, dateOfBirth, personsUnder14, personsOver14, log):
        startDate = datetime.now().strftime('%Y-%m-%d')
        json = {'riskRelevantData':
            {
                'postalCode':f'{postalCode}',
                'city':f'{city}',
                'canton':f'{canton}',
                'dateOfBirth': f'{dateOfBirth}',
                'periodStartDate':f'{startDate}',
                'personsUnder14':int(personsUnder14),
                'personsOver14':int(personsOver14)
            },
            'language':'DE'}
        log.info(json)
        response = requests.post(self.travelAPIUrl, json=json)
        premium = response.json()['payload']['baseData']['premium']
        return premium