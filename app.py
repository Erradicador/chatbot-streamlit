import streamlit as st

st.title("Mi Chatbot con Streamlit")
st.write("¡Bienvenido a mi chatbot en Streamlit!")
import streamlit as st
import openai

st.title("🤖 Chatbot con OpenAI en Streamlit")

# Campo para ingresar la clave de OpenAI
openai_api_key = st.text_input("Ingresa tu OpenAI API Key", type="password")

if openai_api_key:
    openai.api_key = openai_api_key

    # Entrada del usuario
    user_input = st.text_input("Hazme una pregunta:")

    if user_input:
        try:
            respuesta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": user_input}]
            )
            st.write("🤖", respuesta["choices"][0]["message"]["content"])
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.warning("Por favor, ingresa tu API Key para continuar.")
