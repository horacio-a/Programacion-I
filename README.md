# 🧪 TP Programación 1 — Demos Interactivas en Streamlit

Este proyecto es un **Trabajo Práctico de Programación 1**, desarrollado con **[Streamlit](https://streamlit.io/)**.  
El objetivo es **explicar conceptos fundamentales de la programación** de manera **didáctica e interactiva**, a través de pequeñas demos visuales y ejemplos ejecutables.

---

## 📖 Objetivo

La aplicación busca presentar, de forma **minimalista** y **resumida**, algunos de los conceptos clave de la programación imperativa.

Cada sección combina **teoría resumida** con **ejemplos prácticos interactivos**.

---

## 🛠️ Tecnologías utilizadas

- **Python 3.11+**
- **Streamlit**
- **streamlit-ace** (editor de código embebido)
- Módulos propios en carpeta `secciones/` para organizar el contenido.

---

## 📂 Estructura del proyecto

- **app.py** → Script principal con la navegación (sidebar + radio).  
- **secciones/** → Módulos de cada sección teórica y práctica:  
  - `inicio.py`: Página inicial con objetivo y explicación general.  
  - `variables.py`: Explicación y ejemplos sobre variables.  
  - `lifetime.py`: Ciclo de vida de una variable.  
  - `mutabilidad.py`: Diferencias entre mutables e inmutables.  
  - `staticvsdynamic.py`: Tipado estático vs dinámico.  
  - `scope.py`: Alcance (scope) de variables + demo interactiva.  
- **components/** → Componentes auxiliares reutilizables.  
  - `code_and_run.py`: Muestra código junto con su ejecución en la app.  

---

## 🚀 Cómo ejecutar el proyecto

1. Clonar el repositorio:
   git clone https://github.com/horacio-a/Programacion-I.git
   cd /Programacion-I

2. Crear y activar un entorno virtual (opcional, pero recomendado):
   python -m venv .venv
   source .venv/bin/activate # Linux/Mac
   .venv\Scripts\activate # Windows

3. Instalar dependencias:
   pip install -r requirements.txt

4. Ejecutar la aplicación:
   streamlit run app.py

5. Abrir el navegador en: http://localhost:8501

---

## 🎮 Uso

- Utilizá la **barra lateral (sidebar)** para navegar entre las secciones disponibles.
- En la sección **Inicio**, vas a encontrar una descripción general del proyecto y accesos rápidos a cada demo.
- Cada sección contiene:
  - Explicaciones teóricas resumidas.
  - Ejemplos de código en **Python**.
  - **Demos interactivas** para experimentar y comprender los conceptos en acción.

---

## 👨‍💻 Autor

**Horacio M. Albornoz**  
Trabajo Práctico de la materia **Programación 1**

---

## 📜 Licencia

Este proyecto se distribuye con fines **educativos**.  
Podés usarlo como referencia o base para tus propios **trabajos prácticos** o proyectos de aprendizaje.
