import pyrebase
import platform
import os
from math import cos, asin, sqrt
import glob
import time
###Using the Haversine Formula, we can calculate the difference
###between two points whose latituede and logitude are given
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin...

config={        #fill according to your firebase database    
    "apiKey": "AIzaSyAT4UUWIA9HW2CFMgr5T4MuMz5OTbvUC18",
    "authDomain": "",
    "databaseURL": "https://lifesaver-18f28.firebaseio.com",
    "storageBucket": "lifesaver-18f28.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
allCats = db.get()
print("Value=",allCats.val()['auto']['lat'])
print(allCats.val())
for i in allCats.val():
    for j in allCats.val()[i]:
        print(i,j)
        #print(allCats.val()[i][j])
        
