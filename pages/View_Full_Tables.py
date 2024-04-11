# Imports
# Streamlit: Used to create the front-end GUI
import streamlit as st
# DB_Functions: All of the database CRUD functions and similar stuff goes here
from Helpers import DB_Functions

# -----------------------------------------------------------------------------------
# Global Variables
# Set the default configuration for our GUI
st.set_page_config(page_title="CPSC 408 Demo - View Relations", layout="wide", page_icon=":open_file_folder:")

# -----------------------------------------------------------------------------------
# Functions

# -----------------------------------------------------------------------------------
# Main code
st.title("View Relations")
choose_relation = st.selectbox(options=st.session_state.relations,
                               label='Choose a relation to view')
# Display the chosen relation
df = DB_Functions.get_all_records(choose_relation)
rel_id = choose_relation[:-1] + '_ID'
st.dataframe(df.set_index(rel_id))

# Fun stuff
st.subheader("OMG WOWIE SO COOL! But how hard was that..?", divider='rainbow')
if st.button(":green[Show Me the Code!]"):
    c1 = '''
    st.title("View Relations")
    choose_relation = st.selectbox(options=st.session_state.relations, label='Choose a relation to view')
    df = DB_Functions.get_all_records(choose_relation)
    st.dataframe(df.set_index('movie_ID'))
    '''
    st.code(c1, language='python', line_numbers=True)
    st.subheader("Only 4 lines of code??? :shocked_face_with_exploding_head:")