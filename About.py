import streamlit as st
import requests
from streamlit_lottie import st_lottie

def app():
    def local_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>",unsafe_allow_html=True)

    local_css("style/Style.css")



    def load_lottieurl(url):
        r= requests.get(url)
        if r.status_code !=200:
            return None
        return r.json()

    lottie_coding = load_lottieurl("https://lottie.host/0252e70a-c2a7-4ebe-88d7-8c9556ebf50b/zzuEdwEiKS.json")
    lottie=load_lottieurl("https://lottie.host/944c754b-ec01-4e32-8a37-55fe23ad1598/IjCDbwivlI.json")

    with st.container():
        text,ani=st.columns(2,gap='medium')
        with text:
            st.markdown("""
                        <style>
                            /* Define a custom CSS style for the h1 tag */
                            h1 {
                                font-size: 3em; /* Adjust the font size as needed */
                            }
                        </style>
                    """, unsafe_allow_html=True)

            # Header
            st.markdown("<h1 style='text-align: left; color: #ff5e8d;'>About QuickViewInsight</h1>", unsafe_allow_html=True)

        with ani:
            st_lottie(lottie,height=200)

        st.write("##")

        #Introduction

        st.markdown('''<h4>QuickViewInsight is a powerful text summarization and question answering tool designed to simplify the process of extracting key insights and answers from text data.
 </h4>''',unsafe_allow_html=True)


    with st.container():
        st.write("##")
        # Technology Stack
        st.subheader('Technology Stack')
        st.write("""
        QuickViewInsight is built using the following technologies:
        - Streamlit: For building the interactive web application
        - Hugging Face Transformers: For utilizing pre-trained models for text summarization and question answering
        - Python: For backend logic and data processing
        """)
        st.write("##")

    with st.container():
        st.write("---")
        st.header("Get In Touch With Me!")
        st.write("##")

        # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
        contact_form = """
        <form action="https://formsubmit.co/sailokeshparidala03@gmail.com" method="POST">streAM
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st_lottie(lottie_coding,height = 300,key='mail')
