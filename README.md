# Carely Companion Chatbot

A backend AI-powered medical assistant chatbot built with Flask, LangChain, Pinecone, and Google Generative AI. It retrieves answers from a collection of medical PDFs using vector search and large language models.

## Features
- REST API for chat interaction (`/chat` endpoint)
- RAG (Retrieval Augmented Generation) pipeline
- Uses Pinecone for vector search
- Embeddings via HuggingFace Transformers
- Google Generative AI for LLM responses

## Requirements
- Python 3.8+
- See `requirements.txt` for dependencies

## Setup
1. Clone the repo and navigate to the project directory.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set environment variables in a `.env` file:
   - `PINECONE_API_KEY`
   - `GEN_AI_API_KEY`
   - `INDEX_NAME`
4. Place your medical PDF files in the `data/` directory.
5. Build the Pinecone index:
   ```bash
   python store_index.py
   ```
6. Start the server:
   ```bash
   python app.py
   ```

## API Usage
- `POST /chat` with JSON `{ "msg": "your question" }`
- Returns `{ "answer": "response" }`

## Deployment
See `Dockerfile` for containerization instructions.

## License
MIT