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

### Local Deployment with Docker
See `Dockerfile` for containerization instructions:
```bash
docker build -t carely-companion-chatbot .
docker run -p 8080:8080 -e PINECONE_API_KEY=your-key -e GEN_AI_API_KEY=your-key -e INDEX_NAME=your-index carely-companion-chatbot
```

### Deploying on Render
1. Sign up/Login to [Render](https://render.com)
2. Create a new Web Service
3. Connect your repository
4. Configure as follows:
   - **Name**: `carely-companion-chatbot` (or your preferred name)
   - **Environment**: Docker
   - **Branch**: main (or your default branch)
   - **Root Directory**: Leave blank
   - **Region**: Choose closest to your users
   - **Instance Type**: Start with Free tier
   - **Health Check Path**: `/`
5. Add Environment Variables:
   - `PINECONE_API_KEY`: Your Pinecone API key
   - `GEN_AI_API_KEY`: Your Google Generative AI API key
   - `INDEX_NAME`: Your Pinecone index name
6. Click "Create Web Service"

You can also use the included `render.yaml` file for easier deployment through Render's Blueprint feature.

## License
MIT