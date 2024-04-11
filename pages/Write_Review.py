# Imports
# Streamlit: Used to create the front-end GUI
import streamlit as st
# DB_Functions: All of the database CRUD functions and similar stuff goes here
from Helpers import DB_Functions

# -----------------------------------------------------------------------------------
# Global Variables
# Set the default configuration for our GUI
st.set_page_config(page_title="CPSC 408 Demo - Write a Review", layout="wide", page_icon=":heavy_plus_sign:")

# -----------------------------------------------------------------------------------
# Functions

# -----------------------------------------------------------------------------------
# Main code
st.title("Write a Review")

movie_df = DB_Functions.get_all_records('movies')
st.dataframe(movie_df[['movie_ID', 'title']].set_index('movie_ID'))

# Create the write a review form
review_form = st.form(key='rev-form')
uname = review_form.text_input(label='User Name:')
m_id = int(review_form.number_input(label='Movie\'s ID:',
                                min_value=1,
                                max_value=len(movie_df)))
scr = int(review_form.number_input(label='Score (0-100):',
                               min_value=0,
                               max_value=100,
                               ))
rvw_txt = review_form.text_input(label='Write Your Review:')
submit = review_form.form_submit_button(':blue[Submit Review]')

# When the user submits, remove the record and show the generated SQL command
if submit:
    sql_command = DB_Functions.add_record_reviews(uname, m_id, scr, rvw_txt)
    st.write("**Review Added Using the Following SQL Command:**")
    st.code(sql_command, language='sql')

# output edited relation
st.dataframe(DB_Functions.get_all_records('reviews'))