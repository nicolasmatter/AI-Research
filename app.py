from fastapi import FastAPI
from pydantic import BaseModel
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
 
app = FastAPI()

model = OllamaLLM(model="gemma3")

template = """
You give one sentence answers to the question.

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