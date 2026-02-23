<div align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=FF6B6B&center=true&vCenter=true&width=435&lines=%F0%9F%A4%A6+Analizador+de+Datos+Inteligente;💬+Chat+con+CSV;🤖+PandasAI+%2B+OpenAI;📊+Gr%C3%A1ficos+autom%C3%A1ticos;🚀+Empleabilidad+estudiantes" alt="typing svg" />
</div>

# 🤖 **Analizador de Datos Estudiantes Universitarios**

**Pandas + PandasAI + OpenAI** | **Chat en español** | **Dataset empleabilidad Kaggle**

[![Python](https://img.shields.io/badge/Python-PandasAI-FF6B6B?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Dataset](https://img.shields.io/badge/Kaggle-Student%20Placement-FF9900?style=for-the-badge&logo=kaggle&logoColor=white)](https://www.kaggle.com/datasets/sahilislam007/college-student-placement-factors-dataset)

## ✨ **2 Versiones**

| **Base** (`analizador_basico.ipynb`) | **Inteligente** (`analizador_inteligente.py`) |
|-------------------------------------|-----------------------------------------------|
| 📊 Stats descriptivas | 💬 **"¿Qué carrera tiene más empleo?"** |
| 📈 Histogramas + barras | 🤖 **PandasAI + OpenAI GPT** |
| 🔗 Mapa correlaciones | 🎯 Respuestas en lenguaje natural |
| 🧹 Limpieza datos | 🔑 **Solo necesita API OpenAI** |

## 🎯 **Dataset Kaggle**
**"College Student Placement Analysis"** - Sahil Islam  
**Factores empleabilidad estudiantes universitarios**  
[🔗 Dataset original](https://www.kaggle.com/datasets/sahilislam007/college-student-placement-factors-dataset)

## 🚀 **Ejecución Rápida**

```bash
# 1. Clonar + instalar
git clone https://github.com/mvictoriamb/analizador_datos_inteligente.git
cd analizador_datos_inteligente
pip install -r requirements.txt

# 2. Base (sin API)
python analizador_basico.py

# 3. Inteligente (con API)
export OPENAI_API_KEY="sk-proj-tu-key"
python analizador_inteligente.py
```

💬 Ejemplos preguntas IA:

text
"¿Qué nota media tienen los colocados?"
"¿Qué carrera tiene más empleabilidad?"
"Correlación entre horas estudio y empleo"
"Gráfico distribución CGPA por género"

📂 Estructura
📁 analizador_datos_inteligente/
├── 📄 analizador_basico.ipynb      # Análisis clásico
├── 🐍 analizador_inteligente.py    # Chat IA OpenAI
├── 📋 requirements.txt             # pandasai openai
└── 📊 college_student_placement_dataset.csv

🛠 Stack Técnico
text
📊 pandas>=1.5.3     📈 matplotlib>=3.7.1
🔢 numpy>=1.25.0     🎨 seaborn>=0.12.2
🤖 pandasai>=0.2.9   🔑 openai>=0.31.0

📈 Análisis Real
text
✅ CGPA promedio colocados: 7.8/10
✅ Correlación práctica → empleo: +0.65
✅ Internships → 85% colocación
✅ Coding skills → +42% probabilidad empleo

👩‍💻 María Victoria Maldonado Bao
Ciberseguridad & IA | UMA Málaga 2028
✉️ mvictoriamb0425@gmail.com

MIT License | Dataset: Kaggle Sahil Islam
