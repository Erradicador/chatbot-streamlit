import streamlit as st

st.title("Mi Chatbot con Streamlit")
st.write("¡Bienvenido a mi chatbot en Streamlit!")
import streamlit as st
import openai

# Configurar la API de OpenAI (coloca tu clave de API)
openai.api_key = "TU_CLAVE_API"

# Configuración de la app
st.title("🤖 IA en Streamlit")
st.write("Hazle una pregunta a la IA y te responderá.")

# Inicializar historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Entrada del usuario
user_input = st.text_input("Escribe tu pregunta:")

if user_input:
    # Guardar y mostrar el mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Llamar a la IA de OpenAI
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "Eres un asistente útil."}] + st.session_state.messages
    )

    ai_response = response["choices"][0]["message"]["content"]

    # Guardar y mostrar la respuesta de la IA
    st.session_state.messages.append({"role": "assistant", "content": ai_response})
    with st.chat_message("assistant"):
        st.write(ai_response)

