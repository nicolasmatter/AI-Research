# AI-Research

## Intro

This is a research project to figure out how to have a Chatbot running on a remote machine which can be accessed via the web.
The Chatbot should also have access to a local database.

## Tech Stack

- Python
- Langchain
- Ollama
- Open WebUI

## Setup

### On the remote machine

1. Install Ollama
2. Install Python
3. Create a virtual environment with `python -m venv venv`
4. `./venv/bin/activate`to enter the virtual environment
5. `pip install -r requirements.txt`to install the dependencies
6. Run main script with `python main.py`

### On the local machine

1. Install Docker
2. Run, but replace the IP address with the IP address of the remote machine

````docker run -d -p 3000:8080 -e OLLAMA_BASE_URL=http://192.168.1.210:11434 -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
ddb6b5b4cddf6ab7fa49d77ca421f2231cc08c4e8b52aacacf795b4bbd028e1d```
3. Open the browser and go to `http://localhost:3000`
````
