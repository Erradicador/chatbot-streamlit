import streamlit as st

st.title("Mi Chatbot con Streamlit")
st.write("¡Bienvenido a mi chatbot en Streamlit!")
import streamlit as st
import openai
import os

# Configurar clave de OpenAI (usa variables de entorno si es posible)
openai.api_key = os.getenv("OPENAI_API_KEY", "TU_CLAVE_API_AQUÍ")

# Configuración de la app
st.title("🤖 IA en Streamlit")
st.write("Hazle una pregunta a la IA y te responderá.")

# Inicializar historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "system", "content": "Eres un asistente útil."}]

# Mostrar mensajes previos
for message in st.session_state.messages:
    if message["role"] != "system":  # No mostramos el mensaje del sistema
        with st.chat_message(message["role"]):
            st.write(message["content"])

# Entrada del usuario
user_input = st.text_input("Escribe tu pregunta:")

if user_input:
    # Guardar y mostrar el mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Llamar a la IA de OpenAI usando la nueva API
    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=st.session_state.messages
        )

        ai_response = response.choices[0].message.content

        # Guardar y mostrar la respuesta de la IA
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        with st.chat_message("assistant"):
            st.write(ai_response)

    except openai.OpenAIError as e:
        st.error(f"Error en la API de OpenAI: {str(e)}")

