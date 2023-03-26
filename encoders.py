import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendence-realtime-default-rtdb.firebaseio.com/",
    'storageBucket': "face-attendence-realtime.appspot.com"
})

folderPath = 'Images'
PathList = os.listdir(folderPath)

imgList = []
studentIds = []
for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])

    # Below codes will upload images to Database
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)


# Now generate encoding for the images

def find_encoding(imagesList):
    encodedList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # Face recognition uses RGB images
        encode = face_recognition.face_encodings(img)[0]
        encodedList.append(encode)
    return encodedList


encodedStudentList = find_encoding(imgList)
# print(len(encodedStudentList))
encodedStudentListIds = [encodedStudentList, studentIds]
#  print(encodedStudentListIds[0][0],encodedStudentListIds[1][0])

file = open("EncodeFile.p", 'wb')
pickle.dump(encodedStudentListIds, file)
file.close()
