from ast import keyword
import streamlit as st
from mainModel import gpt3

st.title("Headlines Generator")

st.warning('this is made for assignment provided by the Pragmatic Leaders for the intership only')

st.write('The program is made to generate better news headlines when an input of keywords or a series a sentence is given to the A.I model')
st.caption('The Davinci-001 api is used to complete or generate the set of text as per input')

content = st.text_input("enter the heading for the paragraph")
result = gpt3(content)

if st.button('show results'):
    st.write(result)
    st.success("The program wroked sucessfully")
