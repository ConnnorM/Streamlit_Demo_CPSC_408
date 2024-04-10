# Streamlit_Demo_CPSC_408
- A demo of Streamlit for CPSC 408 final project
## TODO:
- Make simple version of our movies database that works like the final project
    - movies, reviews, studio
- Connect to sql server and show that it's easy
- Show html/css options for the nerds
    - Search 'render html' in api
- has Auth0 plugin to make sierra mad
- has its own secrets file for database login
- write guide on how to connect sqlite to streamlit and make the connection
    - include secrets.toml, requirements.txt, 
## Things to Teach/Say:
- It's just a python library. Which means basically anything you can do in python can be integrated with Streamlit
- specifically designed to do data viz and dashboards
- Brief intro to session state and cache_data/resource
- On changes, it reruns the page from top to bottom d
- https://docs.streamlit.io/develop/concepts/connections/connecting-to-data
- current setup doesn't keep the database as a universal source of truth for all users since it's sqlite not mysql server
- doesn't work with notebooks, needs to be a regular python file (.py)