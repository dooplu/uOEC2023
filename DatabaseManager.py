import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("uoec2023f.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

#to get all the data of every id

def insertalldata (thisDic):
    
    doc_ref = db.collection('Link').document()
    doc_ref.set(thisDic["link"])

    doc_ref = db.collection('Usernames').document()
    doc_ref.set(thisDic["username"])


    doc_ref = db.collection('Reports').document()
    doc_ref.set(thisDic["report"])


def getdata ():

    docs = db.collection('Link').get()
    for doc in docs:
        print(doc.to_dict())

    docs = db.collection('Usernames').get()
    for doc in docs:
        print(doc.to_dict())

    docs = db.collection('Reports').get()
    for doc in docs:
        print(doc.to_dict())


