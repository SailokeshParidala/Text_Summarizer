import streamlit as st
import torch
import time
import requests
from streamlit_lottie import st_lottie
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, AutoModelForQuestionAnswering
import nltk
nltk.download('punkt')
from streamlit_option_menu import option_menu
def app():

    def load_lottieurl(url):
        r= requests.get(url)
        if r.status_code !=200:
            return None
        return r.json()

    lottie_coding = load_lottieurl("https://lottie.host/ee755153-e04e-4e04-8afa-a8d6add26287/Jf29i940c9.json")
    lottie = load_lottieurl("https://lottie.host/6b92112c-2c1b-42b4-8694-52e6a3dd6ef7/erj8jvOmIu.json")


    col1,col2=st.columns(2,gap='medium')
    with col1:
        st.markdown("""
                                <style>
                                    /* Define a custom CSS style for the h1 tag */
                                    h1 {
                                        font-size: 3em; /* Adjust the font size as needed */
                                    }
                                </style>
                            """, unsafe_allow_html=True)

        # Header
        st.markdown("<h1 style='text-align: left; color: #ff5e8d;'>Welcome to QuickViewInsight</h1>", unsafe_allow_html=True)

    with col2:
        st_lottie(lottie_coding,height=240)


    selected= option_menu(
        menu_title=None,
        options = ["Summarizer","QuestionAnswering"],
        orientation="horizontal"
    )
    if selected=='Summarizer':
        user_input = st.text_area("Enter Your Text here")

        summarization_method = st.selectbox("Select Summarization Method", ["Abstractive", "Extractive"])

        def summarize_text(text,method):
            if method == 'Abstractive':
                checkpoint = "google/pegasus-cnn_dailymail"

                tokenizer = AutoTokenizer.from_pretrained(checkpoint)
                model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

                sentences = nltk.tokenize.sent_tokenize(text)
                length = 0
                chunk = ""
                chunks = []
                count = -1
                for sentence in sentences:
                    count += 1
                    combined_length = len(
                        tokenizer.tokenize(sentence)) + length  # add the no. of sentence tokens to the length counter

                    if combined_length <= tokenizer.max_len_single_sentence:  # if it doesn't exceed
                        chunk += sentence + " "  # add the sentence to the chunk
                        length = combined_length  # update the length counter

                        # if it is the last sentence
                        if count == len(sentences) - 1:
                            chunks.append(chunk.strip())  # save the chunk
                    else:
                        chunks.append(chunk.strip())  # save the chunk

                        # reset
                        length = 0
                        chunk = ""

                        # take care of the overflow sentence
                        chunk += sentence + " "
                        length = len(tokenizer.tokenize(sentence))

                final_output = []
                inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]
                for input in inputs:
                    output = model.generate(**input)
                    print(tokenizer.decode(*output, skip_special_tokens=True))
                    final_output.append(tokenizer.decode(*output, skip_special_tokens=True))

                for i, text in enumerate(final_output):
                    text = text.capitalize()
                    if text[-1] != '.':
                        text += '.'
                    text = text.replace('<n>', '')
                    final_output[i] = text
                s = '  '.join(final_output)
                return  s

            elif method == 'Extractive':
                checkpoint = "Shobhank-iiitdwd/BERT_summary"

                tokenizer = AutoTokenizer.from_pretrained(checkpoint)
                model = AutoModelForSeq2SeqLM.from_pretrained(checkpoint)

                sentences = nltk.tokenize.sent_tokenize(text)
                length = 0
                chunk = ""
                chunks = []
                count = -1
                for sentence in sentences:
                    count += 1
                    combined_length = len(
                        tokenizer.tokenize(sentence)) + length  # add the no. of sentence tokens to the length counter

                    if combined_length <= tokenizer.max_len_single_sentence:  # if it doesn't exceed
                        chunk += sentence + " "  # add the sentence to the chunk
                        length = combined_length  # update the length counter

                        # if it is the last sentence
                        if count == len(sentences) - 1:
                            chunks.append(chunk.strip())  # save the chunk
                    else:
                        chunks.append(chunk.strip())  # save the chunk

                        # reset
                        length = 0
                        chunk = ""

                        # take care of the overflow sentence
                        chunk += sentence + " "
                        length = len(tokenizer.tokenize(sentence))

                final_output = []
                inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]
                for input in inputs:
                    output = model.generate(**input)
                    print(tokenizer.decode(*output, skip_special_tokens=True))
                    final_output.append(tokenizer.decode(*output, skip_special_tokens=True))

                for i, text in enumerate(final_output):
                    text = text.capitalize()
                    if text[-1] != '.':
                        text += '.'
                    text = text.replace('<n>', '')
                    final_output[i] = text
                s = '  '.join(final_output)
                return s

        if st.button("Summarize"):
            with st.spinner('Summarizing...'):
                if user_input:
                    summary = summarize_text(user_input, summarization_method)
                    st.empty()
                    st.success("Summary:")
                    st.write(summary)
                else:
                    st.empty()
                    st.warning("Please enter some text to summarize")


    elif selected=='QuestionAnswering':
        model_name = "google-bert/bert-large-uncased-whole-word-masking-finetuned-squad"
        model_qa = AutoModelForQuestionAnswering.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)


        user_input=st.text_area("Enter Your Context")
        question = st.text_input("Enter Your Question to Answer")

        input_txt = user_input[:2000]
        inputs = tokenizer(question, input_txt, add_special_tokens=True, return_tensors="pt")
        start_logits, end_logits = model_qa(**inputs).values()

        start_index = torch.argmax(start_logits, dim=1).item()
        end_index = torch.argmax(end_logits, dim=1).item() + 1

        if st.button("Answer"):
            with st.spinner("searching..."):
                answer_tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start_index:end_index])
                answer = tokenizer.convert_tokens_to_string(answer_tokens)
                st.write(answer)

