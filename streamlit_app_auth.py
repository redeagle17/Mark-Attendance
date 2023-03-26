import pyrebase
import streamlit as st
from requests.exceptions import HTTPError
from streamlit_option_menu import option_menu
import cv2
import numpy as np
from home import home_data

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

firebaseConfig = {
    'apiKey': "AIzaSyA34cyeD3V8QvHqQTPcJ__Up4uMiwJyisE",
    'authDomain': "face-attendence-realtime.firebaseapp.com",
    'databaseURL': "https://face-attendence-realtime-default-rtdb.firebaseio.com",
    'projectId': "face-attendence-realtime",
    'storageBucket': "face-attendence-realtime.appspot.com",
    'messagingSenderId': "71061322824",
    'appId': "1:71061322824:web:5c8ca66e1720d0c6a12c7d",
    'measurementId': "G-58JJEMKNQT"
}


studentDetail = {}
# Firebase authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage()

st.sidebar.title("MARK ATTENDANCE")

choice = st.sidebar.selectbox('Signup/Login', ['Sign up', 'Login'])
email = st.sidebar.text_input('Enter your Email')
password = st.sidebar.text_input('Enter your Password', type="password")

if choice == 'Sign up':
    usn = st.sidebar.text_input('Enter your USN')
    submit = st.sidebar.button('Create Account')
    if submit:
        user = auth.create_user_with_email_and_password(email, password)
        st.sidebar.text('Account created Successfully')
        st.balloons()

        user = auth.sign_in_with_email_and_password(email, password)
        st.title('Hey, ' + usn)
        st.info('Login to proceed further!')

if choice == 'Login':
    usn = st.sidebar.text_input('Enter your USN')
    submit = st.sidebar.button('Login')
    if "load_state" not in st.session_state:
        st.session_state.load_state = False
    if submit or st.session_state.load_state:
        try:
            st.session_state.load_state = True
            selected = option_menu(
                menu_title=None,
                options=["Home", "Info", "Time Table", "Examination", "Logout"],
                icons=["house", "info-square", "calendar", "border-all", "box-arrow-right"],
                menu_icon="cast",
                default_index=0,
                orientation="horizontal"
            )
            if selected == 'Home':
                user = auth.sign_in_with_email_and_password(email, password)
                studentDetail = db.child(f'Students/{usn}').get()
                display_image = cv2.imread(f'Images/{usn}.png')
                hh, ww = display_image.shape[:2]
                hh2 = hh // 2
                ww2 = ww // 2
                radius2 = 105
                xc = hh // 2
                yc = ww // 2
                mask2 = np.zeros_like(display_image)
                mask2 = cv2.circle(mask2, (xc, yc), radius2, (255, 255, 255), -1)
                result = cv2.cvtColor(display_image, cv2.COLOR_BGR2RGBA)
                result[:, :, 3] = mask2[:, :, 0]
                home_data(studentDetail, result, usn)

            elif selected == 'Info':
                studentDetail = db.child(f'Students/{usn}').get()
                st.markdown("**COURSE**")
                st.write("B.E in "+studentDetail.val()['Course'])
                st.markdown("**SEMESTER**")
                st.write("Currently in "+str(studentDetail.val()['semester'])+"th Semester")
                st.markdown("**COLLEGE**")
                st.write(studentDetail.val()['College'])

            elif selected == 'Time Table':
                st.title("Time table")
            elif selected == "Examination":
                st.title("Examination")

        except HTTPError:
            st.warning("Email/Password Incorrect")
