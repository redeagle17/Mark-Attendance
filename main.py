import cv2
import cvzone
# import streamlit as st
import os
import pickle
import face_recognition
import numpy as np
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
from datetime import datetime


def mark_attendance_of_student(usn, mark_attendance, studentDetail):
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred, {
        'databaseURL': "https://face-attendence-realtime-default-rtdb.firebaseio.com/",
        'storageBucket': "face-attendence-realtime.appspot.com"
    })

    # FRAME_WINDOW = st.image([])
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    imgBackground = cv2.imread('Resources/background.png')
    # imgBackground = cv2.cvtColor(imgBackground, cv2.COLOR_BGR2RGB)
    # imgBackground = st.image('Resources/background.png')

    # Importing the mode images into a list
    folderModePath = 'Resources/Modes'
    modePathList = os.listdir(folderModePath)
    imgModeList = []
    for path in modePathList:
        imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

    #  Load EncodeFile.p using pickle
    file = open("EncodeFile.p", 'rb')
    encodedStudentListIds = pickle.load(file)
    file.close()
    encodedStudentList, studentIds = encodedStudentListIds
    # print(studentIds)
    modeType = 0
    counter = 0
    id = -1
    imgStudentfromStorage = []
    bucket = storage.bucket()

    while True:
        success, img = cap.read()
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)  # Scaling to one-fourth of the image (img).
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        faceCurFrame = face_recognition.face_locations(imgS)
        encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
        # print(encodeCurFrame,faceCurFrame)
        imgBackground[162:162 + 480, 55:55 + 640] = img
        imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

        if faceCurFrame:
            for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
                matches = face_recognition.compare_faces(encodedStudentList, encodeFace)
                faceDis = face_recognition.face_distance(encodedStudentList, encodeFace)
                # print(matches)
                matchIndex = np.argmin(faceDis)
                # print(matchIndex)
                # print(matches, faceDis)
                if matches[matchIndex]:
                    # print("3")
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
                    imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                    id = studentIds[matchIndex]
                    if counter == 0:
                        counter = 1
                        modeType = 1
            if counter != 0:
                if counter == 1:
                    # Get the students data from database
                    studentData = db.reference(f'Students/{usn}').get()

                    # Get the Image from the storage
                    blob = bucket.get_blob(f'Images/{usn}.png')
                    array = np.frombuffer(blob.download_as_string(), np.uint8)
                    imgStudentfromStorage = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)

                    datetimeObject = datetime.strptime(studentData['last_attendance_time'],
                                                       "%Y-%m-%d %H:%M:%S")
                    secondsElapsed = (datetime.now() - datetimeObject).total_seconds()

                    if secondsElapsed > 30:
                        # After every 30 seconds the students can be again marked present
                        # Update the attendance and last time of attendance
                        ref = db.reference(f'Students/{usn}')
                        # print(mark_attendance)
                        studentData[mark_attendance] += 1
                        ref.child(mark_attendance).set(studentData[mark_attendance])
                        ref.child('last_attendance_time').set(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                    else:
                        modeType = 3
                        counter = 0
                        imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

                if modeType != 3:
                    if 10 < counter < 20:
                        modeType = 2
                    imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]

                    if counter <= 10:
                        cv2.putText(imgBackground, str(studentData[mark_attendance]), (861, 125),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1,
                                    (255, 255, 255), 1)
                        cv2.putText(imgBackground, str(studentData[mark_attendance]), (861, 125),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 1)
                        cv2.putText(imgBackground, str(studentData['major']), (1006, 550),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                        cv2.putText(imgBackground, usn, (1006, 493),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                        cv2.putText(imgBackground, str(studentData['standing']), (910, 625),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 100, 100), 1)
                        li = mark_attendance.split('_')
                        cv2.putText(imgBackground, li[0], (1025, 625),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 100, 100), 1)
                        cv2.putText(imgBackground, str(studentData['starting_year']), (1125, 625),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (100, 100, 100), 1)
                        (w, h), _ = cv2.getTextSize(studentData['name'], cv2.FONT_HERSHEY_SIMPLEX, 1, 1)
                        offset = (414 - w) // 2  # To put name in the center
                        cv2.putText(imgBackground, str(studentData['name']), (808 + offset, 445),
                                    cv2.FONT_HERSHEY_SIMPLEX, 1, (50, 50, 50), 1)
                        imgBackground[175:175 + 216, 909:909 + 216] = imgStudentfromStorage

                    counter = counter + 2
                    if counter >= 20:
                        imgStudentfromStorage = []
                        modeType = 0
                        counter = 0
                        studentData = []
                        imgBackground[44:44 + 633, 808:808 + 414] = imgModeList[modeType]
        else:
            modeType = 0
            counter = 0

        # FRAME_WINDOW.image(imgBackground)
        cv2.imshow("IMAGE", imgBackground)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
