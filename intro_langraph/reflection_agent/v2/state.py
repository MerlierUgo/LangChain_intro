from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import add_messages


class MessageGraph(TypedDict):
    messages :  Annotated[list[BaseMessage], add_messages]

