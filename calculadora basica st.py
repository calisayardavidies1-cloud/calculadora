import streamlit as st

st.title("Calculadora")
st.write("Ingresar los valores numéricos y presionar la operación deseada.")

numero_1 = st.number_input("Primer número:")
numero_2 = st.number_input("Segundo número:", value=0.0, step=1.0, format="%.2f")

st.write("Elegir una operación:")

if st.button("Sumar"):
    resultado = numero_1 + numero_2
    st.success(f"**Resultado:** {numero_1} + {numero_2} = **{resultado:,.2f}**")

# Completar para que utilice las 4 operaciones básicas (resta, multiplicación y división) con botones y 
# muestre el resultado de manera similar al ejemplo de la suma.
