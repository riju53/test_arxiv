import streamlit as st
from langchain_community.retrievers import ArxivRetriever

st.title("ArXiv Research Assistant")

query = st.text_input("Enter topic")

if query:
    retriever = ArxivRetriever(load_max_docs=3)
    docs = retriever.invoke(query)

    for doc in docs:
        st.subheader(doc.metadata["Title"])
        st.write(doc.page_content[:500])
