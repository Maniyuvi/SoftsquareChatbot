import streamlit as st

st.set_page_config(
    page_title="Softsquare AI",
    page_icon="🤖",
)

st.title("Welcome")
st.write("This is a custom AI chatbot specific for our AppExchange Products Agrid, Media Manager and User 360.")



# from langchain.chat_models import ChatOpenAI
# from langchain.chains import ConversationChain
# from langchain.chains.conversation.memory import ConversationBufferWindowMemory
# from langchain.prompts import (
#     SystemMessagePromptTemplate,
#     HumanMessagePromptTemplate,
#     ChatPromptTemplate,
#     MessagesPlaceholder
# )
# import streamlit as st
# from streamlit_chat import message
# from utils import *
# from dotenv import load_dotenv

# load_dotenv()


# st.title("Chat with PDF 💬")

# if 'responses' not in st.session_state:
#     st.session_state['responses'] = []

# if 'requests' not in st.session_state:
#     st.session_state['requests'] = []

# if 'initialPageLoad' not in st.session_state:
#     st.session_state['initialPageLoad'] = True

# llm = ChatOpenAI(temperature=0, model='gpt-3.5-turbo') ## find at platform.openai.com

# if 'buffer_memory' not in st.session_state:
#             st.session_state.buffer_memory=ConversationBufferWindowMemory(k=3,return_messages=True)


# system_msg_template = SystemMessagePromptTemplate.from_template(template="""Answer the question as truthfully as possible using the provided context, 
# and if the answer is not contained within the text below, say 'I don't know'""")


# human_msg_template = HumanMessagePromptTemplate.from_template(template="{input}")

# prompt_template = ChatPromptTemplate.from_messages([system_msg_template, MessagesPlaceholder(variable_name="history"), human_msg_template])

# conversation = ConversationChain(memory=st.session_state.buffer_memory, prompt=prompt_template, llm=llm, verbose=True)


# # container for chat history
# response_container = st.container()
# # container for text box
# textcontainer = st.container()

# print('Initial Load ::::::::', st.session_state.initialPageLoad)
# if(st.session_state.initialPageLoad):
#     print('if Initial Load ::::::::', st.session_state.initialPageLoad)
#     refined_query = 'summarize the document and genrate some meaningfull qustion based on the document'
#     context = find_match(refined_query)
#     response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{refined_query}")
#     st.session_state.responses.append(response) 
#     st.session_state.initialPageLoad = False

# with textcontainer:
#     st.session_state.initialPageLoad = False
#     query = st.text_input("Query: ", key="input")
#     if query:
#         print('query :::', query)
#         with st.spinner("typing..."):
#             conversation_string = get_conversation_string()
#             print('conversation_string ::::: ::: ',conversation_string)
#             # st.code(conversation_string)
#             refined_query = query_refiner(conversation_string, query)
#             print('refined_query :::::', refined_query)
#             st.subheader("Refined Query:")
#             st.write(refined_query)
#             context = find_match(refined_query)
#             # print(context)  
#             response = conversation.predict(input=f"Context:\n {context} \n\n Query:\n{query}")
#         st.session_state.requests.append(query)
#         st.session_state.responses.append(response) 
# with response_container:
#     st.session_state.initialPageLoad = False
#     if st.session_state['responses']:
#         for i in range(len(st.session_state['responses'])):
#             message(st.session_state['responses'][i],key=str(i))
#             if i < len(st.session_state['requests']):
#                 message(st.session_state["requests"][i], is_user=True,key=str(i)+ '_user')
