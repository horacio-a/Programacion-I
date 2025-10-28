import streamlit as st
from components import code_and_run
def run():
    st.header("Mutabilidad")
    st.markdown(
        "<p style='font-size:18px;'>La mutabilidad se refiere a la capacidad que tiene un objeto de cambiar su contenido después de haber sido creado</p>",
        unsafe_allow_html=True
    )
    st.write('Un **objeto mutable** puede modificarse sin necesidad de crear uno nuevo. Ejemplo en Python: listas `(list)` o diccionarios `(dict)`')
    st.code("""
    # Una lista (list)
    numeros = [1, 2, 3]
            
    # Un diccionario (dict)
    personas = {
        "nombre": "Ana",
        "edad": 25,
        "profesion": "Ingeniera",
    }""", language="python")
    st.write('Un **objeto inmutable** no puede modificarse una vez creado. Cualquier operación que parezca “cambiarlo” en realidad crea un nuevo objeto. Ejemplo: enteros `(int)`, cadenas `(str)` o tuplas `(tuple)`.')

    st.code("""
    # Un entero (int)
    edad = 25

    # Una cadena de texto (str)
    nombre = "Ana"

    # Una tupla (tuple)
    coordenadas = (10.5, 20.3)""", language="python")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("`int` (inmutable)")
        val = st.number_input("Valor inicial (int)", value=10, step=1)
        suma = st.number_input("Cantidad a sumar", value=1, step=1)
        
        code_A = f"""
def increment(x):
    x += {int(suma)}  # crea un nuevo int
    return x

a = {int(val)}
b = increment(a)
print("a:", a)   # {int(val)}
print("b:", b)   # {int(val)+ suma}"""
        def run_A():
            a = int(val)
            b = a + suma
            st.write(f"`a` fuera: **{a}**")
            st.write(f"`b` devuelto: **{b}**")
            st.info("El a original no cambió (int es inmutable).")
        code_and_run(code_A, run_A)
    with col2:
        st.subheader("`list` (mutable)")
        items = st.text_input("Lista inicial (valores separados por comas)", "1,2,3")
        item = st.text_input("Valor a agregar", "4")

        try:
            lst0 = [int(x.strip()) for x in items.split(",") if x.strip()!='']
        except:
            lst0 = [1,2,3]
        try:
            addItem = int(item)
        except:
            addItem = item

        code_B = f"""def append_four(L):
    L.append({addItem}) # muta la lista recibida

lista = {lst0}

append_four(lista)
print(lista)  # se ve el cambio afuera
"""
        def run_B():
            L = list(lst0)
            L.append(addItem)
            st.write(f"Lista luego de la función: **{L}**")
            st.warning("Como `list` es mutable, el cambio se observa fuera de la función.")
        code_and_run(code_B, run_B)