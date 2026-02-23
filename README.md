<div align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=FF6B6B&center=true&vCenter=true&width=435&lines=%F0%9F%A4%A6+Analizador+de+Datos+Inteligente;💬+Chat+con+CSV;🤖+PandasAI+%2B+Gemini;📊+Gr%C3%A1ficos+autom%C3%A1ticos;🚀+No+code+necesario" alt="typing svg" />
</div>

# 🤖 **Analizador de Datos sobre Estudiantes Universitarios**

**Streamlit + PandasAI + Gemini** | **Chat en lenguaje natural** | **Dataset empleabilidad estudiantes**

[![Streamlit](https://img.shields.io/badge/Streamlit-PandasAI-Gemini-FF6B6B?style=for-the-badge&logo=python&logoColor=white)](https://streamlit.io)
[![Dataset Kaggle](https://img.shields.io/badge/Kaggle-Student%20Placement-orange?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/sahilislam007/college-student-placement-factors-dataset)

## ✨ **Features**

| **Versión Base** | **Versión Inteligente** |
|------------------|-------------------------|
| 📊 Estadísticas descriptivas | 💬 **Preguntas en español** |
| 📈 Histogramas + barras | 🤖 **PandasAI + Gemini** |
| 🔗 Correlaciones automáticas | 🎨 Gráficos Plotly interactivos |
| 🗃️ Dataset estudiantes | 🚫 **Sin SQL/Pandas necesario** |

## 🎯 **Dataset**
**"College Student Placement Analysis"** (Kaggle)  
**Análisis factores empleabilidad estudiantes universitarios**  
[Ver dataset →](https://www.kaggle.com/datasets/sahilislam007/college-student-placement-factors-dataset)

## 🚀 **Instalación Rápida**

```bash
git clone https://github.com/mvictoriamb/analizador_datos_inteligente.git
cd analizador_datos_inteligente
pip install -r requirements.txt
streamlit run analizador_inteligente.py

🔑 Versión IA (Opcional)
bash
# 1. API Key Gemini/OpenAI
export GOOGLE_API_KEY="tu_api_key"

# 2. Ejecutar
streamlit run analizador_inteligente.py
💬 Ejemplo: "¿Qué carrera tiene mayor tasa de empleo?"

📂 Estructura
text
📁 analizador_datos_inteligente/
├── 📁 data/                 # Dataset CSV
├── 🔹 analizador_basico.py  # Sin IA
├── 🤖 analizador_inteligente.py # Con PandasAI
├── 📋 requirements.txt
└── 📄 README.md
🛠 Tech Stack
text
graph LR
    CSV[📊 CSV Dataset] --> Pandas[Pandas]
    Pandas --> Streamlit[Streamlit UI]
    Streamlit --> Gemini[🔮 Gemini AI]
    Gemini --> Plotly[📈 Plotly]
📈 Resultados
text
✅ Correlaciones carrera → empleo
✅ Tasa colocación por nota media  
✅ Gráficos interactivos automáticos
✅ Chat IA: "Mejores carreras 2026"
👩‍💻 María Victoria Maldonado Bao
Ciberseguridad & IA | UMA 2028
✉️ mvictoriamb0425@gmail.com
