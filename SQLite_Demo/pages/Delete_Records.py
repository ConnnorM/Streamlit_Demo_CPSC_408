# Imports
# Streamlit: Used to create the front-end GUI
import streamlit as st
# DB_Functions: All of the database CRUD functions and similar stuff go here
from Helpers import DB_Functions

# -----------------------------------------------------------------------------------
# Global Variables
# Set the default configuration for our GUI
st.set_page_config(page_title="CPSC 408 Demo - Delete a Record", layout="wide", page_icon=":heavy_minus_sign:")

# -----------------------------------------------------------------------------------
# Main code
# Page title
st.title("Delete a Record")
# Set default option for which relation in the database to display
choose_relation = 'movies'

# Allow user to select and view relations
st.subheader("Choose a relation to view:", divider='rainbow')
# A drop down menu that allows the user to select one of our three relations to view
choose_relation = st.selectbox(options=st.session_state.relations, label='choose_relation', label_visibility='collapsed')
# Get the selected relation as a dataframe
rel_df = DB_Functions.get_all_records(choose_relation)
# Get the name of the primary key of the relation
rel_id = choose_relation[:-1] + '_ID'
# Display the relation as a dataframe with the primary key as the index
st.dataframe(rel_df.set_index(rel_id))

# Create the delete by ID user input as a form. Keys work the same was as in Javascript/CSS
delete_form = st.form(key='del-form')
# Create a slider that allows the user to select a movie ID. I know this is not very practical,
# but I just wanted to show something cooler than another text_input.
id = delete_form.slider('Which ID would you like to delete?', 
                        min_value=1, 
                        max_value=max(rel_df[rel_id]), 
                        value=1)
# Submit button to save the user inputs are saved and processed below
submit = delete_form.form_submit_button(':red[Delete Entry]')

# When the user clicks the submit button, remove the record and show the generated SQL command
if submit:
    # Use the user input to delete a record from the correct relation
    sql_command = DB_Functions.delete_record_by_ID(choose_relation, id)
    st.write("**Entry Deleted Using the Following SQL Command:**")
    # Display the SQL command that was executed
    st.code(sql_command, language='sql')

    # Output the edited relation
    st.write("%s Relation After Delete Record:" % choose_relation)
    # Get all of the records in the relation as a dataframe
    edited_df = DB_Functions.get_all_records(choose_relation)
    # Display the relation as a dataframe with the primary key as the index
    st.dataframe(edited_df.set_index(rel_id))

# -----------------------------------------------------------------------------------
# CSS File Import
with open('./Helpers/CSS_Stuff.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)