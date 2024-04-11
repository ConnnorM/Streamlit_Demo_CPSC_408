# Imports
# Streamlit: Used to create the front-end GUI
import streamlit as st
# SQLAlchemy: Some back-end nonsense that helps Streamlit talk to SQLite
from sqlalchemy import text
# DB_Functions: All of the database CRUD functions and similar stuff goes here
from Helpers import DB_Functions

# -----------------------------------------------------------------------------------
# Global Variables
# Set the default configuration for our GUI
st.set_page_config(page_title="CPSC 408 Demo", layout="wide", page_icon=":wave:")
# Create the SQL connection to movie_reviews_db as specified in your secrets file.
conn = st.connection('movie_reviews_db', type='sql')
# Add the SQL connection to the Streamlit session state so we can access it from any page
if 'conn' not in st.session_state:
    st.session_state.conn = conn
    st.session_state.relations = ['movies', 'reviews', 'studios']

# -----------------------------------------------------------------------------------
# Functions

# -----------------------------------------------------------------------------------
# Main code
# Create the different table with default entries
DB_Functions.initialize_movies_table()
DB_Functions.initialize_reviews_table()
DB_Functions.initialize_studios_table()

# -----------------------------------------------------------------------------------
# GUI code
st.title("CPSC 408 Streamlit Demo with SQLite")
st.header("Example Final Project: Movies Database", divider='rainbow')
st.subheader("Main Page :sunglasses:", divider="red")
st.write("This page loads first! It creates the connection to the SQLite database and initializes our tables.")
c1 = '''
    conn = st.connection('movie_reviews_db', type='sql')
    with conn.session as s:
        s.execute(text(
            \'\'\'
            CREATE TABLE IF NOT EXISTS movies(
                movie_ID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                title TEXT NOT NULL,
                runtime INTEGER,
                budget INTEGER,
                studio_ID INTEGER NOT NULL,
                critic_score INTEGER,
                genre TEXT,
                p_safe_rating TEXT
            );
            \'\'\'
        ))
'''
st.code(c1, language='python')
st.caption("See st.connection in the first line? Streamlit even has a built-in function to help you connect to different databases!")
st.subheader("Now What?", divider="blue")
st.write("Click on a page in the sidebar to the left to see the SQL demos.")
