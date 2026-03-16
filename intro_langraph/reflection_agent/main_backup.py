from typing import TypedDict, Annotated

from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph import END, StateGraph
from langgraph.graph.message import add_messages

from chain_backup import generate_chain, reflecte_chain

from dotenv import load_dotenv
import os

load_dotenv()


class MessageGraph(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]
    

REFLECT= "reflect"
GENERATE="generate"

def generation_node(state: MessageGraph):
    return {"messages" : [generate_chain.invoke({"messages": state["messages"]})]}

def reflection_node(state: MessageGraph):
    res= reflecte_chain.invoke({"messages": state["messages"]})
    return {"messages":[HumanMessage(content=res.content)]}



builder = StateGraph(state_schema=MessageGraph)
builder.add_node(GENERATE, generation_node)
builder.add_node(REFLECT, reflection_node)
builder.set_entry_point(GENERATE)


# on est passé 6 fois donc on arrrete (6 reflection)
def should_continue(state : MessageGraph):
    print(len(state["messages"]))
    print(state["messages"])
    if len(state["messages"]) > 6:
        return END
    return REFLECT


builder.add_conditional_edges(
    GENERATE,
    should_continue,
    {
        REFLECT: REFLECT,
        END: END,
    },
)

builder.add_edge(REFLECT, GENERATE)
graph = builder.compile() # besoin de compile pour invoke

graph.get_graph().draw_mermaid_png(output_file_path="flow.png")

if __name__ == "__main__":
    print("Hello LangGraph")
    inputs = {
        "messages": [
            HumanMessage(
                content="""Make this tweet better:"
                                    @LangChainAI
            — newly Tool Calling feature is seriously underrated.

            After a long wait, it's  here- making the implementation of agents across different models with function calling - super easy.

            Made a video covering their newest blog post

                                  """
            )
        ]
    }
    response = graph.invoke(inputs)
    print(response)


