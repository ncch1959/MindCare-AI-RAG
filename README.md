<p align="center">

# 🤖 Black_Ary Knowledge AI

### Enterprise Intelligent Assistant powered by Artificial Intelligence

*Technology Inspired by Trust and the Future.*

</p>

---

# 📖 Descripción

**Black_Ary Knowledge AI** es un asistente inteligente sobre salud mental desarrollado para responder consultas sobre documentos emitidos por autoridades sanitarias nacional como internacionañes de **Retrieval-Augmented Generation (RAG)**.

El sistema combina búsqueda semántica con Inteligencia Artificial Generativa para entregar respuestas precisas, rápidas y fundamentadas en la documentación fuente.

---

# ✨ Características

- 🤖 Chat inteligente de medecina mental
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
   Documentos de Salud Mental
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
│     ├── logo_blackary Spa.png
│     
│     
│  
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

1 ¿Qué factores sociales y económicos influyen más en el aumento de los trastornos de ansiedad y depresión en la actualidad?

2 ¿Cómo impacta el envejecimiento poblacional en la prevalencia de enfermedades neurodegenerativas como el Alzheimer y el Parkinson?

3 ¿Qué papel juega la digitalización (apps, redes sociales, telemedicina) en el cuidado de la salud mental y cuáles son sus riesgos?

4 ¿Por qué existe una brecha tan grande entre la necesidad de atención en salud mental y la cobertura real de los sistemas de salud?

5 ¿Qué estrategias comunitarias podrían ayudar a reducir el estigma asociado a los trastornos mentales?

6 ¿Cómo se relacionan las crisis globales (cambio climático, migración, conflictos) con el incremento de problemas de salud mental en poblaciones vulnerables?

---

# 📸 Capturas de Pantalla

## Pantalla Principal

*(Agregar captura aquí)*

---

## Chat salud mental

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

**Nelson Cossio Chiang**

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

"Estos valores inspiran el desarrollo de la implementación de aplicaciones para adultos mayores, con poca y/o nada d accecibilidad de recursos económicos y redes de apoyo, y a personas cuidadoras que dsconocen o poco saben sobre enfermedades degenerativas mentales.

La Inteligencia Artificial orientadas a mejorar la forma en que las personas de la tercera edad acceden al conocimiento, de manera rápida, discreta, promoviendo su autonomía y bienestar."

Enfocado en inclusión: “…de manera rápida, discreta y equitativa, garantizando que nadie quede fuera del mundo digital.”

Enfocado en autonomía: “…de manera rápida, discreta y sencilla, fortaleciendo su independencia en el aprendizaje.”

Enfocado en calidad de vida: “…de manera rápida, discreta y significativa, contribuyendo a una mejor calidad de vida.”
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