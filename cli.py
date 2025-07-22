import requests

def main():
    while True:
        question = input("Ask me anything (or type 'q' to quit): ")
        if question.lower() == 'q':
            break
        response = requests.post(
            "http://localhost:8000/ask",
            json={"question": question}
        )
        print("Answer:", response.json().get("answer"))

if __name__ == "__main__":
    main()