import fitz
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    with fitz.open(pdf_path) as pdf:
        for page in pdf:
            text += page.get_text()
    return text


###############################################################################################################
###############################################################################################################
###################################### Input ##################################################################
text = extract_text_from_pdf('PATH_TO_PDF_FILE')
filename_csv = 'flashcards3.csv'
myquery = "What is the answer for everything?"
ai_model = 'gpt-4.1-mini'
number_flashcards = "25"
my_api_key = ''
################################################################################################################
################################################################################################################
################################################################################################################


from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_text(text)


from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS


embeddings = OpenAIEmbeddings(api_key=my_api_key)
vector_store = FAISS.from_texts(chunks, embeddings)


from langchain_community.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

llm = ChatOpenAI(api_key=my_api_key, model=ai_model)

qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(search_kwargs={"k": 5}),
)

def generate_flashcards(query):
    prompt = f"""
    Create {number_flashcards} flashcards based on the document and the following topic:

    {query}

    Flashcards should be clearly formatted as:
    Question: <Question here>  
    Answer: <Answer here>
    """
    response = qa_chain.invoke(prompt)
    return response

flashcards = generate_flashcards(myquery)
print(flashcards)


import re

def parse_flashcards(flashcard_text):
    qa_pairs = re.findall(r"Question: (.+?)\s+Answer: (.+?)(?:\n|$)", flashcard_text, re.DOTALL)
    flashcards_list = [{"question": q.strip(), "answer": a.strip()} for q, a in qa_pairs]
    return flashcards_list

parsed_flashcards = parse_flashcards(flashcards['result'])
print(parsed_flashcards)


import pandas as pd

df = pd.DataFrame(parsed_flashcards)
df.to_csv(filename_csv, index=False)

