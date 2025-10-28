import streamlit as st


def run():
    st.header("📘 Tipado estático vs Tipado dinámico")
    st.write('En programación, el **tipo de dato** de una variable puede manejarse de dos formas principales:')

        
    

    col1, col2 = st.columns(2)

    with col1:
        st.subheader('Tipado estático')

        st.markdown("""
       - El tipo de la variable se **declara y fija en tiempo de compilación**.  
       - Una vez definido, no se puede cambiar.  
       - Ejemplos: C, Java, C++ (aunque algunos permiten genéricos o inferencia).  
    """)
        st.code("""
int numero = 10;      // tipo int declarado explícitamente
                
numero = 1;      // Se le asigna 1 a la variable numero
numero = "texto";     // ❌ Error: no se puede asignar string a int
""", language="java")
        st.markdown("""
    - **Tipado estático es util:**  
      - En proyectos grandes y críticos (bancos, sistemas embebidos, aplicaciones de misión crítica).  
      - Permite encontrar errores de tipo **antes de ejecutar el programa**.  
      - Ayuda al rendimiento porque el compilador optimiza el uso de memoria.  
    """)

    with col2:
        st.subheader('**Tipado dinámico**  ')
        st.markdown("""
    
       - El tipo de la variable se **determina en tiempo de ejecución**.  
       - Una misma variable puede cambiar de tipo durante el programa.  
       - Ejemplos: Python, JavaScript, Ruby.
    """)
        st.code("""
x = 10          # inicialmente entero
print(type(x))  # <class 'int'>
x = "texto"     # ahora es string
print(type(x))  # <class 'str'>""", language="python")
        
        st.markdown("""
    - **Tipado dinámico es util**  
      - Para prototipado rápido, scripting, ciencia de datos o proyectos educativos.  
      - Brinda **flexibilidad y rapidez de desarrollo**.  
      - Ideal cuando se necesita experimentar o manipular datos heterogéneos.  
    """)


        
