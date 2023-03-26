import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendence-realtime-default-rtdb.firebaseio.com/"
})

ref = db.reference("Students")  # It will create Students directory in the database
data = {
    "1DS20AI001":
        {
            "name": "Murtaza Hassan",
            "major": "Robotics",
            "starting_year": 2020,
            "Course": "Artificial Intelligence and Machine Learning",
            "semester": 6,
            "College": "Dayananda Sagar College of Engineering, Bangalore",
            "ML_attendance": 7,
            "BDA_Attendance": 7,
            "IR_Attendance": 7,
            "DM_Attendance": 7,
            "CC_Attendance": 7,
            "JAVA_Attendance": 7,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1DS20AI003":
        {
            "name": "Emily Blunt",
            "major": "Economics",
            "starting_year": 2020,
            "Course": "Artificial Intelligence and Machine Learning",
            "semester": 6,
            "College": "Dayananda Sagar College of Engineering, Bangalore",
            "ML_attendance": 7,
            "BDA_Attendance": 7,
            "IR_Attendance": 7,
            "DM_Attendance": 7,
            "CC_Attendance": 7,
            "JAVA_Attendance": 7,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1DS20AI004":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "Course": "Artificial Intelligence and Machine Learning",
            "semester": 6,
            "College": "Dayananda Sagar College of Engineering, Bangalore",
            "ML_attendance": 7,
            "BDA_Attendance": 7,
            "IR_Attendance": 7,
            "DM_Attendance": 7,
            "CC_Attendance": 7,
            "JAVA_Attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1DS20AI030":
        {
            "name": "Maaz Karim",
            "major": "NLP",
            "starting_year": 2020,
            "Course": "Artificial Intelligence and Machine Learning",
            "semester": 6,
            "College": "Dayananda Sagar College of Engineering, Bangalore",
            "ML_attendance": 7,
            "BDA_Attendance": 7,
            "IR_Attendance": 7,
            "DM_Attendance": 7,
            "CC_Attendance": 7,
            "JAVA_Attendance": 7,
            "standing": "E",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "1DS20AI008":
        {
            "name": "Ankur Singh",
            "major": "Computer Vision",
            "starting_year": 2020,
            "Course": "Artificial Intelligence and Machine Learning",
            "semester": 6,
            "College": "Dayananda Sagar College of Engineering, Bangalore",
            "ML_attendance": 7,
            "BDA_Attendance": 7,
            "IR_Attendance": 7,
            "DM_Attendance": 7,
            "CC_Attendance": 7,
            "JAVA_Attendance": 7,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)  # Will add data to database
