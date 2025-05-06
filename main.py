
import os
from dotenv import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
import pinecone
from langchain_pinecone import PineconeVectorStore
from pinecone import Pinecone
from functools import lru_cache

# Load API keys from .env file
load_dotenv()

# Configuration
openai_api_key = os.getenv("OPENAI_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENV") # e.g., "us-west1-gcp"
pinecone_index_name = "my-index" # choose an appropriate name

# Print validation of .env values
print("✅ OPENAI_API_KEY loaded:", bool(openai_api_key))
print("✅ PINECONE_API_KEY loaded:", bool(pinecone_api_key))
print("✅ PINECONE_ENV loaded:", bool(pinecone_env))

# LangSmith API Key & Tracing
langsmith_api_key = os.getenv("LANGCHAIN_API_KEY")
if langsmith_api_key:
	os.environ["LANGCHAIN_TRACING_V2"] = "true"
	print("✅ LANGCHAIN_API_KEY loaded:", bool(langsmith_api_key))
else:
	print("❌ LANGCHAIN_API_KEY is not set. Please check your .env file or environment variables.")

class CFG:
	# Language Model Configuration (OpenAI GPT)
	llm_model  = 'gpt-4o-mini'
	temperature = 0.01
	max_tokens = 1024

	# Audio Transcription Model (Faster-Whisper)
	transcribe_model = 'small' # Options: 'tiny', 'base', 'small', 'medium', 'large-v2'
	save_transcriptions = True
	transcribe_files = False

	# YouTube Playlist or Audio Source
	playlist_links = [
		'https://www.youtube.com/playlist?list=PLdKd-j64gDcDVXmhHLIRIqpfnxiJadMjd',
	]

	audio_inputs_path = '/content/audio_inputs/'

	# Path to save transcripted text files
	save_transcript_path = '/content/transcriptions/'

	# Transcription parameters (optional placeholders)
	chunk_length = 10
	batch_size = 4

	# Embeddings Configuration (OpenAI + Pinecone)
	embedding_provider = 'openai'
	openai_api_key = os.getenv("OPENAI_API_KEY")
	openai_embedding_dim = 1536
	doc_similarity = 5 # Number of top similar documents to retrieve

	# Document Chunking for Retrieval
	chunk_size = 1000
	chunk_overlap = 0



# Initialize Pinecone client
pc = pinecone.Pinecone(api_key=os.getenv("PINECONE_API_KEY"))

# List current indexes
print("Current indexes:", pc.list_indexes().names())



embedding = OpenAIEmbeddings()

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
index_name = "my-index"
index = pc.Index(index_name)

vectorstore = PineconeVectorStore(
index=index,
embedding=embedding,
text_key="text"
)

#RAG (Retrieval-Augmented Generation) with LangChain
"""
qa_chain = RetrievalQA.from_chain_type(
llm=ChatOpenAI(temperature=0),
chain_type="stuff",
retriever=vectorstore.as_retriever()
)

"""


# Caching similarity search results to speed up repeated queries
@lru_cache(maxsize=128)
def cached_similarity_search(query):
    docs = vectorstore.similarity_search(query, k=CFG.doc_similarity)
    # Only cache the page_content to avoid issues with unhashable objects
    return tuple(doc.page_content for doc in docs)
