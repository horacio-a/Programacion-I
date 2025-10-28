import streamlit as st
from components import code_and_run


def run():
    st.header("🌎 Alcance de las variables (Scope)")

    st.markdown("""
    En programación, el **scope** (alcance) define **dónde** una variable puede ser accedida o modificada.

    En **Python** se aplica la regla **LEGB**:
    1. **Local** → dentro de una función.
    2. **Enclosing** → en funciones anidadas.
    3. **Global** → variables declaradas en el archivo principal.
    4. **Built-in** → nombres reservados de Python.

    👉 Una variable puede existir en un ámbito (scope) pero no en otro y una variable puede sombrear otra.
    """)

    # ----------- DEMO INTERACTIVA -----------
    col1, col2 = st.columns(2)
    with col1:
        initialX = st.number_input("**x** global", value=5, step=1)
    # with col2:
    #     initialY = st.number_input("**y** local", value=5, step=1)
    # Estado inicial
    cola1, cola2,cola3  = st.columns(3)

    with col2:
        # st.markdown("**Utiliza este boton para eliminar el x local**")   # se ve como label
        # st.caption("Este es un label tipo caption")
        st.markdown(
            """
            <div style="
                font-family: 'Source Sans', sans-serif;
                font-size: 0.875rem;
                color: inherit;
                max-width: 100%;
                overflow-wrap: break-word;
                margin-bottom:6px;
            ">
                Texto con estilos aplicados
            </div>
            """,
            unsafe_allow_html=True
        )
        if "activo" not in st.session_state:
            st.session_state.activo = True

        def toggle_activo():
            st.session_state.activo = not st.session_state.activo

        # El texto depende del estado, pero el widget tiene un KEY ESTABLE
        label = "Desactivar" if st.session_state.activo else "Activar"

        st.button(
            label,
            key="toggle_btn",              # <-- clave para que no se 'reinvente' el widget al cambiar el label
            on_click=toggle_activo,        # <-- mutamos estado en callback, bien sincronizado
            type="primary",
            use_container_width=True
        )
    # with cola3:
    #     st.markdown(
    #     f"<div style='text-align: right;'>Estado actual:" \
    #     f"{st.session_state.activo}"
    #     f"</div>",
    #     unsafe_allow_html=True
    # )

 
    if st.session_state.activo:
        code = f"""x = {int(initialX)}

def f():
    x = 1000
    y_local = "Y local"
    return {{x: x, y: y_local}}

print("f() ->", f())    # 99
print("global x ->", x) # 5
    """
    else:
        code = f"""x = {int(initialX)}

def f():
    #x = 1000
    #y_local = "Y local"
    return x

print("f() ->", f())    # 99
print("global x ->", x) # 5
    """
    def run():

            
            x = int(initialX)
            sta= st.session_state
            print(sta)
            def f():
                if st.session_state.activo:
                    x_local = 1000
                    y_local = "Y local"
                    return {"x": x_local, "y": y_local}
                else:
                    return {"x": x, "y": "No existe y"}

                
            st.info(f"Valor de la x local de f() → **{f()['x']}**")
            st.info(f"Valor de la y local de f() → **{f()['y']}**")
            st.info(f"Valor de la x global → **{x}**")
    code_and_run(code, run)