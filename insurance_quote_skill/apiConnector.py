import string

import requests
import base64
from datetime import datetime


class baloiseApiConnector:
    travelAPIUrl = 'https://www.baloise.ch/mybaloise-api/public/api/traveloffering/v2/createTravelOffering'
    travelAPIUpdateUrl = 'https://www.baloise.ch/mybaloise-api/public/api/traveloffering/v2/updateCoverages'
    submissionInfo: string
    quoteID: string
    encryptedQuoteID: string
    sessionUUID: string

    def calculateTravelPremium(self, postalCode, city, canton, dateOfBirth, personsUnder14, personsOver14, log):
        startDate = datetime.now().strftime('%Y-%m-%d')
        json = {'riskRelevantData':
            {
                'postalCode': f'{postalCode}',
                'city': f'{city}',
                'canton': f'{canton}',
                'dateOfBirth': f'{dateOfBirth}',
                'periodStartDate': f'{startDate}',
                'personsUnder14': int(personsUnder14),
                'personsOver14': int(personsOver14)
            },
            'language': 'DE'}
        log.info(json)
        response = requests.post(self.travelAPIUrl, json=json)
        premium = response.json()['payload']['baseData']['premium']
        self.submissionInfo = response.json()['payload']['submissionInfo']
        self.quoteID = self.submissionInfo['quoteId']
        self.encryptedQuoteID = self.submissionInfo['encryptedQuoteId']
        self.sessionUUID = self.submissionInfo['sessionUuid']
        return premium

    def updateCoverages(self,
                        travelLifeAnnulmentCosts: bool,
                        travelLifeAssistanceAndBaggage: bool,
                        travelDriveCoverage: bool):
        json = {"coverages":
            {
                "travelLifeAnnulmentCosts": travelLifeAnnulmentCosts,
                "travelLifeAssistanceAndBaggage": travelLifeAssistanceAndBaggage,
                "travelDriveCoverage": travelDriveCoverage
            },
            "submissionInfo": {
                "quoteId": self.quoteID,
                "encryptedQuoteId": self.encryptedQuoteID,
                "sessionUuid": self.sessionUUID
            }
        }
        response = requests.put(self.travelAPIUpdateUrl, json=json)
        premium = response.json()['payload']['baseData']['premium']
        return premium
