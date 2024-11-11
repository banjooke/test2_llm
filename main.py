# main.py
import streamlit as st
from langchain.llms import OpenAI
from langchain import PromptTemplate, LLMChain

# Initialize OpenAI API key (use an environment variable for deployment)
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Set up LangChain components
llm = OpenAI(api_key=openai_api_key)
template = "Translate the following English text to French: {input_text}"
prompt = PromptTemplate(template=template, input_variables=["input_text"])
llm_chain = LLMChain(prompt=prompt, llm=llm)

# Streamlit App Interface
st.title("LLM Translation App with LangChain")
user_input = st.text_input("Enter text to translate:")

if st.button("Translate"):
    if user_input:
        response = llm_chain.run(input_text=user_input)
        st.write(response)
    else:
        st.write("Please enter some text.")
