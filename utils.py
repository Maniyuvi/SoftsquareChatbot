from sentence_transformers import SentenceTransformer
import pinecone
import openai
import streamlit as st
import json

#Streamlit Run
openai.api_key = st.secrets["OPENAI_API_KEY"]

embed_model = "text-embedding-ada-002"
pinecone_api_key = st.secrets["PINECONE_API_KEY"]
pinecone_environment = st.secrets["PINECONE_ENVIRONMENT"]
pinecone_index = st.secrets["PINECONE_INDEX"]


pinecone.init(api_key=pinecone_api_key,
              environment=pinecone_environment
             )
index_name = pinecone_index
index = pinecone.Index(index_name) # index name from pinecone)


def find_match(input):
    res = openai.Embedding.create(
        input=[input],
        engine=embed_model
    )
    xq = res['data'][0]['embedding']

    result = index.query(xq, top_k=2, include_metadata=True)
    # print('matches:::', result['matches'])

    return result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text']

def query_refiner(conversation, query):
    print('conversation :::::', conversation)
    print('query ::::::', query)

    if 'user_input' in st.session_state:
        user_info = st.session_state['user_input']
        product_type = user_info['product_type']
        if(product_type):
            query = query + f"in {product_type}"

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=f"Given the following user query and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base.\n\nCONVERSATION LOG: \n{conversation}\n\nQuery: {query}\n\nRefined Query:",
    temperature=0.7,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )

    print('response ::::', response)

    return response['choices'][0]['text']

def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses'])-1):
        
        conversation_string += "Human: "+st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: "+ st.session_state['responses'][i+1] + "\n"
    return conversation_string
