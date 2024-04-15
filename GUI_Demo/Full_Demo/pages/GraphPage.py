import streamlit as st

st.set_page_config(page_title="CPSC 408 Chart Page", layout="wide", page_icon=":chart_with_upwards_trend:")

st.title(":orange[A Graph :o]")

y_axis = st.selectbox(options=['Rotten Tomatoes %',
                               'Year'],
                      label="**Select the Y axis**")

st.scatter_chart(data=st.session_state.movies_df,
                 x="Film",
                 y=y_axis,
                 size="Worldwide Gross",
                 color="Genre")