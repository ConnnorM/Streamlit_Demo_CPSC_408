# Imports
# Streamlit: Used to create the front-end GUI
import streamlit as st
# DB_Functions: All of the database CRUD functions and similar stuff go here
from Helpers import DB_Functions
# sqlite3: SQLite is the DBMS we are using for this demo
import sqlite3

# -----------------------------------------------------------------------------------
# Global Variables
# Set the default configuration for our GUI
st.set_page_config(page_title="CPSC 408 Demo", layout="wide", page_icon=":wave:")
# Create the SQL connection to movie_reviews_db
conn = sqlite3.connect("movie_reviews_db.db", check_same_thread=False)
c = conn.cursor()
# Add the SQL connection to the Streamlit session state so that we can access it from any page or file.
# Session state is a very important concept for Streamlit. If you save objects, variables, etc. into
# the session state, you can access those objects (and change them) from any page in your app.
# If an object is not in the session state, it cannot be seen by other pages in the app.
# Read more here: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
if 'conn' not in st.session_state:
    st.session_state.conn = conn
    st.session_state.c = c
    st.session_state.relations = ['movies', 'reviews', 'studios']

# -----------------------------------------------------------------------------------
# Main code
# Create the different tables with default entries
DB_Functions.initialize_movies_table()
DB_Functions.initialize_reviews_table()
DB_Functions.initialize_studios_table()

# -----------------------------------------------------------------------------------
# GUI code
# Page title
st.title("CPSC 408 Streamlit Demo with SQLite")
# Header with rainbow colored divider below
st.header("Example Final Project: Movies Database", divider='rainbow')
# Subheader with red divider. P.S. You can use emojis anywhere! Here's a handy list of all of the emoji
# shortcodes for Streamlit: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.subheader("Main Page :sunglasses:", divider="red")
st.write("This page loads first! It creates the connection to the SQLite database and initializes our tables.")
c1 = '''
    conn = sqlite3.connect("movie_reviews_db.db", check_same_thread=False)
    c = conn.cursor()
    with conn:
        c.execute(
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
        )
        conn.commit()
    '''
# Display a code block in whatever language!
st.code(c1, language='python')
# Another subheader followed by a blue divider line
st.subheader("Now What?", divider="blue")
st.write("Click on a page in the sidebar to the left to see the SQL demos.")
