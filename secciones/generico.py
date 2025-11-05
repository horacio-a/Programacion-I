import streamlit as st
from typing import TypeVar, Generic, List

def run():
    st.title("Tipos Genéricos en Programación")

    # ======= TEORÍA =======
    st.subheader("¿Qué es un tipo genérico?")
    st.markdown(
        """
Un **tipo genérico** permite escribir código que funcione con **diferentes tipos de datos**  
sin tener que duplicar funciones o clases.

👉 En lugar de definir versiones separadas para `int`, `float` o `str`,  
un tipo genérico **usa un parámetro de tipo** que se reemplaza en tiempo de ejecución.

Esto es muy común en lenguajes **estáticamente tipados** (como Java, C++ o TypeScript),  
pero Python también lo soporta a través del módulo `typing`.

**Ejemplo:**
"""
    )

    st.code(
        "from typing import TypeVar\n\n"
        "T = TypeVar('T')  # T puede ser cualquier tipo\n\n"
        "def duplicar(valor: T) -> list[T]:\n"
        "    return [valor, valor]\n\n"
        "print(duplicar(5))      # [5, 5]\n"
        "print(duplicar('hola')) # ['hola', 'hola']",
        language="python"
    )

    st.markdown(
        """
En este ejemplo, `T` representa un **tipo genérico**:  
la función `duplicar()` puede recibir y devolver **cualquier tipo de dato**,  
siempre conservando el mismo tipo de entrada y salida.
"""
    )

    st.info("Los tipos genéricos hacen el código más **flexible**, **seguro** y **reutilizable**.")

    st.divider()

    # ======= DEMO INTERACTIVA =======
    st.subheader("Demo interactiva: función genérica en acción")

    st.markdown(
        "Probá una función genérica `duplicar()` con distintos tipos de valores:"
    )

    # Estado de ejemplo
    tipo = st.selectbox("Seleccioná el tipo de dato:", ["Número", "Texto", "Lista"])
    entrada = None

    if tipo == "Número":
        entrada = st.number_input("Ingresá un número", value=5)
    elif tipo == "Texto":
        entrada = st.text_input("Ingresá un texto", value="Hola")
    elif tipo == "Lista":
        entrada = st.text_area("Ingresá una lista (separada por comas)", value="1, 2, 3")

    # Función genérica simulada
    def duplicar_generico(valor):
        return [valor, valor]

    if st.button("🚀 Duplicar valor", use_container_width=True):
        if tipo == "Lista":
            try:
                lista = [v.strip() for v in entrada.split(",")]
                st.success(f"Resultado: {duplicar_generico(lista)}")
            except Exception:
                st.error("Formato de lista inválido.")
        else:
            st.success(f"Resultado: {duplicar_generico(entrada)}")

    st.divider()

    # ======= MÁS EJEMPLOS =======
    st.subheader("🔧 Otros ejemplos de tipos genéricos")

    st.markdown(
        """
Podemos usar genéricos para construir **clases o estructuras** que manejen distintos tipos:

```python
from typing import TypeVar, Generic, List
T = TypeVar('T')

class Caja(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []

    def agregar(self, elemento: T):
        self.elementos.append(elemento)

    def obtener_todos(self) -> List[T]:
        return self.elementos

# Caja de enteros
caja_int = Caja[int]()
caja_int.agregar(10)
caja_int.agregar(20)

# Caja de textos
caja_str = Caja[str]()
caja_str.agregar("hola")
caja_str.agregar("mundo")
# Esto nos permite tener una sola clase que puede trabajar con distintos tipos sin perder consistencia.
"""
)
    st.success("En resumen: un tipo genérico permite escribir una única definición reutilizable para múltiples tipos de datos.")

