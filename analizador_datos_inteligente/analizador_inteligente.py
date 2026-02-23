#-------------0. CONFIGURACIÓN-------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

pd.set_option("display.max_columns", None)
sns.set(style="whitegrid")

#-------------1. CARGAR DATASET-------------

df=pd.read_csv("college_student_placement_dataset.csv")

print("\nPrimeras filas del dataset")
print(df.head())

print("\nInformación general:")
print(df.info())

print("\nResumen de los datos:")
print(df.describe())

print("\nTamaño del dataset (filas, columnas):", df.shape)

print("\nNombres de columnas:")
print(df.columns)

print("\nValores nulos por columna:")
print(df.isnull().sum())

#-------------2. LIMPIEZA-------------
#Limpiamos valores infinitos y nulos
df.replace([np.inf, -np.inf], np.nan, inplace=True) 
df = df.dropna()

#-------------3. ANÁLISIS POR CATEGORÍAS-------------

print("\nPromedios de cada columna numérica:")
columnas_numericas = df.select_dtypes(include=["int64","float64"]).columns
for columna in columnas_numericas:
    print(f"\n{columna}: {df[columna].mean():.2f}")

print("\nConteo de valores únicos en las columnas no numéricas:")
columnas_no_numericas = df.select_dtypes(exclude=["int64","float64"]).columns
for columna in columnas_no_numericas:
    print(f"\n{columna}: {df[columna].nunique()}")
    
print("\nValor más común en columnas no numéricas (si aparece más de una vez):")
for columna in columnas_no_numericas:
    conteo = df[columna].value_counts()
    if conteo.iloc[0] > 1: 
        porcentaje = conteo.iloc[0] / len(df[columna]) * 100
        print(f"{columna}: {conteo.index[0]} ({porcentaje:.2f}% del total)")

              
#-------------5. REPRESENTACIÓN-------------

print("\nHistogramas para las columnas numéricas:")
for columna in columnas_numericas:
    plt.figure(figsize=(8,4))
    sns.histplot(df[columna], bins=10, kde=True, color='violet')
    plt.title(f"Distribución de {columna}")
    plt.xlabel(columna)
    plt.ylabel("Número de estudiantes")
    #plt.show()

print("\nGráfico de barras:")
for columna in columnas_no_numericas:
    conteo = df[columna].value_counts()
    if conteo.iloc[0] > 1:
        plt.figure(figsize=(8,4))
        sns.countplot(x=columna, data=df, hue=columna, palette='pastel', order=conteo.index, legend=False)
        plt.title(f"{columna}")
        plt.ylabel("Número de estudiantes")
        #plt.show()

#-------------6. CORRELACIÓN-------------
num_df = df[columnas_numericas]

if not num_df.empty:
    plt.figure(figsize=(8,4))
    corr = num_df.corr()
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Mapa de correlación")
    #plt.show()


#-------------7. CONECTAR CON INTELIGENCIA ARTIFICIAL----------

import pandasai
from pandasai import SmartDataframe
from pandasai.llm import OpenAI

llm = OpenAI(api_token="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") #necesito una api key de openai
sdf = SmartDataframe(df, config={"llm": llm})

while True:
    pregunta = input("\nEscribe tu pregunta (o 'exit' para terminar):")
    if pregunta.lower() == "exit":
        print("Has salido del analizador de datos inteligente.")
        break
    try:
        respuesta = sdf.chat(pregunta)
        print("Respuesta: {respuesta}")
    except Exception as error:

        print("Error al procesar la pregunta:", error)
