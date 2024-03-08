from pathlib import Path
#from llama_index import download_loader
import openai
from llama_index.readers.file import PDFReader
 
# get keys from .env file
import os
from dotenv import load_dotenv
load_dotenv()
os.environ['OPENAI_API_KEY']='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'

openai.api_key = os.getenv('OPENAI_API_KEY')

#download_loader
#pdfReader = PDFReader("PDFReader") # https://llamahub.ai

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

#loader = pdfReader()
documents = SimpleDirectoryReader('data').load_data()
index = VectorStoreIndex.from_documents(documents)
index.storage_context.persist()
print("Done") 