from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from vector import retriever
 
model = OllamaLLM(model="deepseek-r1")

template = """
You are a helpful assistant which answers in one sentence about the sections, which contain the products.

Here is the list of sections: {sections}

Here is the question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = prompt | model

while True:
    print("--------------------------------")
    question = input("Ask me anything: ")
    if question == "q":
        break

    sections = retriever.invoke(question)
    result = chain.invoke({"sections": sections, "question": question})
    print(result)