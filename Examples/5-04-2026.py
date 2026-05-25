import streamlit as st


def render():
    st.title("Prueba Stramlit")
    st.markdown("#Titulo ##Subtitulo ### mas chico ***letras negras*** *letras cursiva")
    st.header("Streamlit")
    st.caption("Frase de prueba stramlit")
    st.code("x = 202 ")

    st.image("C:\dev\prog\data-extraction-programming\Examples\imagenes\login.png")

def render2():
    st.title("Prueba Stramlit")
    st.checkbox("si")
    st.button("Click")
    st.radio("Genero", ["Mujer", "Hombre"])
    st.selectbox("Ciudad", ["Tijuana", "Rosarito", "Ensenada", "Tecate"])
    st.multiselect("Color", ["Rojo", "Morado", "Verde", "Negro"])
    st.select_slider("Califica", ["Bueno", "Malo", "Meh"])
    st.slider("Edad", 0, 100)
    st.text_input("Nombre")
    st.text_area("Descripcion")
    st.date_input("Fecha de inicio")
    st.success("EXITO")
    st.error("ERROR")
    st.warning("WARNING")
    st.info("INFO")


render2()