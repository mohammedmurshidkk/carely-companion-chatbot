from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from  src.prompt import *

app = Flask(__name__)

# Setup CORS - Use comma-separated list of allowed domains from environment variable
# Example: export CORS_ALLOWED_ORIGINS=https://example.com,https://app.example.com
cors_allowed_origins_str = os.environ.get('CORS_ALLOWED_ORIGINS', '')
cors_allowed_origins = [origin.strip() for origin in cors_allowed_origins_str.split(',')] if cors_allowed_origins_str else []
CORS(app, resources={r"/chat": {"origins": cors_allowed_origins}})

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
GEN_AI_API_KEY = os.environ.get('GEN_AI_API_KEY')
INDEX_NAME = os.environ.get('INDEX_NAME')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["GEN_AI_API_KEY"] = GEN_AI_API_KEY

embeddings = download_hugging_face_embeddings()

index_name = INDEX_NAME

doc_search = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = doc_search.as_retriever(search_type='similarity', search_kwargs={"k": 3})

llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",  # or another Gemini model name if desired
    google_api_key=GEN_AI_API_KEY,
    temperature=0.4,
    max_output_tokens=500
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "{input}")
    ]
)

question_answer_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "msg" not in data:
        return jsonify({"error": "Missing 'msg' in JSON body"}), 400

    msg = data["msg"]
    print("request:", msg)

    response = rag_chain.invoke({"input": msg})
    print("response:", response["answer"])

    return jsonify({"answer": response["answer"]})


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host="0.0.0.0", port=port, debug=False)