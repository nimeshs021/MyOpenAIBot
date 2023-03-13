import openai 
import streamlit as st

# pip install streamlit-chat  
from streamlit_chat import message
openai.api_key = st.secrets["inc"]["APIKey"]


def generate_response(prompt):
    completions = openai.Completion.create(
        engine = "text-davinci-003",
        prompt = prompt,
        max_tokens = 1024,
        n = 1,
        stop = None,
        temperature=1,
    )
    message = completions.choices[0].text
    return message 

#Creating the chatbot interface
st.title("chatBot : Streamlit + openAI By Nimesh. Played by NeelLohit")

# Storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []


# We will get the user's input by calling the get_text function
def get_text():
    #input_text = st.text_input("You: ","Hello, how are you?", key="input")
    input_text = st.text_input("You: ","", key="input")
    return input_text


user_input = get_text()

if user_input:
    output = generate_response(user_input)
    # store the output 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

 


#Finally, we will display the chat history by iterating through the generated and past lists and using the message function 
# from the streamlit_chat library to display each message.
if st.session_state['generated']:
    
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')


