import streamlit as st
from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.chat_models import ChatOllama
from langchain_core.runnables import RunnablePassthrough

# Define function to create the chain
def create_chain():
    local_model = "starcoder2"
    llm = ChatOllama(model=local_model)

    template = """You are an AI language coding assistant specialized in SQL, Python, R, and web applications named Gary Seven, after the star trek character. Answer the following question and provide the relevant code:
    Question: {question}
    """

    prompt = ChatPromptTemplate.from_template(template)

    chain = (
        {"question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

# Initialize the chain
chain = create_chain()

def ask_question(question):
    return chain.invoke(question)

# Streamlit app layout
st.title("Agent Gary Seven: AI Language Coding Assistant")
st.write("Specialized in SQL, Python, R, and web applications")

question = st.text_area("Enter your coding question:")
if st.button("Ask"):
    if question:
        answer = ask_question(question)
        st.write("### Answer")
        st.write(answer)
    else:
        st.write("Please enter a question.")
