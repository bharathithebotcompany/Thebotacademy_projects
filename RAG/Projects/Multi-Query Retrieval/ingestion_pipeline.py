import os;
from langchain_community.document_loaders import TextLoader, DirectoryLoader;
from langchain_text_splitters import CharacterTextSplitter;
from langchain_openai import OpenAIEmbeddings;
from langchain_chroma import Chroma;
from dotenv import load_dotenv;

load_dotenv();

def load_documents(docs_path="docs"):
    print(f"loading doucments from {docs_path}");
    if not os.path.exists(docs_path):
        raise FileNotFoundError(f"Directory {docs_path} does not exist");

    loader=DirectoryLoader(
        path=docs_path,
        glob="*.txt",
        loader_cls=TextLoader,
        loader_kwargs={"encoding": "utf-8"} 
        
    )
    documents=loader.load();
     
    if len(documents)==0:
        raise FileNotFoundError(f"No .txt files found in {docs_path}");

    for i,doc in enumerate(documents[:5]):
        print(f"\nDocument {i+1}");
        print(f" Source: {doc.metadata['source']}");
        print(f" Content Preview : {doc.page_content[:100]}");
        print(f" metadata: {doc.metadata}");
        print(f" document length : {len(doc.page_content)}");


    return documents;
       

def split_documents(documents,chunk_size=800,chunk_overlap=0):
    print(f"Spliting documents into the chunks");
    text_splitter=CharacterTextSplitter(
        chunk_size=chunk_size,
        # repeation between chunks to maintain context
        chunk_overlap=chunk_overlap
    )
    chunks=text_splitter.split_documents(documents);
    if chunks:
        for i , chunk in enumerate(chunks[:5]):
            print(f"\n ----Chunks----- {i+1}  ");
            print(f"Source {chunk.metadata['source']}");
            print(f"Content: ");
            print(chunk.page_content);
            print("-"*50);
        if len(chunks)>5:
            print(f"\n.. and {len(chunks)-5} more chunks");
    return chunks;


def create_vector_store(chunks,persist_directory="db/chroma_db"):
    print(f"creating embeddings and storing in chromadb");

    #Embedding models;
    embedding_model=OpenAIEmbeddings(model="text-embedding-3-small");
    print("---- Creating vector store");
    vector_store=Chroma.from_documents(
        documents=chunks,
        embedding=embedding_model,
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space":"cosine"}

    )
    print("----Finishing creating vector store");
    print(f"Vector store created and saved to {persist_directory}");
    return vector_store;
            







def main():
    
    print("System is working");
    #loading documents
    documents=load_documents(docs_path="docs");
    #chunking models;
    chunks=split_documents(documents);
    # creating embedding and storing into the vector database(Chromadb)
    vector_store=create_vector_store(chunks);
    



if __name__=="__main__":
    main();




# documents=[
#     Document(
#         page_content="difjdf kd fdjkfjj d",
#         metadata={'source':'docs/google.txt'};
#     )
# ]