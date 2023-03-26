# Mark-Attendance

### Recognize The faces And Take Automatic Attendance.✨

![Logo](https://www.ramco.com/hs-fs/hubfs/facial-recognition.jpg?width=650&height=550&name=facial-recognition.jpg)

## Abstract
The management of the attendance can be a great burden on the teachers if it is done by hand. To resolve this problem, smart and auto attendance management system is being utilized. By utilizing this framework, the problem students being marked present even though they are not physically present can easily be solved. This system marks the attendance using live video stream. The frames are extracted from video using OpenCV. The main implementation steps used in this type of system are face detection and recognizing the detected face, for which dlib is used. After these, the connection of recognized faces ought to be conceivable by comparing with the database containing student's faces. Later, the data of the student is updated in realtime Datatbase.This model will be a successful technique to manage the attendance of students.

## Feature 📋
- Train the model on the faces from Datatbase
- Capture face from webcam
- Compare faces from the faces present in Datatbase
- Mark the attendance if output is convincing
- Update the data in the Datatbase

## Tech Used 💻

### Build with

Python 3.10

### Module used

- opencv-python 4.5.4.64
- numpy 1.21.6
- face-recognition 1.3.0
- dlib 19.19.0
- cvzone 1.5.6
- pyrebase 3.0.27

### Editor Used
- PyCharm 2022.2.3

### Frontend
- Streamlit

### Backend
- Firebase (For storing data and user authentication)
