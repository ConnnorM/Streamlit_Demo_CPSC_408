# Streamlit_Demo_CPSC_408
- A demo of Streamlit for the CPSC 408 final project
## TODO:
- then do a demo of creating a basic output from scratch just reading in a csv or something
    - point is to show how easy it is
    - run through columns, tabs, layout options, css, dataframes, quickly show session_state and add a page, cache data, emojis, sort df by clicking, dividers and headers, auto rerun feature, darkmode last lol, html/css render html,
## Things to Teach/Say:
- It's just a python library. Which means basically anything you can do in python can be integrated with Streamlit
- specifically designed to do data viz and dashboards
- Brief intro to session state and cache_data/resource
- On changes, it reruns the page from top to bottom d
- https://docs.streamlit.io/develop/concepts/connections/connecting-to-data
- current setup doesn't keep the database as a universal source of truth for all users since it's sqlite not mysql server
- doesn't work with notebooks, needs to be a regular python file (.py)