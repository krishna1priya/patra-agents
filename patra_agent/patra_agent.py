from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate, ChatPromptTemplate
from langgraph.graph import END, StateGraph, START
from typing import Annotated, Literal, Sequence, TypedDict
from langchain_core.pydantic_v1 import BaseModel, Field
from util import graph, llm, top_k_results
from patra_agent.cypher_templates import patra_generation_template, answer_generator_template

class CypherGenerator(BaseModel):
    cypher_query: str = Field(
        description="Syntactically correct cypher query ready for execution"
    )

    context: str = Field(
        description="Context about the query"
    )

generation_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", patra_generation_template),
        ("human", "Schema: {schema}.",
        ),
    ]
)
cypher_gen_llm = llm.with_structured_output(CypherGenerator)
cypher_generator = generation_prompt | cypher_gen_llm

answer_generator_prompt = PromptTemplate(
    input_variables=["question", "db_response"], template=answer_generator_template
)

answer_generator = answer_generator_prompt | llm | StrOutputParser()

class PatraAgent(TypedDict):
    """
    Represents the state of the graph
    """


def generate_cypher(state):
    """
    Generate or regenerate the cypher query.
    """
    print("---GENERATING CYPHER QUERY---")
    user_question = state["question"]
    chat_history = state["chat_history"]
    cypher_generation = state["cypher_generation"]

    if cypher_generation is not None:
        user_question = user_question + " Previously generated cypher was wrong which was: " + cypher_generation

    cypher_gen_result = cypher_generator.invoke({"chat_history": chat_history, "schema": graph.get_structured_schema, "question": user_question})
    generated_cypher = cypher_gen_result.cypher_query
    print(state)
    return {"cypher_generation": generated_cypher, "question": user_question}

def execute_query(state):
    print("---DECISION: EXECUTING QUERY ON GRAPH ---")
    print(state)
    query = state["cypher_generation"]
    response = graph.query(query)[:top_k_results]
    query_result = str(response).replace("{", "{{").replace("}", "}}")
    return {"query_response": query_result, "cypher_generation": query}


def generate_human_response(state):
    print("---GENERATING HUMAN LIKE RESPONSE ---")

    print(state)

    user_question = state["question"]
    query_response = state["query_response"]

    generated_answer = answer_generator.invoke({"question": user_question, "db_response": query_response})
    print("GENERATED:" + generated_answer)
    return {"query_response": query_response, "question": user_question, "generated_answer": generated_answer}


workflow = StateGraph(PatraAgent)


workflow.add_node("generate_cypher", generate_cypher)  # retrieve
workflow.add_node("execute_query", execute_query)  # grade documents
workflow.add_node("gen_human_response", generate_human_response)  # grade documents

# Build graph
workflow.add_edge(START, "generate_cypher")
workflow.add_edge("generate_cypher", "execute_query")
workflow.add_edge("execute_query", "gen_human_response")
workflow.add_edge("gen_human_response", END)
app = workflow.compile()
