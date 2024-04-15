# Imports
# Streamlit: Used to create the front-end GUI
import streamlit as st
# DB_Functions: All of the database CRUD functions and similar stuff go here
from Helpers import DB_Functions

# -----------------------------------------------------------------------------------
# Global Variables
# Set the default configuration for our GUI
st.set_page_config(page_title="CPSC 408 Demo - Write a Review", layout="wide", page_icon=":heavy_plus_sign:")

# -----------------------------------------------------------------------------------
# Main code
# Page title
st.title("Write a Review")

# Get all of the movies as a dataframe
movie_df = DB_Functions.get_all_records('movies')
# Show only the movie_ID and title columns, and set the index to be the primary key
st.dataframe(movie_df[['movie_ID', 'title']].set_index('movie_ID'))

# Create the write a review form. Keys work the same way as they do in Javascript/CSS.
review_form = st.form(key='rev-form')
# Create a text entry widget and save the value into the user name variable
uname = review_form.text_input(label='User Name:')
# Create a number input and save the user's input as the movie ID
m_id = int(review_form.number_input(label='Movie\'s ID:',
                                min_value=1,
                                max_value=max(movie_df['movie_ID'])))
# Create a number input and save the user's input as the movie's score by the user
scr = int(review_form.number_input(label='Score (0-100):',
                               min_value=0,
                               max_value=100,
                               ))
# Create a text entry widget and save the value into the review text variable
rvw_txt = review_form.text_input(label='Write Your Review:')
# When this button is clicked, the values in the form will be saved
submit = review_form.form_submit_button(':blue[Submit Review]')

# When the user submits, remove the record and show the generated SQL command
if submit:
    # Add the inputs from the form as a new review to our reviews relation
    sql_command = DB_Functions.add_record_reviews(uname, m_id, scr, rvw_txt)
    st.write("**Review Added Using the Following SQL Command:**")
    # Display the SQL command that was executed
    st.code(sql_command, language='sql')

    # Get the updated relation as a dataframe
    new_df = DB_Functions.get_all_records('reviews')
    # Display the relation as a dataframe with the primary key as the index
    st.dataframe(new_df.set_index('review_ID'))

# -----------------------------------------------------------------------------------
# CSS File Import
with open('./Helpers/CSS_Stuff.css') as f:
    css = f.read()

st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)