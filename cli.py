import requests
import argparse

def main():
    parser = argparse.ArgumentParser(description="CLI for asking questions to the API.")
    parser.add_argument('--url', type=str, default="http://localhost:8000/ask", help="API endpoint URL")
    args = parser.parse_args()

    while True:
        question = input("Ask me anything (or type 'q' to quit): ")
        if question.lower() == 'q':
            break
        response = requests.post(
            args.url,
            json={"question": question}
        )
        print("Answer:", response.json().get("answer"))

if __name__ == "__main__":
    main()