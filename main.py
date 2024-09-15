import streamlit as st
from lanchain_helper import create_vector_db
from lanchain_helper import get_qa_chain

st.title("Course information QA")
btn=st.button("Create Knowledge base")

if btn:
    create_vector_db()
question = st.text_input("Question: ")

question= st.text_input("Question:")
if question:
    chain=get_qa_chain()
    response=chain(question)
    st.header("Answer")
    st.write(response["result"])
    pass