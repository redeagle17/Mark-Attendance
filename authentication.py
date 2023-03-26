import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth

names = ["Murtaza Hassan", "Emily Blunt", "Elon Musk", "Maaz Karim", "Ankur Singh"]
usernames = ["1DS20AI001", "1DS20AI003", "1DS20AI004", "1DS20AI030", "1DS20AI008"]
password = ["******", "******", "******", "******", "******"]

hashed_passwords = stauth.Hasher(password).generate()
file_path = Path(__file__).parent / "hashed_pw.pkl"
with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)