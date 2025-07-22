from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
 
app = FastAPI()

model = OllamaLLM(model="gemma3")

template = """
You are a helpful assistant which answers in one sentence about the sections, which contain the products.

Here is the list of sections: {sections}

Here is the question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask(request:QuestionRequest):
    sections = retriever.invoke(request.question)
    result = chain.invoke({"sections":sections,"question":request.question})
    return{"answer":result}