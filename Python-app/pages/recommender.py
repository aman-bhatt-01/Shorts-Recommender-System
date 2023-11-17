import streamlit as st
from streamlit_player import st_player
import os
import pickle
import pandas as pd

shorts_dict = pickle.load(open('shorts_dict.pkl', 'rb'))
shorts = pd.DataFrame(shorts_dict)

if 'clicked' not in st.session_state:
    st.session_state.clicked = 0

def click_button():
    st.session_state.clicked += 1
    st.session_state.clicked %= len(st.session_state.recommended)


st_player('https://www.youtube.com/watch?v={}'.format(st.session_state.recommended[st.session_state.clicked]))

st.button('Next Video', on_click=click_button)
