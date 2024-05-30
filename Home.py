import streamlit as st
from streamlit_extras.switch_page_button import switch_page

import About,GetStarted,Home,Services

import requests
from streamlit_lottie import st_lottie

def app():

    def load_lottieurl(url):
        r= requests.get(url)
        if r.status_code !=200:
            return None
        return r.json()

    lottie_coding = load_lottieurl("https://lottie.host/6b92112c-2c1b-42b4-8694-52e6a3dd6ef7/erj8jvOmIu.json")
    # Header Section
    with st.container():
        st.markdown("""
            <style>
                /* Define a custom CSS style for the h1 tag */
                h1 {
                    font-size: 8em; /* Adjust the font size as needed */
                }
            </style>
        """, unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: #ff5e8d;'>Quick View Insight</h1>", unsafe_allow_html=True)
        st.markdown("<h4 style='text-align: center'>Your Destination for Efficient Text Summarization and Question Answering</h4>",unsafe_allow_html=True)
        st.write("")
        st.write("")
        st.markdown("<h6 style ='text-align: center'> Welcome to QuickViewInsight, where we simplify the process of extracting key insights and answers from text data.Whether you need concise summaries or quick answers to your questions, we've got you covered!</h6>",unsafe_allow_html=True)
        st.markdown("<h6 style ='text-align: center'> </h6>",unsafe_allow_html=True)


    # Features Section
    with st.container():
        st.write("---")
        st.header("Key Features")
        st.write("##")

        st.markdown("""
        - **Abstractive Summarization with Pegasus Model** Our advanced abstractive summarization feature utilizes the state-of-the-art Pegasus model to generate concise and coherent summaries, capturing the essence of the text.

        - **Extractive Summarization with BERT Model**: Harness the power of the BERT model for extractive summarization, extracting the most relevant sentences from the text to provide informative summaries.

        - **Question Answering with BERT Model**: Ask questions and get precise answers directly from the text using our question answering feature powered by the BERT model.
        
        """)
    # Working Description
    with st.container():
        st.write("---")
        st.header("How It Works")
        st.write("##")

        st.write("""
        - **Choose Your Task**: Select between abstractive summarization, extractive summarization, or question answering based on your requirements.

        - **Input Text**: Paste or type the text you want to summarize or extract information from into the input box.

        - **Get Results**: Sit back and let QuickViewInsight do the rest! Within seconds, you'll receive a summary or answers to your questions, helping you save time and effort.
        """)
    st.write("##")
    st.write('##')
    st.write('<p style="font-size:37px; color:#ff5e8d;">Try It Out!</p>',
             unsafe_allow_html=True)

    st.markdown("<h5 style ='text-align: center'> Ready to experience the power of QuickViewInsight? Head over to our services page to explore our offerings and click on GetStarted to  try out our text summarization and question answering functionalities today!</h5>", unsafe_allow_html=True)


