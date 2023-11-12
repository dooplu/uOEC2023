import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("uoec2023f.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

#to get all the data of every id

def insertalldata (thisDic):
    
    doc_ref = db.collection('Reports').document()
    doc_ref.set(thisDic)


def getdata ():
    docs = db.collection('Reports').get()
    reports = []
    for doc in docs:
        reports.append(doc.to_dict())

    return reports


