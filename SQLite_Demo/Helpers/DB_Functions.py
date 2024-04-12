# DB_Functions: All of the database CRUD functions and similar stuff goes here

# Imports
# Streamlit: Used to create the front-end GUI
import streamlit as st
# Pandas: Allows you to use dataframes as a data structure
import pandas as pd

# -----------------------------------------------------------------------------------
# Functions
# initialize_movies_table: Create the movies table and assign default entries. This function only runs
# when you first start the app thanks to the st.cache_data decorator.
@st.cache_data
def initialize_movies_table():
    # Using the with keyword for resource management makes things nicer. You don't have to do it this way
    with st.session_state.conn:
        # Create the table and put constraints on attributes
        st.session_state.c.execute(
            '''
            CREATE TABLE IF NOT EXISTS movies(
                movie_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                runtime INTEGER,
                budget INTEGER,
                studio_ID INTEGER NOT NULL,
                critic_score INTEGER,
                genre TEXT,
                p_safe_rating TEXT
            );
            '''
        )
        # Remove any records that already exist. Only doing this so that the demo runs the same
        # way every time.
        st.session_state.c.execute(
            '''
            DELETE FROM movies;
            '''
        )
        # Create initial dataset
        movies = {'The LEGO Movie': [1, 100, 1000000, 1, 100, 'Action/Comedy', 'P Safe Approved'],
                'Kung Fu Panda 4': [2, 95, 2000000, 2, 45, 'Action/Comedy', 'P Safe Approved'],
                'Whiplash': [3, 120, 500000, 2, 88, 'Drama', 'P Safe Not Approved'],
                'Iron Man 15': [4, 117, 234567890, 1, 62, 'Action/Comedy', 'P Safe Approved'],
                'Healthy Panther Documentary': [5, 35, 10, 3, 50, 'Documentary', 'P Safe Loves This Movie']}
        
        # Load inital dataset into table
        for m in movies:
            st.session_state.c.execute(
                '''
                INSERT INTO movies (movie_ID, title, runtime, budget, studio_ID, critic_score, genre, p_safe_rating)
                VALUES (%d, '%s', %d, %d, %d, %d, '%s', '%s');
                ''' % (movies[m][0], m, movies[m][1], movies[m][2], movies[m][3], movies[m][4], movies[m][5], movies[m][6])
            )

        # Commit the operations
        st.session_state.conn.commit()

# initialize_reviews_table: Create the reviews table and assign default entries. This function only runs
# when you first start the app thanks to the st.cache_data decorator
@st.cache_data
def initialize_reviews_table():
    # Using the with keyword for resource management makes things nicer. You don't have to do it this way
    with st.session_state.conn:
        # Create the table and put constraints on attributes
        st.session_state.c.execute(
            '''
            CREATE TABLE IF NOT EXISTS reviews(
                review_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                movie_ID INTEGER NOT NULL,
                score INTEGER,
                review_text TEXT
            );
            '''
        )
        # Remove any records that already exist. Only doing this so that the demo runs the same
        # way every time.
        st.session_state.c.execute(
            '''
            DELETE FROM reviews;
            '''
        )
        # Create initial dataset
        reviews = {1: ['SQL_Lover_444', 1, 100, "'Wow everything really is awesome when youre part of a team'"],
                2: ['Definitely_Not_Sierra123456', 3, 95, "'Go little drummer boi go'"],
                3: ['GuyInThe3rdRow4thSeatFromTheRight', 1, 31, "'I hate legos >:('"]}
        
        # Load inital dataset into table
        for r in reviews:
            st.session_state.c.execute(
                '''
                INSERT INTO reviews (review_ID, username, movie_ID, score, review_text)
                VALUES (%d, '%s', %d, %d, %s);
                ''' % (r, reviews[r][0], reviews[r][1], reviews[r][2], reviews[r][3])
            )

        # Commit the operations
        st.session_state.conn.commit()

# initialize_studios_table: Create the studios table and assign default entries. This function only runs
# when you first start the app thanks to the st.cache_data decorator.
@st.cache_data
def initialize_studios_table():
    # Using the with keyword for resource management makes things nicer. You don't have to do it this way
    with st.session_state.conn:
        # Create the table and put constraints on attributes 
        st.session_state.c.execute(
            '''
            CREATE TABLE IF NOT EXISTS studios(
                studio_ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                location TEXT
            );
            '''
        )
        # Remove any records that already exist. Only doing this so that the demo runs the same
        # way every time.
        st.session_state.c.execute(
            '''
            DELETE FROM studios;
            '''
        )
        # Create initial dataset
        studios = {1: ['Cool Movie Studio', "'Disneyland, California'"],
                2: ['Yet Another Movie Studio', "'Go little drummer boi go'"],
                3: ['Dodge Kids are So Cool OMG INC.', "'Top Secret Dodge Facility (that one warehouse across the street)'"]}
        
        # Load inital dataset into table
        for stu in studios:
            st.session_state.c.execute(
                '''
                INSERT INTO studios (studio_ID, name, location)
                VALUES (%d, '%s', %s);
                ''' % (stu, studios[stu][0], studios[stu][1])
            )

        # Commit the operations
        st.session_state.conn.commit()

# get_all_records: Takes in a relation's name and returns the relation as a dataframe
def get_all_records(relation):
    query = st.session_state.c.execute(
        '''
        SELECT *
        FROM %s;
            ''' % relation
    )

    # Get a list of column names from the relation
    cols = [column[0] for column in query.description]
    # Use the column names list and the query.fetchall()'s output (tuples) to make a dataframe and return it
    return pd.DataFrame.from_records(data = query.fetchall(), columns = cols)

# delete_record: pass in a relation and an ID to remove. Returns the SQL command it executed
def delete_record_by_ID(relation, remove_id):
    with st.session_state.conn:
        rel_id = relation[:-1] + '_ID'
        # SQL Command
        command = '''
            DELETE FROM %s
            WHERE %s = %d;
            ''' % (relation, rel_id, remove_id)
        
        
        st.session_state.c.execute(command)
        # Commit the operation
        st.session_state.conn.commit()
    # Return the SQL command as a string
    return command

# add_record_reviews: pass in the attributes of the review and update the reviews relation.
# Returns the SQL command it executed.
def add_record_reviews(uname, m_ID, scr, rvw_txt):
    with st.session_state.conn:
        # SQL Command
        command = '''
            INSERT INTO reviews(username, movie_ID, score, review_text)
            VALUES('%s',%d,%d,'%s');
            ''' % (uname, m_ID, scr, rvw_txt)
        
        st.session_state.c.execute(command)
        # Commit the operation
        st.session_state.conn.commit()
    # Return the SQL command as a string
    return command