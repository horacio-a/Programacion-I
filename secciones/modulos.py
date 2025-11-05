# secciones/modulos.py
import streamlit as st
import modulos.banco as banco  # ← import real del módulo

def run():
    st.title("Módulos y Encapsulamiento (con módulo real)")

    # ========= Teoría breve =========
    st.subheader("¿Qué es un módulo?")
    st.markdown("""
Un **módulo** es un **archivo `.py`** que agrupa **funciones, clases y variables** relacionadas.
Sirve para **organizar**, **reutilizar** y **mantener** mejor el código.
""")

    st.code(
        "# archivo: matematicas.py\n"
        "def sumar(a, b):\n"
        "    return a + b\n",
        language="python"
    )

    st.code(
        "# archivo: app.py\n"
        "import matematicas\n\n"
        "print(matematicas.sumar(3, 4))  # 7\n",
        language="python"
    )

    st.subheader("Encapsulamiento (idea clave)")
    st.markdown("""
El **encapsulamiento** consiste en **ocultar detalles internos** y exponer una **interfaz pública**.
En Python, por **convención**, los nombres que comienzan con **`_`** se tratan como **privados**.
""")

    st.code(
        "# archivo: cuenta.py\n"
        "_saldo = 0  # 'privado' por convención\n\n"
        "def depositar(monto):\n"
        "    global _saldo\n"
        "    _saldo += monto\n\n"
        "def ver_saldo():\n"
        "    return _saldo\n",
        language="python"
    )

    st.info("La idea: otras partes del programa usan funciones públicas sin tocar los datos internos directamente.")

    st.divider()

    # ========= Demo con módulo real =========
    st.subheader("Usando el módulo real `modulos/banco.py`")

    col1, col2, col3 = st.columns(3)
    with col1:
        monto_dep = st.number_input("Depositar", min_value=0, step=10, key="monto_dep_real")
        if st.button("➕ Depositar", use_container_width=True):
            banco.depositar(monto_dep)
    with col2:
        monto_ret = st.number_input("Retirar", min_value=0, step=10, key="monto_ret_real")
        if st.button("➖ Retirar", use_container_width=True):
            ok = banco.retirar(monto_ret)
            if not ok:
                st.warning("Saldo insuficiente.")
    with col3:
        if st.button("🔄 Reiniciar saldo", use_container_width=True):
            banco.reiniciar()

    st.metric("💰 Saldo (desde el MÓDULO real)", f"${banco.ver_saldo():,}")

    st.caption("Interactuás mediante funciones **del módulo real** (`depositar`, `retirar`, `ver_saldo`, `reiniciar`). No accedés a `_saldo`.")

    st.divider()

    # Mostrar el código real del módulo (lectura del archivo)
    with st.expander("📄 Ver código actual de modulos/banco.py"):
        try:
            with open("modulos/banco.py", "r", encoding="utf-8") as f:
                st.code(f.read(), language="python")
        except Exception as e:
            st.error(f"No pude leer modulos/banco.py: {e}")
