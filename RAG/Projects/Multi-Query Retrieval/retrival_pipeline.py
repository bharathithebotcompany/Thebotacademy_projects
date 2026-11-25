from langchain_chroma import Chroma;
from langchain_openai import OpenAIEmbeddings;
from dotenv import load_dotenv;
from langchain_openai import ChatOpenAI;
from langchain_core.messages import HumanMessage,SystemMessage;


load_dotenv();
persistent_directory="db/chroma_db";

embedding_model=OpenAIEmbeddings(model="text-embedding-3-small");

db=Chroma(
    persist_directory=persistent_directory,
    embedding_function=embedding_model,
    collection_metadata={"hnsw:space":"cosine"}
)
# query="which island does SpaceX lease for its launches in the Pacific?"
query="When the google was founded and who founded the google?"
# query="In what year did tesla began production of the Roadster?"
# query="Is a  Microsoft  american company and who founded the Microsoft?"

#now here retriver is going to choose top 3 chunks with higher similarity
# retriever=db.as_retriever(search_kwargs={"k":5});

#more enhanced way
retriever=db.as_retriever(
    search_type="similarity_score_threshold",
    search_kwargs={
        "k":5,
        "score_threshold":0.3
    }
)

relevant_docs=retriever.invoke(query);

print(f"User Query  {query}" );
print("--- Context----");
for i,doc in enumerate(relevant_docs,1):
    print(f"Document {i} :\n {doc.page_content}\n");






#Now using LLm chatgpt model , gpt-4o to get output using chunks knwoledge from vector db.

combined_input=f""" Based on the following documents, please answer this question" {query}

Documents:
{chr(10).join([f"{doc.page_content}" for doc in relevant_docs])}


Please provide a clear, helpful answer using on the information from these documents. If you cant find the answer in the documents, say "I dont have enough information to answer this question 

""";
model=ChatOpenAI(model="gpt-4o");
messages=[
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content=combined_input
)]


result=model.invoke(messages);
print("---- Response Generating --------")
print("Content only: \n")
print(result.content);



