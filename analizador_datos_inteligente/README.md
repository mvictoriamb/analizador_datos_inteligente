# Analizador de Datos sobre Estudiantes Universitarios

Este proyecto analiza un dataset sobre estudiantes universitarios, generando estadísticas, gráficos y correlaciones automáticamente. Además, cuenta con una versión avanzada que integra **PandasAI**, permitiendo hacer preguntas en lenguaje natural sobre los datos. El análisis se basa en el dataset “College Student Placement Analysis” de Kaggle, creado por Sahil Islam:
https://www.kaggle.com/datasets/sahilislam007/college-student-placement-factors-dataset
Este proyecto está liberado bajo la **MIT License**.


## 📂 Estructura del proyecto

Analizador_Datos/
├─ data/ # Carpeta para colocar el dataset
├─ analizador_basico.py # Versión clásica de análisis de datos
├─ analizador_inteligente.py # Versión con PandasAI
├─ README.md
├─ requirements.txt


## 🔹 Versiones

1. **Versión base (Kaggle)**  
   - Analiza el dataset con Python, pandas, matplotlib y seaborn.  
   - Genera estadísticas descriptivas, histogramas, gráficos de barras y mapas de correlación.  

2. **Versión inteligente**  
   - Integra `pandasai` y `SmartDataframe` para poder hacer preguntas en lenguaje natural sobre los datos.  
   - No requiere conocimientos de SQL o pandas para interactuar con el dataset.  
   - Requiere una API Key de OpenAI.

## ⚙️ Requisitos

- Python 3.10+  
- Bibliotecas Python: pandas, matplotlib, seaborn, numpy  
- (Opcional para la versión inteligente) pandasai y OpenAI API Key


## 🚀 Cómo usar

# 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/mvictoriamb/analizador_datos_inteligente.git
cd analizador_datos_inteligente

# 2️⃣ Crear y activar un entorno virtual (opcional pero recomendado)
python -m venv .venv
.venv\Scripts\activate    # Windows
# source .venv/bin/activate # Linux / Mac

# 3️⃣ Actualizar pip e instalar dependencias
pip install --upgrade pip
pip install -r requirements.txt
