import json
import streamlit as st
import pandas as pd

# text
st.title('FOIs | MOD')
st.subheader("Freedom of Information requests to the Ministry of Defence")

df = pd.read_csv('foi_MOD.csv')

search_term = st.text_input("Enter a search term:")

def search_dataframe(df, term):
    term = term.lower()
    return df[df.apply(lambda row: row.astype(str).str.lower().str.contains(term).any(), axis=1)]

if search_term:
    results = search_dataframe(df, search_term)
    st.write("### Search Results")
    st.dataframe(results)

# print link to the README on the github repo
st.link_button('Source', 'https://www.gov.uk/government/collections/foi-responses-released-by-the-ministry-of-defence-2025',  use_container_width=False)

