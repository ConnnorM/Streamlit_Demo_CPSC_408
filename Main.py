# Imports
# Streamlit: Used to create the front-end GUI
import streamlit as st
# SQLAlchemy: Some back-end nonsense that helps Streamlit talk to SQLite
from sqlalchemy import text

# -----------------------------------------------------------------------------------
# Global Variables
# Set the default configuration for our GUI
st.set_page_config(page_title="CPSC 408 Demo", layout="wide", page_icon=":wave:")
# Create the SQL connection to movie_reviews_db as specified in your secrets file.
conn = st.connection('movie_reviews_db', type='sql')
# Add the SQL connection to the Streamlit session state so we can access it from any page
if 'conn' not in st.session_state:
    st.session_state.conn = conn
# -----------------------------------------------------------------------------------
# Functions
# initialize_movies_table: Create the movies table and assign default entries.
# Takes in conn.session
@st.cache_data
def initialize_movies_table():
    # Create the table and put constraints on attributes
    # Not entirely sure why, but if you don't use the 'with' keyword to lump all of the conn.session functions
    # and handle resource management, queries won't close and the database will remain locked forever 
    with conn.session as s:
        s.execute(text(
            '''
            CREATE TABLE IF NOT EXISTS movies(
                movie_ID INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
                title TEXT NOT NULL,
                runtime INTEGER,
                budget INTEGER,
                critic_score INTEGER,
                genre TEXT,
                p_safe_rating TEXT
            );
            '''
        ))
        # Remove any records that already exist
        s.execute(text(
            '''
            DELETE FROM movies;
            '''
            )
        )
        # Create initial dataset
        movies = {'The LEGO Movie': [1, 100, 1000000, 100, 'Action/Comedy', 'P Safe Approved'],
                'Kung Fu Panda 4': [2, 95, 2000000, 45, 'Action/Comedy', 'P Safe Approved'],
                'Whiplash': [3, 120, 500000, 88, 'Drama', 'P Safe Not Approved'],
                'Iron Man 15': [4, 117, 234567890, 62, 'Action/Comedy', 'P Safe Approved'],
                'Healthy Panther Documentary': [5, 35, 10, 50, 'Documentary', 'P Safe Loves This Movie']}
        
        # Load inital dataset into table
        for m in movies:
            s.execute(text(
                '''
                INSERT INTO movies (movie_ID, title, runtime, budget, critic_score, genre, p_safe_rating)
                VALUES (%d, '%s', %d, %d, %d, '%s', '%s');
                ''' % (movies[m][0], m, movies[m][1], movies[m][2], movies[m][3], movies[m][4], movies[m][5],)
                )
            )

        # Commit the operations
        s.commit()

# query: Takes the connection session, and the relation and returns the relation as a dataframe
def get_all_records(relation):
    df = conn.query(
        '''
        SELECT *
        FROM %s;
        ''' % relation
    )

    return df

# -----------------------------------------------------------------------------------
# Main code
# Create the movies table with default entries
initialize_movies_table()

# Get the movies table as a dataframe
movies_df = get_all_records('movies')

st.write("Movies:")
st.dataframe(movies_df.set_index('movie_ID'))