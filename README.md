# Streamlit_Demo_CPSC_408
- A demo of Streamlit for the CPSC 408 final project
## Run the SQL Demo:
- Install the Python dependencies
    - Open the cloned repository in a terminal and type the following command:
        - pip install -r requirements.txt
- Run the demo:
    - Open the SQLite_Demo folder in a terminal and type the following command:
        - streamlit run Main.py
    - The demo will open in your browser and is hosted locally on your computer

## Run the GUI Demo:
- Open the GUI_Demo folder in a terminal and type the following command:
    - streamlit run Demo.py

## Streamlit Learning Resources:
- Basic Concepts of How Streamlit Works: https://docs.streamlit.io/get-started/fundamentals/main-concepts
- API Home Page: https://docs.streamlit.io/develop/api-reference
- How to Use Session State: https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state
- Create Multi-Page Apps: https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app
- Deploying App to the Web: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app
    - NOTE: Streamlit Cloud supports up to Python 3.9. This isn't a huge deal, but you can't do certain things if they were added in a later version of Python (for example, switch statements were added in Python 3.10. So, if your app is only running locally, you can use switch statements if your Python version is 3.10+. However, if you're running the app in the cloud,
    you'll get complier errors since that syntax doesn't exist in Python 3.9.)
- Emoji Shortcodes: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

## Talking Points for Live Demo of This App:
- Streamlit is a Python library; anything you can do in Python can be integrated with Streamlit
- Basically everything in Streamlit is one simple function call
- Specifically designed to make data dashboards (visualiations) that are accessible to non-technical people
    - For example, one of the super cool features of Streamlit is the ability to run machine learning models inside your app and allow the user to change parameters of the model within the GUI and rerun that model to see the results.
- When you change something in your GUI, it reruns that page's Python file from the top down.
    - Mention cache_data/resource here.
- Streamlit has a connection object, but I would recommend connecting to your database in the databases' native process.
    - The Streamlit connection object is a weird wrapper thing that's supposed to make it easy to connect to data, but I don't think it actually makes anything easier. It just adds more potential failure points.
        - For example, just use the SQLite3 library that's built in to Python instead of using streamlit.connection() to create a SQL connection.
- You cannot use Streamlit with notebook files (.ipynb); you have to use a regular Python file (.py).

## Streamlit Functions to Show Off in From-Scratch Demo:
- Title
- Subheader/Divider
- Emojis
- Dataframes
- Rerun and Auto-Rerun
- Buttons, Text Input, Sliders, etc.
- Columns/Tabs/Layout Options
- Multiple Pages
    - Page Config
- Session State
- Chart
- HTML/CSS Customization
    - Search Render HTML
- Dark Mode