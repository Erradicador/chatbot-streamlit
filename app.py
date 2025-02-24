import streamlit as st

st.title("Mi Chatbot con Streamlit")
st.write("¡Bienvenido a mi chatbot en Streamlit!")
import streamlit as st

# Configuración del chatbot
st.title("🤖 Chatbot con Streamlit")
st.write("¡Bienvenido! Escribe un mensaje y el chatbot responderá.")

# Inicializar el historial de conversación
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostrar mensajes previos
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Entrada del usuario
user_input = st.text_input("Escribe tu mensaje:")

if user_input:
    # Guardar y mostrar el mensaje del usuario
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    # Respuesta del chatbot (ejemplo básico)
    response = f"🤖 Respuesta automática: {user_input}"
    
    # Guardar y mostrar la respuesta del chatbot
    st.session_state.messages.append({"role": "bot", "content": response})
    with st.chat_message("bot"):
        st.write(response)
