import streamlit as st
from cleaning import clean_all
from column import deal_df, work_df
from query import handle_user_query

deal_df, work_df = clean_all(deal_df, work_df)


st.set_page_config(page_title="Founder BI Agent")

st.title("Founder BI Agent")
st.write("Ask business intelligence questions about Deals & Work Orders data.")


user_query = st.text_input("Enter your BI query:")

if st.button("Run Query"):
    if user_query:
        result = handle_bi_query(user_query, deal_df, work_df)
        st.write(result)
    else:
        st.warning("Please enter a query.")

