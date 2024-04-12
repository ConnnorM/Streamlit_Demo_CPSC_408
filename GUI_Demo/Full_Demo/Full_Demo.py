import streamlit as st
import pandas as pd

if 'slider_val' not in st.session_state:
    st.session_state.slider_val = 50

if 'movies_df' not in st.session_state:
    st.session_state.movies_df = pd.read_csv('movies.csv')

st.set_page_config(page_title="CPSC 408 GUI Demo", layout="wide", page_icon=":volcano:")

st.title("Demo Page")

st.subheader("Next Section :point_down:", divider='rainbow')

st.dataframe(st.session_state.movies_df, use_container_width=True)

button_col, radio_col, slider_col = st.columns([0.2, 0.2, 0.6])

with button_col:
    no_click = st.button(label=":red[**Don't click on me or else >:(**]")

    if no_click:
        st.write("Ow that hurt")

with radio_col:
    t1, t2, t3 = st.tabs(["Prof", "Dog", "Class"])
    with t1:
        radio = st.radio(label='**Pick the coolest professor**',
            options=['Sandie', 'Sierra', 'Whoever is Next Door Right Now'],
            index=1) 
    with t2:
        radio = st.radio(label='**Pick the furriest dog**',
            options=['Sandie', 'Luna', 'Jerry price'],
            index=1) 
    with t3:
        radio = st.radio(label='**Pick the classroom**',
            options=['123', '233', '333'],
            index=1) 


with slider_col:
    slider_val = st.slider(label="**Pick a number!**",
                   min_value=0,
                   max_value=100,
                   value=st.session_state.slider_val)
    st.write("You picked this value: %s" % slider_val)
    st.session_state.slider_val = slider_val


