import streamlit as st

def run():
    st.title("⚙️ Estructuras de Control")

    st.markdown("""
En el **paradigma imperativo**, un programa se ejecuta normalmente en **secuencia**, línea por línea.  
Pero para resolver problemas reales necesitamos:

- Tomar decisiones  
- Repetir acciones  
- Saltar acciones específicas  
- Detener iteraciones  
- Manejar errores  

A estas herramientas se las conoce como **estructuras de control**.
""")

    st.divider()

    # ================= CONDICIONALES =================
    st.subheader("🧭 Condicionales (`if`, `elif`, `else`)")
    st.markdown("""
Los condicionales permiten **ejecutar un bloque de código solo si se cumple una condición**.
""")

    st.code(
        "x = 10\n"
        "if x > 5:\n"
        "    print('Mayor que 5')\n"
        "else:\n"
        "    print('Menor o igual que 5')",
        language="python"
    )

    st.info("✅ Sirven para que el programa tome **decisiones**.")

    st.divider()

    # ================= BUCLES =================
    st.subheader("🔁 Bucles (`for` y `while`)")
    st.markdown("""
Los bucles permiten **repetir acciones** sin reescribir código.
""")

    st.code(
        "for i in range(3):\n"
        "    print('Iteración', i)",
        language="python"
    )

    st.code(
        "contador = 1\n"
        "while contador <= 3:\n"
        "    print(contador)\n"
        "    contador += 1",
        language="python"
    )

    st.info("✅ Permiten repetir tareas en secuencia controlada.")

    st.divider()

    # ================= BREAK / CONTINUE =================
    st.subheader("⬇️ `break` y `continue`")

    st.markdown("""
### `break`
Sale completamente del bucle.

### `continue`
Salta a la **siguiente iteración**, sin ejecutar el resto del bloque actual.
""")

    st.code(
        "for i in range(5):\n"
        "    if i == 3:\n"
        "        break     # rompe el bucle\n"
        "    print(i)",
        language="python",
    )

    st.code(
        "for i in range(5):\n"
        "    if i % 2 == 0:\n"
        "        continue  # salta pares\n"
        "    print(i)",
        language="python",
    )

    st.info("✅ Estas estructuras reemplazan los saltos arbitrarios que antes se hacían con `goto`.")

    st.divider()

    # ================= TRY / EXCEPT =================
    st.subheader("🧯 Manejo de errores (`try` / `except`)")
    st.markdown("""
Permite capturar **errores** y evitar que el programa termine abruptamente.
""")

    st.code(
        "try:\n"
        "    numero = int(input('Ingrese un número: '))\n"
        "    print('Doble:', numero * 2)\n"
        "except ValueError:\n"
        "    print('Debes ingresar un número válido.')",
        language="python"
    )

    st.info("✅ Esto reemplaza muchos usos antiguos de `goto` para manejar errores.")

    st.divider()

    # ================= DEMO INTERACTIVA =================
    st.subheader("💻 Demo interactiva: clasificación con control de flujo")

    st.markdown("La siguiente demo recorre una lista y usa `if`, `continue` y `break` para procesar elementos.")

    # Estado
    if "ctrl_iter" not in st.session_state:
        st.session_state.ctrl_iter = 0

    numeros = [1, -3, 2, 0, 9, -1]

    st.markdown("**Lista de valores:**")
    st.code(str(numeros), language="text")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("▶ Siguiente paso", use_container_width=True):
            if st.session_state.ctrl_iter < len(numeros):
                st.session_state.ctrl_iter += 1

    with col2:
        if st.button("🔄 Reiniciar", use_container_width=True):
            st.session_state.ctrl_iter = 0

    with col3:
        if st.button("⏭ Ejecutar todo", use_container_width=True):
            st.session_state.ctrl_iter = len(numeros)

    st.markdown("### Ejecución:")

    # Simulación lógica
    for i, n in enumerate(numeros[:st.session_state.ctrl_iter]):
        if n < 0:
            st.write(f"🔁 {n} es negativo → **continue** (se salta)")
            continue
        if n == 0:
            st.write(f"⛔ {n} es cero → **break** (fin del bucle)")
            break
        st.write(f"✅ {n} es positivo → se procesa normalmente")

    # Estado final
    if st.session_state.ctrl_iter == 0:
        st.info("Presioná 'Siguiente paso' para empezar.")
    elif st.session_state.ctrl_iter >= len(numeros):
        st.success("✅ Bucle completado.")

    st.divider()

    # ================= RESUMEN =================
    st.subheader("📖 Resumen general")
    st.markdown("""
Las **estructuras de control** permiten:

- Desviar el flujo normal (`if` / `else`)
- Repetir acciones (`for`, `while`)
- Controlar la repetición (`break`, `continue`)
- Manejar errores (`try` / `except`)

Son esenciales para organizar la lógica del programa de manera clara y estructurada.
""")

    st.caption("© 2025 — Horacio M. Albornoz")

# Ejecución individual
if __name__ == "__main__":
    run()
