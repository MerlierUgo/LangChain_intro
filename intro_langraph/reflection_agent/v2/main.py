import os
from dotenv import load_dotenv
from graph import build_graph
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from text_loader import load_prompt

load_dotenv()

if __name__ == "__main__":
    llm = ChatOpenAI()
    app = build_graph(llm)
    app.get_graph().draw_mermaid_png(output_file_path="flow_v2.png")
    tweet = load_prompt(node_name="tweet", prompt_type="system")
    inputs = {
            "messages": [
                HumanMessage(
                    content=f"""Make this tweet better:"
                                        {tweet}
                                    """
                )
            ]
        }
    
    print(inputs["messages"][0].content)
    response = app.invoke(inputs)

    print(response)


    