#Necessary imports to create query engine for our data 
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, download_loader
from llama_index.core import Settings
from llama_index.llms.openai import OpenAI
import os
from llama_index.core import StorageContext, VectorStoreIndex, load_index_from_storage

load_dotenv()

#Only creating index store if does not exist 
def get_index(index_name):
    index = None
    if not os.path.exists(index_name):
        print("building index", index_name)
        #Creating index with all documents stored in data folder 
        documents = SimpleDirectoryReader('data').load_data()
        index = VectorStoreIndex.from_documents(documents, show_progress=True)
        #Saving index files created (index_store.json, docstore.json etc...)
        index.storage_context.persist(persist_dir=index_name)
    else:
        #Loading stored index files 
        index = load_index_from_storage(
            StorageContext.from_defaults(persist_dir=index_name)
        )

    return index

#Providing specific settings for our engine 
Settings.llm = OpenAI(model="gpt-3.5-turbo", temperature=0.1)
Settings.chunk_size = 1024
Settings.chunk_overlap = 20
rbi_index = get_index("rbi")
#Creating the query engine 
rbi_query_engine_service_context = rbi_index.as_query_engine(llm=Settings.llm) 
