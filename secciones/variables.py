import ast
import streamlit as st
from streamlit_ace import st_ace

def run():

    st.title("Funcionamiento de las variables")

    st.markdown(
        "<p style='font-size:18px;'>"
        "En programación, una <b>variable</b> es un espacio de memoria identificado por un nombre. "
        "Su función es almacenar un valor que puede ser usado y modificado durante la ejecución de un programa."
        "</p>",
        unsafe_allow_html=True
    )

    st.subheader("Estructura de una variable:")
    st.markdown("""
    - **Nombre**: identificador con el que el programador accede a la variable.
    - **Tipo de dato**: determina qué clase de valores puede guardar (por ejemplo: enteros, cadenas de texto, booleanos, objetos).
    - **Valor**: contenido almacenado en ese momento dentro de la variable.
    - **Dirección de memoria**: aunque normalmente no es visible para el programador, toda variable está asociada a una posición específica en la memoria del sistema.
    """)

    st.subheader("Python específicamente:")
    st.markdown(
        "<p style='font-size:18px;'>En Python, cuando declaramos o usamos una variable ocurren dos procesos:</p>"
        "<ul>"
        "<li><div><b>El nombre</b> de la variable se registra en un <i>namespace</i>, que funciona como una libreta donde se anotan todos los nombres existentes en ese momento.</div></li>"
        "<li><div><b>El objeto real</b> (número, texto, lista, etc.) se guarda en el <i>heap</i>, una zona de memoria donde residen los datos.</div></li>"
        "</ul>"
        "<p style='font-size:18px;'>La relación es que el nombre escrito en la libreta (<i>namespace</i>) apunta al objeto almacenado en el <i>heap</i>. "
        "De este modo, una variable no <i>contiene</i> directamente el valor, sino que funciona como una <b>etiqueta</b> que señala al objeto verdadero en memoria.</p>",
        unsafe_allow_html=True
    )

    st.subheader('Mira como guardan:')

    # col1, col2, col3 = st.columns(3)
    # with col1:
    #     st.write('Aqui escribe las variables que quieras')
    #     content = st_ace(
    #     language="python",
    #     theme="github",
    #     key="ace",
    #     auto_update=True
    #     )
    #     print(content)
    # with col2:
    #     st.write('namespace')
    #     st.code(content, language="python")
       

    # with col3:
    #     st.write('heap')
    #     st.code(content, language="python")
    st.title("💻 Demo: Variables definidas y sus valores")

    # --- Editor ---
    code = st_ace(
        language="python",
        theme="github",
        height=260,
        key="ace_editor",
        placeholder="# Escribe código Python aquí...\n"
                   "# Ejemplos:\n"
                   "# x = 10\n# nombre = 'Ana'\n# lista = [1, 2, 3]\n# (y := 5)\n"
    )

    # --- Detección de variables con AST (opcional pero útil para avisar errores de sintaxis) ---
    def assigned_names(src: str):
        try:
            tree = ast.parse(src or "")
        except SyntaxError as e:
            return set(), f"❌ Error de sintaxis: {e}"
        names = set()
        def collect(t):
            if isinstance(t, ast.Name):
                names.add(t.id)
            elif isinstance(t, (ast.Tuple, ast.List)):
                for c in t.elts: collect(c)
        for n in ast.walk(tree):
            if isinstance(n, ast.Assign):
                for t in n.targets: collect(t)
            elif isinstance(n, ast.AnnAssign):
                collect(n.target)
            elif isinstance(n, ast.AugAssign):
                collect(n.target)
            elif isinstance(n, ast.For):
                collect(n.target)
            elif isinstance(n, ast.With):
                for item in n.items:
                    if item.optional_vars is not None: collect(item.optional_vars)
            elif hasattr(ast, "NamedExpr") and isinstance(n, ast.NamedExpr):
                collect(n.target)
        return names, None

    vars_def, parse_err = assigned_names(code)

    col1, col2 = st.columns(2)

    
    with col1:
        if code.strip() and not parse_err:
            st.subheader('Head')
            # Builtins seguros mínimos
            SAFE_BUILTINS = {
                "range": range, "len": len, "print": print, "sum": sum, "min": min, "max": max,
                "abs": abs, "enumerate": enumerate, "zip": zip, "map": map, "filter": filter,
                "list": list, "dict": dict, "set": set, "tuple": tuple,
            }
            g = {"__builtins__": SAFE_BUILTINS}
            l = {}

            try:
                exec(code, g, l)  # ejecuta el código del usuario en entorno aislado

                # Filtrar “variables del usuario”: ignorar dunders/privadas
                rows = []
                for name, val in sorted(l.items()):
                    if name.startswith("_"):  # ignora __algo__ o _tmp
                        continue
                    try:
                        rep = repr(val)
                        if len(rep) > 200:
                            rep = rep[:197] + "..."
                    except Exception:
                        rep = "<no-repr>"
                    rows.append({"id":"13925---0","Type": type(val).__name__,"repr":rep,"depth":0})

                if rows:
                    st.dataframe(rows, use_container_width=True)
                else:
                    st.info("No se encontraron variables definidas tras la ejecución.")
            except Exception as e:
                st.error(f"Error al ejecutar el código: {e}")
        elif not code.strip():
            st.info("Escribe algo de código arriba para analizar y ejecutar.")

    with col2:
        if code.strip() and not parse_err:
            st.subheader('Namespace')

            # Builtins seguros mínimos
            SAFE_BUILTINS = {
                "range": range, "len": len, "print": print, "sum": sum, "min": min, "max": max,
                "abs": abs, "enumerate": enumerate, "zip": zip, "map": map, "filter": filter,
                "list": list, "dict": dict, "set": set, "tuple": tuple,
            }
            g = {"__builtins__": SAFE_BUILTINS}
            l = {}

            try:
                exec(code, g, l)  # ejecuta el código del usuario en entorno aislado

                # Filtrar “variables del usuario”: ignorar dunders/privadas
                rows = []
                for name, val in sorted(l.items()):
                    if name.startswith("_"):  # ignora __algo__ o _tmp
                        continue
                    try:
                        rep = repr(val)
                        if len(rep) > 200:
                            rep = rep[:197] + "..."
                    except Exception:
                        rep = "<no-repr>"
                    rows.append({"id":"13925---0","Name": name, "Type": type(val).__name__,"scope":'global'})
                if rows:
                    st.dataframe(rows, use_container_width=True)
                else:
                    st.info("No se encontraron variables definidas tras la ejecución.")
            except Exception as e:
                st.error(f"Error al ejecutar el código: {e}")
        elif not code.strip():
            st.info("Escribe algo de código arriba para analizar y ejecutar.")

