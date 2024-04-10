# Imports
# Streamlit: Used to create the front-end GUI
import streamlit as st
# SQLAlchemy: Some back-end nonsense that helps Streamlit talk to SQLite
from sqlalchemy import text

# -----------------------------------------------------------------------------------
# Global Variables
# Set the default configuration for our GUI
st.set_page_config(page_title="CPSC 408 Demo", layout="wide", page_icon=":wave:")

# -----------------------------------------------------------------------------------
# Functions

# -----------------------------------------------------------------------------------
# Main code
# Create the SQL connection to pets_db as specified in your secrets file.
conn = st.connection('pets_db', type='sql')

st.write(conn)

# Insert some data with conn.session.
with conn.session as s:
    s.execute(text('''CREATE TABLE IF NOT EXISTS pet_owners (person TEXT, pet TEXT);'''))
    s.execute(text('''DELETE FROM pet_owners;'''))
    pet_owners = {'jerry': 'fish', 'barbara': 'cat', 'alex': 'puppy'}
    for k in pet_owners:
        s.execute(text(
            '''INSERT INTO pet_owners (person, pet) VALUES (:owner, :pet);'''),
            params=dict(owner=k, pet=pet_owners[k])
        )
    s.commit()
    st.write(s)

# # Query and display the data you inserted
pet_owners = conn.query('''
                        select * from pet_owners
                        ''')
st.dataframe(pet_owners)