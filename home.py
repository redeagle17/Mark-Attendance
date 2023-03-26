import streamlit as st
from main import mark_attendance_of_student


def home_data(studentDetail, result, usn):
    detail = studentDetail.val()
    name = detail['name']
    st.image(result)
    st.title(f'Hey, **{name}** ({usn})')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('**Core Java**')
        JAVA = st.button("Java Attendance")
        if JAVA:
            mark_attendance_of_student(usn, 'JAVA_Attendance', studentDetail)
    with col2:
        st.markdown('**Machine Learning**')
        ML = st.button("ML Attendance")
        if ML:
            mark_attendance_of_student(usn, 'ML_attendance', studentDetail)
    with col3:
        st.markdown('**Big Data Analytics**')
        BDA = st.button("BDA Attendance")
        if BDA:
            mark_attendance_of_student(usn, 'BDA_Attendance', studentDetail)

    col4, col5, col6 = st.columns(3)
    with col4:
        st.markdown('**Intro to Robotics**')
        IR = st.button("IR Attendance")
        if IR:
            mark_attendance_of_student(usn, 'IR_Attendance', studentDetail)
    with col5:
        st.markdown('**Data Mining**')
        DM = st.button(" DM Attendance")
        if DM:
            mark_attendance_of_student(usn, 'DM_Attendance', studentDetail)
    with col6:
        st.markdown('**Cloud Computing**')
        CC = st.button("CC Attendance")
        if CC:
            mark_attendance_of_student(usn, 'CC_Attendance', studentDetail)
