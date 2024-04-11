# Imports
# Streamlit: Used to create the front-end GUI
import streamlit as st
# DB_Functions: All of the database CRUD functions and similar stuff goes here
from Helpers import DB_Functions

# -----------------------------------------------------------------------------------
# Global Variables
# Set the default configuration for our GUI
st.set_page_config(page_title="CPSC 408 Demo - Delete a Record", layout="wide", page_icon=":heavy_minus_sign:")

# -----------------------------------------------------------------------------------
# Functions

# -----------------------------------------------------------------------------------
# Main code
st.title("Delete a Record")

# Set default option
choose_relation = 'movies'

# Allow user to select and view relations
st.subheader("Choose a relation to view:", divider='rainbow')
choose_relation = st.selectbox(options=st.session_state.relations, label='choose_relation', label_visibility='collapsed')
rel_df = DB_Functions.get_all_records(choose_relation)
rel_id = choose_relation[:-1] + '_ID'
st.dataframe(rel_df.set_index(rel_id))

# Create the delete by ID options as a form
delete_form = st.form(key='del-form')
id = delete_form.slider('Which ID would you like to delete?', 1, len(rel_df), 1)
submit = delete_form.form_submit_button(':red[Delete Entry]')

# When the user submits, remove the record and show the generated SQL command
if submit:
    sql_command = DB_Functions.delete_record_by_ID(choose_relation, id)
    st.write("**Entry Deleted Using the Following SQL Command:**")
    st.code(sql_command, language='sql')

# output edited relation
st.dataframe(DB_Functions.get_all_records('movies'))