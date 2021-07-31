import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from time import time
cred = credentials.Certificate('./jsonfilename.json')
firebase_admin.initialize_app(cred)
tic = time()
db = firestore.client()
plates_ref = db.collection(u'collection_name')
for doc in plates_ref.stream():
    print(u'{} => {}'.format(doc.id, doc.to_dict()))
toc = time()
print ("Ping : ",toc - tic)
