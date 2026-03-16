from dotenv import load_dotenv

load_dotenv()

from langchain_tavily import TavilySearch
from langchain_core.tools import StructuredTool
from langgraph.prebuilt import ToolNode
from schema import AnswerQuestion, ReviseAnswer



tavily_tool = TavilySearch(max_results=5)

# si le llm donne d'autres valeurs que search_queries, pour pas avoir d'erreurs on ajoute  **kwargrs
# le but de la focntione st de faire plus de recherches sur les thèmes que le llm trouve qu'il manque
def run_queries(search_queries: list[str], **kwargrs):
    """Run the generated quesries."""
    return tavily_tool.batch([{"query": query} for query in search_queries])


execute_tools = ToolNode(
    [
        StructuredTool.from_function(run_queries, name = AnswerQuestion.__name__),
        StructuredTool.from_function(run_queries, name= ReviseAnswer.__name__),
    ]
)



