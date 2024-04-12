# Imports
# Streamlit: Used to create the front-end GUI
import streamlit as st
# DB_Functions: All of the database CRUD functions and similar stuff go here
from Helpers import DB_Functions

# -----------------------------------------------------------------------------------
# Global Variables
# Set the default configuration for our GUI
st.set_page_config(page_title="CPSC 408 Demo - View Relations", layout="wide", page_icon=":open_file_folder:")

# -----------------------------------------------------------------------------------
# Main code
# Title of the page
st.title("View Relations")
# Drop down menu that lets you choose which relation to view
choose_relation = st.selectbox(options=st.session_state.relations,
                               label='Choose a relation to view')
# Display the chosen relation as a dataframe
df = DB_Functions.get_all_records(choose_relation)
# Get the name of this relation's primary key
rel_id = choose_relation[:-1] + '_ID'
# Set the index to be equal to the primary key of the relation
st.dataframe(df.set_index(rel_id))

# Goofy stuff
st.subheader("OMG WOWIE SO COOL! But how hard was that..?", divider='rainbow')
# If the button is pressed, then do the following code:
if st.button(":green[Show Me the Code!]"):
    c1 = '''
    st.title("View Relations")
    choose_relation = st.selectbox(options=st.session_state.relations, label='Choose a relation to view')
    df = DB_Functions.get_all_records(choose_relation)
    st.dataframe(df.set_index('movie_ID'))
    '''
    # Code block with python syntax and line numbers are displayed!
    st.code(c1, language='python', line_numbers=True)
    st.subheader("Only 4 lines of code??? :shocked_face_with_exploding_head:")