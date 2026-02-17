from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_pinecone import PineconeVectorStore
import os
from pathlib import Path

load_dotenv()

if __name__ == "__main__":
    current_dir = Path(__file__).parent
    file_path = current_dir / "mediumblog1.txt"
    print(file_path)
    loader = TextLoader(str(file_path), encoding='UTF-8', autodetect_encoding=True)
    document = loader.load()

    print("splitting...")
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(document)

    print(f'created {len(texts)} chunks')

    embeddings = OpenAIEmbeddings(openai_api_type=os.environ.get("OPENAI_API_KEY"))

    print("ingesting...")

    PineconeVectorStore.from_documents(texts, embeddings, index_name=os.environ['INDEX_NAME'])
    
     
    

    
    
    
    
    