# local-rag-cli

Prerequisites:
- Ollama must be running llama3.1:8b

To index the files (run initially):

python main.py index --folder ./my-pdf-folder

To query the indexed files:

python main.py query --question "What is a good question for your specific PDFs?"

![Example of RAG CLI program with question and answer](./static/RAG_CLI_example.png)
