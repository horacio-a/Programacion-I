import streamlit as st
import time, sys, gc

def run():
    st.header("Ciclo de vida de las variables")
    st.markdown(
        "<p style='font-size:18px;'>El ciclo de vida de una variable describe todas las etapas por las que pasa una variable desde que es creada hasta que se elimina de la memoria. Generalmente incluye:</p>",
        unsafe_allow_html=True
    )
    st.markdown("""
    1. **Declaración / Definición** → cuando se le asigna un nombre en el programa.
    2. **Asignación** → cuando ese nombre se vincula con un valor almacenado en memoria.
    3. **Uso** → la variable es utilizada por el programa (lectura, modificación, operaciones).
    4. **Desasignación** → cuando deja de ser accesible y el espacio de memoria ocupado se libera.
    """)
    st.markdown(
        "<p style='font-size:18px;'>Dentro de la etapa final del ciclo de vida de una variable, existe una diferencia significativa según el lenguaje de programación. En el proceso de desasignación, podemos distinguir dos casos claramente distintos:</p>",
        unsafe_allow_html=True
    )
    st.markdown("""
    - En lenguajes **con garbage collector** (como Python o Java), la memoria se libera automáticamente cuando el objeto deja de usarse.
    - En lenguajes **sin garbage collector** (como C o C++), el programador debe liberar la memoria manualmente.
    """)
    st.subheader("GC vs Manual")
    
    size_kb = st.slider("Tamaño del objeto (KB)", 64, 1024, 256, help="Usado en ambas columnas")

    col_gc, col_manual = st.columns(2)

    # ===========================
    # Columna 1: GC (auto-liberación con countdown)
    # ===========================
    with col_gc:
        st.subheader("Con Garbage Collector (auto)")
        delay = st.number_input("Liberar automáticamente en (segundos)", 1, 10, 3, help="Cuenta regresiva y luego se suelta la referencia")

        # Estado para esta columna
        if "gc_obj" not in st.session_state:
            st.session_state.gc_obj = None
        if "gc_created_at" not in st.session_state:
            st.session_state.gc_created_at = None
        if "gc_freed_at" not in st.session_state:
            st.session_state.gc_freed_at = None

        # Crear y liberar automáticamente después de 'delay' segundos
        if st.button("➕ Crear y liberar automáticamente", use_container_width=True):
            # 1) Crear objeto “pesado”
            st.session_state.gc_obj = bytearray(size_kb * 1024)
            st.session_state.gc_created_at = time.time()
            st.session_state.gc_freed_at = None

            # 2) Mostrar countdown bloqueante (simple para demo)
            ph = st.empty()
            for remaining in range(int(delay), -1, -1):
                ph.metric("Liberación en", f"{remaining}s")
                time.sleep(1)

            # 3) Soltar referencia y pedir GC (simula que el runtime recolecta)
            del st.session_state.gc_obj
            st.session_state.gc_obj = None
            gc.collect()
            st.session_state.gc_freed_at = time.time()

        # Estado/metricas
        bytes_live = 0 if st.session_state.gc_obj is None else sys.getsizeof(st.session_state.gc_obj)
        st.metric("Memoria (objeto vivo)", f"{bytes_live/1024:.1f} KB")
        st.write("**Creado:**", 
                 time.strftime("%H:%M:%S", time.localtime(st.session_state.gc_created_at)) 
                 if st.session_state.gc_created_at else "—")
        st.write("**Liberado automáticamente:**", 
                 time.strftime("%H:%M:%S", time.localtime(st.session_state.gc_freed_at)) 
                 if st.session_state.gc_freed_at else "—")
        st.caption("En esta demo, tras el countdown se suelta la última referencia y se invoca GC → el objeto queda elegible y se libera.")

    # ===========================
    # Columna 2: Sin GC (manual)
    # ===========================
    with col_manual:
        st.subheader("Sin GC (liberación manual)")
        # Estado para esta columna
        if "manual_obj" not in st.session_state:
            st.session_state.manual_obj = None
        if "manual_created_at" not in st.session_state:
            st.session_state.manual_created_at = None
        if "manual_freed_at" not in st.session_state:
            st.session_state.manual_freed_at = None

        c1, c2 = st.columns(2)
        with c1:
            if st.button("➕ Crear objeto (manual)", use_container_width=True):
                st.session_state.manual_obj = bytearray(size_kb * 1024)
                st.session_state.manual_created_at = time.time()
                st.session_state.manual_freed_at = None
        with c2:
            if st.button("🧹 Liberar manualmente", use_container_width=True):
                del st.session_state.manual_obj
                st.session_state.manual_obj = None
                st.session_state.manual_freed_at = time.time()

        # Estado/metricas
        m_bytes = 0 if st.session_state.manual_obj is None else sys.getsizeof(st.session_state.manual_obj)
        st.metric("Memoria (objeto vivo)", f"{m_bytes/1024:.1f} KB")
        st.write("**Creado:**", 
                 time.strftime("%H:%M:%S", time.localtime(st.session_state.manual_created_at)) 
                 if st.session_state.manual_created_at else "—")
        st.write("**Liberado manualmente:**", 
                 time.strftime("%H:%M:%S", time.localtime(st.session_state.manual_freed_at)) 
                 if st.session_state.manual_freed_at else "—")
        st.caption("Aquí la memoria no se libera “sola”: queda viva hasta que presionás **Liberar manualmente**.")