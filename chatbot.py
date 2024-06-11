
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Neo4jVector
from langchain_core.example_selectors import SemanticSimilarityExampleSelector
from langchain_core.prompts import FewShotPromptTemplate,PromptTemplate
from langchain_community.graphs import Neo4jGraph

def create_selectors(train_data:list)-> any:
    return SemanticSimilarityExampleSelector.from_examples(
        train_data,
        OpenAIEmbeddings(),
        Neo4jVector,
        k=5,
        input_keys=["question"]
    )

def refreshing_graph_schema():
    return Neo4jGraph()
    
def generate_prompt(selectors:any)->any:

    example_prompt=PromptTemplate.from_template(
        "User input:{question}\nCypher query:{query}"
    )
    
    return FewShotPromptTemplate(
        example_selector=selectors,
        example_prompt=example_prompt,
        prefix="Hello this customer graph chatbot",
        suffix="User input:{question}\nCypher quuery",
        input_variables=["questions"]
    )

