from dotenv import load_dotenv
import os
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_ollama import ChatOllama
#from langchain_anthropic import AnthropicLLM
from langchain_anthropic import ChatAnthropic
from tavily import TavilyClient
from langchain_tavily import TavilySearch
from typing import List
from pydantic import BaseModel, Field # parsing, metadata

load_dotenv()


tavily = TavilyClient()

class Source(BaseModel):
    """Schema for a source used by the agent"""
    
    url:str = Field (description="The URL of the source")
    
class AgentResponse(BaseModel):
    """Schema for agent response with answer and sources"""
    
    answer:str = Field(description="The agent's answer to the query")
    sources: List[Source] =  Field(default_factory=list, description="List of sources used to generate the answer")
    
    
# @tool
# def search(query: str)-> str:
#     '''
#     Docstring for search
    
#     :param query: Description
#     :type query: str
#     :return: Description
#     :rtype: str
#     '''
#     print(f"Recherche pour {query}")
#     return tavily.search(query=query)


llm = ChatAnthropic(temperature=0, model_name="claude-3-haiku-20240307")
#llm = ChatOllama(temperature=0, model="llama3.2:3b")
tools =[TavilySearch()]
agent = create_agent(model=llm, tools = tools, response_format=AgentResponse)


def main():
    result = agent.invoke({"messages": HumanMessage(content= "search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details")})
    print(result)

    
    
if __name__ == "__main__":
    main()