from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import  HuggingFaceEmbeddings


def load_pdf_file(folder_path):
    loader = DirectoryLoader(folder_path, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    return documents


def text_split(ed):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=20)
    text_chunks = text_splitter.split_documents(ed)
    return text_chunks


def download_hugging_face_embeddings():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    return embeddings