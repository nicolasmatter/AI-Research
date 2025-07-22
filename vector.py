from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma 
from langchain_core.documents import Document
import os
import pandas as pd

df = pd.read_csv("sections.csv")
embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./chrome_langchain_db"
add_documents = not os.path.exists(db_location)

if add_documents:
    documents = []
    ids = []
    
    for i, row in df.iterrows():
        # Build a more informative document text
        content_parts = [
            f"Title: {row['title']}",
            f"Description: {row['description']}",
            f"Products: {row['products']}"
        ]
        page_content = "\n".join([str(part) for part in content_parts if pd.notnull(part)])
        document = Document(
            page_content=page_content,
            metadata={"products": row["products"], "title": row["title"]},
            id=str(i)
        )
        ids.append(str(i))
        documents.append(document)
        
vector_store = Chroma(
    collection_name="sections",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)
    
retriever = vector_store.as_retriever(
    search_kwargs={"k": 5}
)