import os
import shutil
import re
import json

from datetime import datetime
from dotenv import load_dotenv

from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.document_loaders import PyPDFDirectoryLoader


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

chunk_size = 1000
chunk_overlap = 150
model_name = "azure-gpt-4o",
persist_directory = "db",
documents_directory = "doc_pool"

loader = PyPDFDirectoryLoader(documents_directory)
docs = loader.load()
