
from google.cloud import firestore

class persistence:

    def createItem(self, item):
        db = firestore.Client(project='voice-assistant-330820') #Client.from_service_account_json('/Users/lukasbrendle/Downloads/voice-assistant-330820-c4dbf6b3a7e9.json')
        doc_ref = db.collection(u'Einkaufsliste').document(f'{item}')
        amount = doc_ref.get({'amount'}).get('amount')
        doc_ref.set({
            u'amount': f'{int(amount or 0) + 1}',
        })
        return doc_ref.id + " " + doc_ref.get({'amount'}).get('amount')

if __name__ == '__main__':
    persistence = persistence()

    while True:
        item = (input("item: "))
        result = persistence.createItem(item)
        print(result)