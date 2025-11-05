import streamlit as st

def run():
    st.title("🧱 Tipos de Datos Abstractos (TDA)")

    # ======= TEORÍA =======
    st.subheader("📘 ¿Qué es un Tipo de Dato Abstracto?")
    st.markdown("""
Un **Tipo de Dato Abstracto (TDA)** es un **modelo lógico** que define **qué operaciones se pueden realizar sobre un conjunto de datos**,  
pero **sin especificar cómo se implementan internamente**.

En otras palabras: un TDA **describe el comportamiento**, no los detalles del código.

Por ejemplo, podemos definir una **Pila (Stack)** así:
- `apilar(elemento)` → agrega un elemento arriba.
- `desapilar()` → saca el último elemento agregado.
- `ver_tope()` → devuelve el último elemento sin quitarlo.
- `vacia()` → indica si la pila está vacía.

El usuario del TDA no necesita saber si la pila se guarda en una lista, un arreglo o una cola.  
Solo importa que **funcione como una pila** (último en entrar, primero en salir — LIFO).
""")

    st.info("👉 Los TDAs separan **qué hace** una estructura de datos de **cómo lo hace** (encapsulan la implementación).")

    st.divider()

    # ======= DEMO INTERACTIVA =======
    st.subheader("💻 Ejemplo interactivo: TDA Pila (Stack)")

    # Estado de la pila (simula los datos internos del TDA)
    if "pila" not in st.session_state:
        st.session_state.pila = []

    # Operaciones del TDA
    def apilar(elemento):
        st.session_state.pila.append(elemento)

    def desapilar():
        if st.session_state.pila:
            st.session_state.pila.pop()

    def ver_tope():
        if st.session_state.pila:
            return st.session_state.pila[-1]
        return None

    def vacia():
        return len(st.session_state.pila) == 0
    colA, colB,colC = st.columns(3)
    with colA:
        nuevo = st.text_input("Elemento a apilar", key="nuevo_elemento")
    # Interfaz
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ Apilar", use_container_width=True):
            if nuevo:
                apilar(nuevo)
    with col2:
        if st.button("➖ Desapilar", use_container_width=True):
            if vacia():
                st.warning("La pila está vacía.")
            else:
                desapilar()
    with col3:
        if st.button("🔄 Reiniciar", use_container_width=True):
            st.session_state.pila.clear()

    # Mostrar pila
    st.markdown("### 📦 Estado actual de la pila (de arriba hacia abajo):")

    if vacia():
        st.info("La pila está vacía.")
    else:
        for i, item in enumerate(reversed(st.session_state.pila), 1):
            st.code(f"[{i}] {item}", language="text")

    # Mostrar tope
    tope = ver_tope()
    if tope is not None:
        st.success(f"🧩 Tope de la pila: {tope}")

    st.caption("Este ejemplo muestra cómo se usa un TDA sin conocer su implementación interna.")

    st.divider()

    st.subheader("🧩 Otros ejemplos de TDAs comunes")
    st.markdown("""
- **Cola (Queue)** → primero en entrar, primero en salir (FIFO).  
- **Lista enlazada (Linked List)** → nodos conectados entre sí.  
- **Árbol (Tree)** → estructura jerárquica.  
- **Grafo (Graph)** → conjunto de nodos conectados por aristas.  
- **Diccionario / Mapa (Map)** → pares clave–valor.
""")
