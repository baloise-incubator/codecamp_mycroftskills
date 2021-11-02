
from google.cloud import firestore

class persistence:
    def getDbInstance():
        return firestore.Client.from_service_account_json(path + '/voice-assistant-330820-c4dbf6b3a7e9.json')
    
    def getDocRef():
        return db.collection(u'Einkaufsliste').document(f'{item}')
    
    def createItem(self, item, path):
        db = getDbInstance()
        doc_ref = getDocRef()
        amount = int(doc_ref.get({'amount'}).get('amount') or 0)
        doc_ref.set({
            u'amount': f'{amount + 1}',
        })
        return doc_ref.id + " " + doc_ref.get({'amount'}).get('amount')

    def removeItem(self, item, path):
        db = getDbInstance()
        doc_ref = getDocRef()
        amount = int(doc_ref.get({'amount'}).get('amount') or 0)
        if amount != 0:
            doc_ref.set({
                u'amount': f'{amount - 1}',
            })
            return doc_ref.get({'amount'}).get('amount')
        else:
            return "Fehlgeschlagen"

if __name__ == '__main__':
    persistence = persistence()

    while True:
        item = (input("item: "))
        result = persistence.removeItem(item)
        print(result)