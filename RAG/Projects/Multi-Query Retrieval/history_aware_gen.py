from dotenv import load_dotenv;
from langchain_chroma import Chroma;
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage;
from langchain_openai import ChatOpenAI,OpenAIEmbeddings;


load_dotenv();


persistent_directory="db/chroma_db";
embeddings=OpenAIEmbeddings(model="text-embedding-3-small");
db=Chroma(persist_directory=persistent_directory,embedding_function=embeddings);


model=ChatOpenAI(model="gpt-4o-mini");

chat_history=[];


def ask_question(user_question):
    print(f"\n---- You asked: {user_question}");
    
    #step1: Make the question clear using old conversion history;
    if chat_history:
        #llm rewrites thee question according the current question and history.
        messages=[
            SystemMessage(content="Given the chat history, rewrite the new question to be standalone and searchable. Just return the rewritten question.")
        ]+chat_history+[
            HumanMessage(content=f"New question : {user_question} ")
        ]

        result=model.invoke(messages);
        search_question=result.content.strip();
        print(f" Searching for: {search_question}");
    else:
        search_question=user_question;
    
    #step 2
    retriver=db.as_retriever(search_kwargs={"k":3});
    docs=retriver.invoke(search_question);
    
    for i , doc in enumerate(docs,1):
        lines=doc.page_content.split('\n')[:2];
        preview='\n'.join(lines);
        print(f"    Doc{i}:  {preview}...");

    #step 3: Create final prompt
    # Step 3: Create final prompt
    # Step 3: Create final prompt

    docs_text = "\n".join([f"- {doc.page_content}" for doc in docs])

    combined_input = f"""Based on the following documents, please answer this question: {user_question}

    Documents:
    {docs_text}

    Please provide a clear, helpful answer using only the information from these documents. 
    If you can't find the answer in the documents, say "I don't have enough information to answer that question based on the provided documents."
    """


    # Step 4: Get the answer
    messages = [
        SystemMessage(content="You are a helpful assistant that answers questions based on provided documents and conversation history."),
    ] + chat_history + [
        HumanMessage(content=combined_input)
    ]

    result=model.invoke(messages);
    answer=result.content;

    chat_history.append(HumanMessage(content=user_question));
    chat_history.append(AIMessage(content=answer));
    print(f"\n\tAnswer: {answer}");

    return answer;

def start_chat():
    print("\t\t  ------Hello Hamas!----- \n");
    print("     Ask me a Question! Type 'quit' to exit    :    ");
   

    while True:
        question=input("\nYour Question:   ");
        if question.lower()=="quit":
            print("\n\n-----GoodBye------");
            break;
        else:
            ask_question(question);

if __name__=="__main__":
    start_chat();


#who is the founder of micorsoft?
#what was the first microsoft hardware product release?
#  in which year it was founded?
# in which country it was founded?
