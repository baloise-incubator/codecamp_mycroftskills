
from google.cloud import firestore

class persistence:

    def createItem(self, item):
        db = firestore.Client.from_service_account_json('./voice-assistant-330820-c4dbf6b3a7e9.json')
        doc_ref = db.collection(u'Einkaufsliste').document(f'{item}')
        amount = int(doc_ref.get({'amount'}).get('amount') or 0)
        doc_ref.set({
            u'amount': f'{amount + 1}',
        })
        return doc_ref.id + " " + doc_ref.get({'amount'}).get('amount')

    def removeItem(self, item):
        db = firestore.Client.from_service_account_json('./voice-assistant-330820-c4dbf6b3a7e9.json')
        doc_ref = db.collection(u'Einkaufsliste').document(f'{item}')
        amount = int(doc_ref.get({'amount'}).get('amount') or 0)
        if amount != 0:
            doc_ref.set({
                u'amount': f'{amount + 1}',
            })
        else:
            return "fail"

        return doc_ref.id + " " + doc_ref.get({'amount'}).get('amount')

if __name__ == '__main__':
    persistence = persistence()

    while True:
        item = (input("item: "))
        result = persistence.createItem(item)
        print(result)