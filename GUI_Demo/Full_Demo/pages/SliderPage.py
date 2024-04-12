import streamlit as st

st.set_page_config(page_title="CPSC 408 Demo Slider Page", layout="wide", page_icon=":egg:")

st.title("Wow a Slider!")

slider_val = st.slider(label="**Pick a number!**",
                   min_value=0,
                   max_value=100,
                   value=st.session_state.slider_val)

st.write("You picked this value: %s" % slider_val)

st.session_state.slider_val = slider_val
