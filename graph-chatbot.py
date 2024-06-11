#######################################
## POC for neo4j graph chatbot
#######################################
import os
from dotenv import load_dotenv

## Neo4j imports
from neo4j import GraphDatabase

## Langchain, langchain_community,langchain_openai
from langchain.chains import GraphCypherQAChain
from langchain_openai import ChatOpenAI
from traindata import train_data
from chatbot import create_selectors,generate_prompt,refreshing_graph_schema
import streamlit as st

## reading environments
load_dotenv()
NEO4J_URI=os.getenv("NEO4J_URI")
NEO4J_USERNAME=os.getenv("NEO4J_USERNAME")
NEO4J_PASSWORD=os.getenv("NEO4J_PASSWORD")
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
OPEN_AI_MODEL=os.getenv("OPEN_AI_MODEL")
DEBUG_FLAG=os.getenv("DEBUG_FLAG")

# print(DEBUG_FLAG)
# if DEBUG_FLAG : 
#     print(f'Neo4j URI is {NEO4J_URI} , USER Name is {NEO4J_USERNAME}') 
#     print(train_data)  


def generate_ui():
    st.title('🎈 Graph-chatbot')
    #st.set_page_config(page_title="🤗💬 Graph-chatbot")
    st.chat_message("user")
    st.write("Hello :-)")

    if "messages" not in st.session_state.keys():
        st.session_state.messages = [{"role": "assistant", "content": "How may I help you?"}]

    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    prompt = st.chat_input("Say something")
    
    if prompt:
        st.write(f"User has sent the following prompt: {prompt}")


if __name__ == "__main__":
    try:    
        if DEBUG_FLAG : print("Refreshing graph schema...")
        # graph = refreshing_graph_schema()
        # graph.refresh_schema()
        # print(graph.schema)
        # if DEBUG_FLAG : print("Creating LLM and chains....")
        # llm=ChatOpenAI(model=OPEN_AI_MODEL,temperature =0)
        # chain=GraphCypherQAChain.from_llm(graph=graph,llm=llm,verbose=True)
        # if DEBUG_FLAG : print("creating selectors...")
        # selectors=create_selectors(train_data)
        # # print(selectors)
        # if DEBUG_FLAG : print("Generating prompt...")
        # prompt=generate_prompt(selectors)
        # print(prompt)
        #print(prompt.format(question="how many clients are there ?"))
        #selectors.select_examples({"how many clients are there ?"})
    except Exception as e:
        print("Error while creating selectors or prompts, may be refreshing graph schema!!!")


    # print(prompt.format(question="how many clients are there ?"))
    # selectors.select_examples({"how many clients are there ?"})


    # response=chain.invoke({"query": "how many clients have the policies ?"})
    # print(response)
    generate_ui()