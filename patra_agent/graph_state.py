from typing import Annotated, Sequence, TypedDict, List
from langchain_core.messages import HumanMessage, AIMessage, BaseMessage
import operator
from langchain_core.pydantic_v1 import BaseModel
from patra_agent.util import graph

class PatraState(BaseModel):
    """
    Agent state for the Agentic workflow.
    """
    messages: Annotated[Sequence[BaseMessage], operator.add]
    # graph schema for the CKN graph
    graph_schema = str(graph.get_structured_schema)
    # sender of the last message
    sender = "human"
