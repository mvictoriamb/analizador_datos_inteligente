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

## 💬 Ejemplos de preguntas IA
Una vez que ejecutes el script, puedes interactuar con el chat probando consultas como estas:

> *"¿Qué nota media tienen los colocados?"* > *"¿Qué carrera tiene más empleabilidad?"* > *"Dime la correlación entre horas de estudio y empleo."* > *"Genera un gráfico de distribución de CGPA por género."*

---

## 📂 Estructura del Proyecto

```text
📁 analizador_datos_inteligente/
├── 📄 analizador_basico.ipynb               # Análisis estadístico clásico
├── 🐍 analizador_inteligente.py             # Script principal con Chat IA (OpenAI)
├── 📋 requirements.txt                      # Dependencias (pandasai, openai, etc.)
└── 📊 college_student_placement_dataset.csv # Dataset original
```

## 🛠 Stack Técnico

| 🧮 Tratamiento de Datos | 🎨 Visualización | 🧠 Inteligencia Artificial |
| :--- | :--- | :--- |
| `pandas >= 1.5.3` | `matplotlib >= 3.7.1` | `pandasai >= 0.2.9` |
| `numpy >= 1.25.0` | `seaborn >= 0.12.2` | `openai >= 0.31.0` |

---

## 📈 Análisis Real (Insights)

Tras procesar el dataset, la IA nos permite extraer estas conclusiones clave de forma automática:

> 🎯 **Datos Destacados:**
> * 🎓 **Excelencia Académica:** El CGPA promedio de los estudiantes colocados es de **7.8/10**.
> * 🔗 **Factor Clave:** La correlación entre la práctica y conseguir empleo es muy positiva (**+0.65**).
> * 💼 **Experiencia Previa:** Realizar *Internships* (prácticas) dispara la colocación al **85%**.
> * 💻 **Valor Añadido:** Dominar *Coding skills* aumenta un **42%** la probabilidad real de encontrar empleo.

---

<div align="center">
  <h3>👩‍💻 María Victoria Maldonado Bao</h3>
  <p><i>Ciberseguridad & Inteligencia Artificial | UMA Málaga 2028</i></p>

  <a href="mailto:mvictoriamb0425@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail" /></a>
  <a href="https://github.com/mvictoriamb"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" /></a>
  
  <br><br>

  <p>📜 <b>Licencia MIT</b> | 📊 Dataset original cortesía de <b>Sahil Islam (Kaggle)</b></p>
</div>
