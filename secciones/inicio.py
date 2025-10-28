import streamlit as st

def run():
    st.header("Paradigma imperativo")
    st.markdown("""
El **paradigma imperativo** es un estilo de programación que describe *cómo* debe ejecutarse un programa,
mediante **instrucciones que cambian el estado** del sistema paso a paso.

Es decir, el programador le dice a la computadora **qué hacer y en qué orden**.
""")
# ---- Características clave ----
    st.subheader("🔑 Características principales")
    st.markdown("""
    - **Secuencialidad** → las instrucciones se ejecutan una detrás de otra.
    - **Asignación de variables** → se modifica el estado del programa.
    - **Estructuras de control** → `if`, `for`, `while` para tomar decisiones o repetir tareas.
    - **Enfoque en *cómo* hacerlo** más que en *qué* se quiere lograr.
    """)

    st.info("👉 El paradigma imperativo es la base de muchos lenguajes modernos y es el más usado para enseñar programación.")
    st.subheader("Ejemplo Imperativo paso a paso")

    # Programa de ejemplo
    program = [
        "suma = 0",                
        "i = 1",                   
        "while i <= 5:",           
        "    suma = suma + i",     
        "    i = i + 1",           
        "print('La suma es:', suma)" 
    ]

    # --- Estado persistente ---
    if "pc" not in st.session_state:
        st.session_state.pc = 0
    if "env" not in st.session_state:
        st.session_state.env = {"suma": None, "i": None}
    if "out" not in st.session_state:
        st.session_state.out = []
    if "done" not in st.session_state:
        st.session_state.done = False

    # --- Render del código en bloque st.code ---
    def render_code(program, pc):
        bloque = ""
        for idx, line in enumerate(program):
            if idx == pc and not st.session_state.done:
                bloque += f">>> {line}    # ← línea actual\n"
            else:
                bloque += f"    {line}\n"
        return bloque

    st.code(render_code(program, st.session_state.pc), language="python")

    # --- Controles ---
    c1, c2 = st.columns([1,1])
    with c1:
        if st.button("▶ Siguiente", use_container_width=True, disabled=st.session_state.done):
            pc = st.session_state.pc
            env = st.session_state.env

            if pc == 0:  # suma = 0
                env["suma"] = 0
                st.session_state.pc = 1
            elif pc == 1:  # i = 1
                env["i"] = 1
                st.session_state.pc = 2
            elif pc == 2:  # while
                if env["i"] <= 5:
                    st.session_state.pc = 3
                else:
                    st.session_state.pc = 5
            elif pc == 3:  # suma = suma + i
                env["suma"] += env["i"]
                st.session_state.pc = 4
            elif pc == 4:  # i = i + 1 (y volver al while)
                env["i"] += 1
                st.session_state.pc = 2
            elif pc == 5:  # print
                st.session_state.out.append(f"La suma es: {env['suma']}")
                st.session_state.done = True

    with c2:
        if st.button("🔄 Reiniciar", use_container_width=True):
            st.session_state.pc = 0
            st.session_state.env = {"suma": None, "i": None}
            st.session_state.out = []
            st.session_state.done = False

    # --- Estado actual ---
    st.subheader("Estado de ejecución")
    st.write("**suma:**", st.session_state.env["suma"])
    st.write("**i:**", st.session_state.env["i"])
    st.write("**Salida:**", st.session_state.out if st.session_state.out else "—")