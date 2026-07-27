<p align="center">

# 🤖 Black_Ary Knowledge AI

### Enterprise Intelligent Assistant powered by Artificial Intelligence

*Technology Inspired by Trust and the Future.*

</p>

---

# 📖 Descripción

**Black_Ary Knowledge AI** es un asistente inteligente empresarial desarrollado para responder consultas sobre documentos internos utilizando técnicas de **Retrieval-Augmented Generation (RAG)**.

El sistema combina búsqueda semántica con Inteligencia Artificial Generativa para entregar respuestas precisas, rápidas y fundamentadas en la documentación corporativa.

---

# ✨ Características

- 🤖 Chat inteligente empresarial
- 📄 Consulta de documentos PDF y Word
- 🧠 Búsqueda semántica mediante FAISS
- 🔍 Recuperación inteligente de información (RAG)
- 🚀 Integración con Google Gemini
- 💬 Interfaz moderna desarrollada con Streamlit
- 📚 Visualización de fuentes consultadas
- ⚡ Carga optimizada mediante caché

---

# 🏗 Arquitectura

```text
                    Usuario
                       │
                       ▼
             Black_Ary Knowledge AI
                  (Streamlit)
                       │
                       ▼
                 RAG Pipeline
             ┌───────────────────┐
             │                   │
             ▼                   ▼
        FAISS Vector DB     Google Gemini
             │
             ▼
   Documentos Corporativos
   PDF • DOCX • Manuales
```

---

# 📂 Estructura del Proyecto

```text
Enterprise-Knowledge-Agent/

│
├── app.py
├── rag_agent.py
├── config.py
├── requirements.txt
├── README.md
│
├── documents/
│
├── embeddings/
│
├── images/
│     ├── logo_blackary.png
│     ├── banner_blackary.png
│     ├── screenshot_home.png
│     └── screenshot_chat.png
│
└── vectorstore/
```

---

# 🧪 Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-------------------------------|
| 🐍 Python | Lenguaje principal |
| 🤖 Google Gemini | Modelo LLM |
| 🦜 LangChain | Orquestación |
| 📚 FAISS | Base vectorial |
| 📄 PyPDF | Lectura de PDF |
| 📝 python-docx | Lectura de Word |
| 🎨 Streamlit | Interfaz Web |
| 🔑 dotenv | Variables de entorno |

---

# ⚙ Instalación

## 1️⃣ Clonar el proyecto

```bash
git clone https://github.com/TU_USUARIO/Black_Ary_Knowledge_AI.git
```

---

## 2️⃣ Crear entorno virtual

```bash
python -m venv venv
```

---

## 3️⃣ Activar entorno

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 4️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Configurar la API Key

Crear un archivo **.env**

```text
GOOGLE_API_KEY=TU_API_KEY
```

---

## 6️⃣ Ejecutar la aplicación

```bash
streamlit run app.py
```

---

# 💬 Ejemplos de preguntas

- ¿Qué beneficios tiene un colaborador?
- ¿Cómo funciona la política de vacaciones?
- ¿Qué es el programa PLR?
- ¿Cuál es el presupuesto anual para capacitación?
- ¿Cómo solicitar un viaje corporativo?
- ¿Qué indica el Manual de Recursos Humanos?

---

# 📸 Capturas de Pantalla

## Pantalla Principal

*(Agregar captura aquí)*

---

## Chat Empresarial

*(Agregar captura aquí)*

---

# 🚀 Próximas Mejoras

- ✅ Mejorar precisión del RAG
- ✅ Historial persistente
- ✅ Memoria conversacional
- ✅ OCR para imágenes
- ✅ Soporte para Excel
- ✅ Soporte para PowerPoint
- ✅ Dashboard administrativo
- ✅ Carga dinámica de documentos
- ✅ Multiusuario

---

# 👨‍💻 Autor

**Nelson Cossio**

Ingeniero Constructor | Desarrollador de Soluciones con IA

**Black_Ary SpA**

---

# 💙 Nuestra Inspiración

Black_Ary SpA nace inspirado en dos compañeros muy especiales.

### 🐶 Black

Representa:

- Confianza
- Lealtad
- Cercanía
- Protección

### 👶 Ary

Representa:

- Futuro
- Aprendizaje
- Curiosidad
- Innovación

Estos valores inspiran el desarrollo de soluciones de Inteligencia Artificial orientadas a mejorar la forma en que las personas acceden al conocimiento.

---

# 🎓 Proyecto desarrollado para

- Oracle Next Education (ONE)
- Alura Latam
- Challenge IA Agents

---

<p align="center">

## 🤖 Black_Ary Knowledge AI

### *Technology Inspired by Trust and the Future.*

© 2026 Black_Ary SpA

</p>