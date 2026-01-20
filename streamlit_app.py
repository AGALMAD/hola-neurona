import streamlit as st

st.image("./images/neurona.jpg", width=200)
st.header("!Hola neurona¡")

tab1, tab2, tab3 = st.tabs(["Una entrada", "Dos entradas", "Tres entradas y sesgo"])

y = 0

with tab1:
    w0 = st.slider("Peso", value=0.0, min_value=0.0, max_value=5.0, key="w0_col1")
    x0 = st.number_input("Entrada x0", value=0.0, key="x0_col1")

    if st.button("Calcular la salida", key="calc_button_col1"):
        y = w0 * x0
        st.success(f"Salida de la neurona: {y}")


with tab2:
    col1, col2 = st.columns(2)
    with col1:
        w0 = st.slider("Peso w0", min_value=0.0, max_value=5.0, key="w0_col2")
        w1 = st.slider("Peso w1", min_value=0.0, max_value=5.0, key="w1_col2")

    with col2:
        x0 = st.number_input("Entrada x0", value=0.0, key="x0_col2")
        x1 = st.number_input("Entrada x1", value=0.0, key="x1_col2")

    if st.button("Calcular la salida", key="calc_button_col2"):
        y = w0 * x0 + w1 * x1
        st.success(f"Salida de la neurona: {y}")

with tab3:
    col1, col2 = st.columns(2)
    with col1:
        w0 = st.slider("Peso w0", min_value=0.0, max_value=5.0, key="w0_col3")
        w1 = st.slider("Peso w1", min_value=0.0, max_value=5.0, key="w1_col3")
        w2 = st.slider("Peso w2", min_value=0.0, max_value=5.0, key="w2_col3")

    with col2:
        x0 = st.number_input("Entrada x0", value=0.0, key="x0_col3")
        x1 = st.number_input("Entrada x1", value=0.0, key="x1_col3")
        x2 = st.number_input("Entrada x2", value=0.0, key="x2_col3")

    b = st.number_input("Introduzca el valor del sesgo", value=1.0, key="b_col3")

    if st.button("Calcular la salida", key="calc_button_col3"):
        y = w0 * x0 + w1 * x1 + w2 * x2 + b
        st.success(f"Salida de la neurona: {y}",)

st.caption("© Alejandro Gálvez Madueño - CPIFP Alan Turing")
