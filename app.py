import streamlit as st
# from streamlit_ace import st_ace  # si lo usás en otras secciones
from secciones import variables, lifetime, mutabilidad, staticvsdynamic, scope, inicio
# from secciones import paradigma  # si tenés módulo para “Paradigma imperativo”

st.set_page_config(page_title="TP Programación", page_icon="🧪", layout="wide")

SECCIONES = [
    "Inicio",
    "Paradigma imperativo",
    "Variables",
    "Lifetime",
    "Mutabilidad",
    "Static vs dynamic",
    "Scope",
]

# ------------------ Estado de navegación sin pelear con el radio ------------------
if "current_page" not in st.session_state:
    st.session_state.current_page = "Inicio"

def go(section: str):
    """Cambiar de sección desde botones/link en la UI."""
    if section in SECCIONES:
        st.session_state.current_page = section
        st.rerun()

# ------------------ Sidebar: radio SIN key, index controlado ------------------
side_idx = SECCIONES.index(st.session_state.current_page)
nav_choice = st.sidebar.radio("Secciones", SECCIONES, index=side_idx)
# Si el usuario cambia manualmente en el radio, actualizamos nuestro estado:
if nav_choice != st.session_state.current_page:
    st.session_state.current_page = nav_choice
    st.rerun()

# ------------------ Contenido ------------------
page = st.session_state.current_page

if page == "Inicio":
    st.title("TP Programación 1 — Página Inicial")
    st.markdown("**Autor:** Horacio M. Albornoz")
    st.markdown("---")

    st.subheader("🎯 Objetivo del proyecto")
    st.markdown("""
Este proyecto presenta, de forma **didáctica y resumida**, algunos de los **conceptos clave de Programación 1**,
combinando **explicaciones teóricas** con **demos interactivas**.
""")
    st.markdown("---")

    st.subheader("📚 Secciones")
    st.caption("Hacé clic para navegar:")

    items = [
        ("Paradigma imperativo", "Introducción y ejemplo paso a paso (ejecución secuencial y estado)."),
        ("Variables", "Definición, estructura (nombre, tipo, valor, dirección) y ejemplos."),
        ("Lifetime", "Ciclo de vida de una variable: creación, uso y desasignación."),
        ("Mutabilidad", "Diferencias entre tipos mutables/inmutables y efectos al pasar a funciones."),
        ("Static vs dynamic", "Tipado estático vs dinámico: diferencias y cuándo conviene cada uno."),
        ("Scope", "Alcance (LEGB) con demo interactiva: global, local y sombreado."),
    ]

    for nombre, desc in items:
        c1, c2 = st.columns([2, 6])
        with c1:
            if st.button(f"→ {nombre}", key=f"btn_{nombre}", use_container_width=True):
                go(nombre)
        with c2:
            st.write(desc)

    st.markdown("---")

    st.caption("© 2025 — Horacio M. Albornoz")

elif page == "Paradigma imperativo":
    st.header("📘 Paradigma imperativo")
    st.write("Pegá aquí tu demo paso a paso con `st.code` y resaltado de línea.")
    inicio.run()  # si tenés un módulo

elif page == "Variables":
    variables.run()

elif page == "Lifetime":
    lifetime.run()

elif page == "Mutabilidad":
    mutabilidad.run()

elif page == "Static vs dynamic":
    staticvsdynamic.run()

elif page == "Scope":
    scope.run()
