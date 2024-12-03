import streamlit as st

st.title("Learning Streamlit")
st.write("... for the first time")

st.header("Checkbox")

agree = st.checkbox("Do you accept the terms?")

if agree:
    st.write("Great!")


st.header("Radiobox")

genre = st.radio("What's your favorite movie genre?",
                 ["Comedy", "Drama", "Documentary"],
                index=None,
                 )

if genre == "Comedy":
    st.write("You comedy me.. HaHa.")
else: 
    st.write("I think you would prefer comedy!")

genre = st.radio(
    "What's your favorite movie genre",
    [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
    index=None,
)

st.write("You selected:", genre)

st.header("Markdown")

st.markdown("*Streamlit* is **really** ***cool***.")
st.markdown('''
    :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
    :gray[pretty] :rainbow[colors].''')
st.markdown("Here's a bouquet &mdash;\
            :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

multi = '''If you end a line with two spaces,  
a soft return is used for the next line.

Two (or more) newline characters in a row will result in a hard return.
'''
st.markdown(multi)

st.header("Stock data")