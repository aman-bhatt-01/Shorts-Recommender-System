import streamlit as st
from streamlit_player import st_player
import numpy as np
import os
import pickle
import pandas as pd
import random

if 'recommended' not in st.session_state:
    st.session_state.recommended = []
if 'recommendedtitle' not in st.session_state:
    st.session_state.recommendedtitle = []


def recommend(shorts_id):
    shorts_index = shorts[shorts['id'] == shorts_id].index[0]
    distances = similarity[shorts_index]
    shorts_id_list = sorted(list(enumerate(distances)), reverse =True, key = lambda x: x[1])[1:10]
    for i in shorts_id_list:
        st.session_state.recommended.append(shorts.iloc[i[0]].id)
        st.session_state.recommendedtitle.append("".join(shorts.iloc[i[0]].title))


similarity = pickle.load(open('similarity.pkl', 'rb'))
shorts_dict = pickle.load(open('shorts_dict.pkl', 'rb'))
shorts = pd.DataFrame(shorts_dict)


if 'change' not in st.session_state:
    st.session_state.change = random.randint(0, len(shorts)-1)

def click():
    st.session_state.change = random.randint(0, len(shorts)-1)

def click_button():
    recommend(selected)
    click()

st.title('Recommender System')
# selected = st.selectbox(
#     'Select a movie', movies['title'].values
# )
selected = shorts.iloc[st.session_state.change].id

st_player('https://www.youtube.com/watch?v={}'.format(selected))
st.header(selected)


st.button('Recommend', on_click=click_button)
st.button('Not Interested', on_click=click)
st.divider()

#
# st.session_state.recommended = list(np.unique(st.session_state.recommended))

# st.title('Recommender System')
# selected = st.selectbox(
#     'Select a movie', movies['title'].values
# )
#

if st.button('show recommended titles'):
    for i in st.session_state.recommendedtitle:
        st.write(i, " ")


# st.session_state.recommended = ['kU88ow3-FSA', 'I842dLvaN7c', '9F85jQQmQCw', 'LqSR4Q7h7JE', 'sOgcM3t9v7A']



# st.button('Next Video', on_click=click_button)
