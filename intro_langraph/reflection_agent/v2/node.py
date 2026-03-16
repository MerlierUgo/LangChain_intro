from langgraph.graph import END, StateGraph
from state import MessageGraph
from text_loader import load_prompt
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import BaseMessage, HumanMessage

GENERATE = "generate"
REFLECTION = "reflection"

def generate_node(model):
    text_generate = load_prompt(node_name="prompt_generate", prompt_type="system")
    prompt_generate = ChatPromptTemplate(
        [
            (
                "system",
                text_generate
            ),
            MessagesPlaceholder(variable_name="messages")
        ]
    )

    chain = prompt_generate | model

    def _node(state : MessageGraph):
        message_generate = chain.invoke({"messages" : state["messages"]})
        return {"messages" : message_generate}
    
    return _node

def reflection_node(model):
    prompt_reflection = load_prompt(node_name="prompt_reflection", prompt_type="system")
    prompt_reflection = ChatPromptTemplate(
        [
            (
                "system",
                prompt_reflection
            ),
            MessagesPlaceholder(variable_name="messages")
        ]
    )
    chain = prompt_reflection | model

    def _node(state : MessageGraph):
        message_reflection = chain.invoke({"messages":state["messages"]})
        return {"messages" : [HumanMessage(content = message_reflection.content)]}

    return _node



def should_continue(state: MessageGraph):
    # print(len(state["messages"]))
    # print(state["messages"])
    if len(state["messages"]) > 6:
        return END 
    return REFLECTION