# Text_Summarizer
QuickViewInsight
QuickViewInsight is an advanced text summarization and question-answering tool designed to simplify the process of extracting key insights and answers from text data. This web application leverages state-of-the-art models like Pegasus and BERT to provide both abstractive and extractive summarization, as well as question-answering capabilities.

Features
Abstractive Summarization with Pegasus Model: Generates concise and coherent summaries, capturing the essence of the text.
Extractive Summarization with BERT Model: Extracts the most relevant sentences from the text to provide informative summaries.
Question Answering with BERT Model: Provides precise answers directly from the text.
Technology Stack
Streamlit: For building the interactive web application.
Hugging Face Transformers: For utilizing pre-trained models for text summarization and question answering.
Python: For backend logic and data processing.
PyTorch: For loading and running the machine learning models.
Jupyter Notebooks: For initial development and testing of core code.
PyCharm: For building the user interface using Streamlit.
Installation
Clone the repository:

git clone https://github.com/SailokeshParidala/Text_Summarizer
cd Text_Summarizer
Install the required packages:

pip install -r requirements.txt
Run the application:

streamlit run main.py

Usage
Main Page
The application's main page includes a sidebar menu to navigate between different sections: Home, About, Services, and Get Started.

Home Page
Provides an overview of QuickViewInsight, its key features, and how it works.

About Page
Introduces QuickViewInsight and the technology stack used in the project.

Services Page
Details the services offered by QuickViewInsight, including both types of summarization and question answering.

Get Started Page
Allows users to interact with the application by selecting a task (Summarizer or Question Answering), inputting text, and receiving results.

Results and Analysis
Abstractive Summarization with Pegasus Model: Provides high-quality summaries emphasising generating new sentences.
Extractive Summarization with BERT Model: Selects the most relevant sentences from the input text for summarization.
Question Answering with BERT Model: Achieves high accuracy in providing answers to questions based on the input text.
Evaluation Metrics
ROUGE Scores: Measures recall, precision, and F1 score based on the overlap of n-grams, word sequences, and word pairs between the system and reference summaries.
F1 Score: The harmonic mean of precision and recall.
Exact Match (EM) Score: Measures the percentage of predictions that match any one of the ground truth answers exactly.
Evaluation Results
Summarization Models (Pegasus and BERT):
ROUGE-1, ROUGE-2, and ROUGE-L scores for recall, precision, and F1.
Question Answering Model (BERT):
F1 Score: The harmonic mean of precision and recall.
Exact Match Score: The percentage of answers that match the ground truth exactly.

Contributing
If you would like to contribute to QuickViewInsight, please fork the repository and create a pull request. We welcome any improvements or additions to the project.
