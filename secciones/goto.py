import streamlit as st

def run():
    st.title("El GOTO y por qué dejó de usarse")

    # =============== TEORÍA ===============
    st.subheader("¿Qué es el GOTO?")
    st.markdown(
        """
`GOTO` es una instrucción que existía en muchos lenguajes antiguos.  
Sirve para **saltar la ejecución** del programa a **otra línea o etiqueta** de forma directa.

Ejemplo en pseudocódigo:
"""
    )

    st.code(
        "x = 0\n"
        "inicio:\n"
        "x = x + 1\n"
        "print(x)\n"
        "if x < 5:\n"
        "    goto inicio",
        language="python"
    )

    st.markdown(
        """
Esto funciona, pero crea un **salto incontrolado** dentro del programa,  
lo que puede generar código difícil de leer, seguir y mantener.

A este caos se lo llamó **“espagueti code”**, porque el flujo de ejecución queda lleno de idas y vueltas.
"""
    )

    st.info("👉 GOTO permite saltar a cualquier parte del programa, rompiendo la estructura lógica del flujo.")

    st.divider()

    # =============== POR QUÉ YA NO SE USA ===============
    st.subheader("¿Por qué ya no se usa en lenguajes modernos?")
    st.markdown(
        """
Los problemas del `GOTO` llevaron a la creación de lenguajes en los que la estructura del programa  
**debe ser clara, ordenada y predecible**.

Los motivos principales:
- **Hace el código difícil de leer** (los saltos no son obvios).
- **Complica el mantenimiento** (cualquier cambio puede romper la lógica).
- **Rompe la secuencialidad** del paradigma imperativo.
- **Genera errores difíciles de detectar**.

En 1968, Edsger Dijkstra publicó “**Go To Statement Considered Harmful**”,  
marcando formalmente el inicio del rechazo a esta instrucción.
"""
    )

    st.success("Hoy, las estructuras de control reemplazan completamente al GOTO.")

    st.divider()

    # =============== ESTRUCTURAS QUE LO REEMPLAZAN ===============
    st.subheader("¿Qué se usa hoy en lugar del GOTO?")
    st.markdown("Lenguajes modernos reemplazaron `GOTO` con estructuras claras y seguras:")

    st.markdown(
        """
### 1. **Condicionales (`if`, `elif`, `else`)**
Permiten tomar decisiones sin saltos arbitrarios.

### 2. **Bucles (`for`, `while`)**
Permiten repetir acciones sin tener que volver manualmente a otra parte del código.

### 3. **Funciones**
Permiten encapsular lógica y “saltar” solo mediante llamadas ordenadas.

### 4. **Estructuras de control como `break`, `continue`**
Reemplazan comportamientos específicos de GOTO sin romper el flujo global.

### 5. **Excepciones (`try/except`)**
Reemplazan los saltos para manejar errores.
"""
    )

    st.divider()

    # =============== COMPARACIÓN PROGRAMAS ===============
    st.subheader(" Comparación: con GOTO vs sin GOTO")

    st.markdown("**Con GOTO (pseudocódigo):**")
    st.code(
        "i = 0\n"
        "inicio:\n"
        "i = i + 1\n"
        "print(i)\n"
        "if i < 5:\n"
        "    goto inicio",
        language="python"
    )

    st.markdown("**Sin GOTO (Python moderno):**")
    st.code(
        "for i in range(1, 6):\n"
        "    print(i)",
        language="python"
    )

    st.info("El segundo ejemplo es más corto, más claro y más seguro.")


# Permite ejecución directa
if __name__ == '__main__':
    run()
