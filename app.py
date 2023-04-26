from helper import *
import streamlit as st

import streamlit as st
from helper import *

st.title("Ask about your CRM contacts!")


def main():
    # Get user input
    user_query = st.text_input("Ask the CRM", value='Who is Toni?')

    if user_query != ":q" or user_query != "":
        # st.write(response['gpt_full_response']['choices'][0]['text'])
        response = get_contact_response(user_query)
        st.write(response[['f_name', 'l_name', 'notes']])
        return


main()
