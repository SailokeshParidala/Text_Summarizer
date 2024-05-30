import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import requests
from streamlit_lottie import st_lottie

def app():
    def load_lottieurl(url):
        r= requests.get(url)
        if r.status_code !=200:
            return None
        return r.json()

    lottie_coding = load_lottieurl("https://lottie.host/d9c3069b-a81c-4ed6-b3f2-ddd2cbbd4358/9WTvlSbv7z.json")

    text,logo =st.columns(2)
    with text:
        st.markdown("""
            <style>
                /* Define a custom CSS style for the h1 tag */
                h1 {
                    font-size: 5em; /* Adjust the font size as needed */
                }
            </style>
        """, unsafe_allow_html=True)

        # Header
        st.markdown("<h1 style='text-align: left; color: #ff5e8d;'>Our Services</h1>", unsafe_allow_html=True)

    with logo:
        st_lottie(lottie_coding,height =300)


    # Abstractive Summarization
    st.write("##")
    st.subheader('Abstractive Summarization with Pegasus Model')
    st.write("""
    Our advanced abstractive summarization feature utilizes the state-of-the-art Pegasus model to generate concise and coherent summaries, capturing the essence of the text.
    """)

    # Extractive Summarization
    st.write("---")
    st.subheader('Extractive Summarization with BERT Model')
    st.write("""
    Harness the power of the BERT model for extractive summarization, extracting the most relevant sentences from the text to provide informative summaries.
    """)

    # Question Answering
    st.write("---")
    st.subheader('Question Answering with BERT Model')
    st.write("""
    Ask questions and get precise answers directly from the text using our question answering feature powered by the BERT model.
    """)

    # Use Cases
    st.write("---")
    st.subheader('Use Cases')
    st.write("""
    QuickViewInsight can be applied in various domains and scenarios, including:
    - Research: Quickly summarize research papers and articles for efficient review.
    - Content Creation: Generate concise summaries for blog posts, reports, and presentations.
    - Information Retrieval: Extract relevant information from large text documents or datasets.
    """)

    # Try It Out
    st.write("---")
    st.header('Try It Out!')
    st.write("""
    Ready to experience the power of QuickViewInsight? Head over to our home page to explore our offerings and try out our text summarization and question answering functionalities today!
    """)


    # HTML for embedding Lottie animation
    html_code = f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            <iframe src="https://embed.lottiefiles.com/animation/69319"></iframe>
        </div>
    """

