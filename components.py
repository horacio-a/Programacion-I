
import streamlit as st
def code_and_run(py_code, runner):
    col1, col2 = st.columns([2, 1])
    with col1:
        st.code(py_code, language="python")
    with col2:
        st.caption("Salida")
        runner()