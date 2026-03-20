import os
from dotenv import load_dotenv
load_dotenv()
from graph.graph import app



if __name__ == "__main__":
    print("Agentic Rag")
    print(app.invoke(input={"question" : "How to make pizza ?"}))

