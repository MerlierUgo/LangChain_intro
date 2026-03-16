from langgraph.graph import END, StateGraph
from state import MessageGraph
from node import should_continue, generate_node, reflection_node



GENERATE = "generate"
REFLECTION = "reflection"


def build_graph(model):
    g = StateGraph(state_schema=MessageGraph)
    g.add_node(GENERATE, generate_node(model))
    g.set_entry_point(GENERATE)
    g.add_node(REFLECTION, reflection_node(model))

    g.add_conditional_edges(GENERATE, should_continue,{ 
                                    END:END,
                                    REFLECTION:REFLECTION,
                                }
                            )
    
    g.add_edge(REFLECTION, GENERATE)

    return g.compile()





