"""
Proyecto: JustIA - Embeddings Semánticos
Actividad 4 - Caso Práctico Unidad 2

Este script carga el conjunto de textos jurídicos generado
previamente y utiliza el modelo Sentence-BERT para convertir
cada fragmento en un embedding semántico. Estos embeddings
serán utilizados posteriormente para crear agrupamientos
temáticos mediante algoritmos de clustering.

Terminal: python src/generar_embeddings.py
"""

import pandas as pd
from sentence_transformers import SentenceTransformer


# ==========================================================
# Generación de embeddings semánticos
# ==========================================================

def generar_embeddings():
    """
    Lee el dataset de textos jurídicos y genera un embedding
    para cada fragmento utilizando el modelo
    paraphrase-multilingual-MiniLM-L12-v2.

    Retorna:
        pandas.DataFrame:
            DataFrame con las columnas:
            - tema
            - texto
            - embedding
    """

    # ==========================================================
    # Leer el dataset
    # ==========================================================

    df = pd.read_csv("data/textos_juridicos.csv")

    # ==========================================================
    # Cargar el modelo Sentence-BERT
    # ==========================================================

    modelo = SentenceTransformer(
        "paraphrase-multilingual-MiniLM-L12-v2"
    )

    # ==========================================================
    # Generar embeddings
    # ==========================================================

    embeddings = modelo.encode(
        df["texto"].tolist(),
        show_progress_bar=True
    )

    # ==========================================================
    # Agregar embeddings al DataFrame
    # ==========================================================

    df["embedding"] = list(embeddings)

    # ==========================================================
    # Retornar resultado
    # ==========================================================

    return df



# ==========================================================
# Ejecución individual del script
# Terminal: python src/generar_embeddings.py
# ==========================================================


if __name__ == "__main__":

    print("=" * 50)
    print("GENERANDO EMBEDDINGS SEMÁNTICOS...")
    print("=" * 50)

    df = generar_embeddings()

    print(f"Total de registros: {len(df)}")
    print()

    print(df[["tema", "texto"]].head())

    print()
    print("Embeddings generados correctamente.")