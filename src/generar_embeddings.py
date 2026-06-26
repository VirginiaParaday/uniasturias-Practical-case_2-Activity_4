"""
Proyecto: JustIA - Embeddings Semánticos
Actividad 4 - Caso Práctico Unidad 2

Este script carga el conjunto de textos jurídicos generado
previamente y utiliza el modelo Sentence-BERT para convertir
cada fragmento en un embedding semántico. Estos embeddings
serán utilizados posteriormente para crear agrupamientos
temáticos mediante algoritmos de clustering.

Terminal:
python src/generar_embeddings.py
"""

import pandas as pd
from sentence_transformers import SentenceTransformer


# ==========================================================
# Generación de embeddings semánticos
# ==========================================================

def generar_embeddings():
    """
    Lee el conjunto de textos jurídicos y genera un embedding
    semántico para cada fragmento utilizando el modelo
    paraphrase-multilingual-MiniLM-L12-v2.

    Retorna:
        pandas.DataFrame:
            DataFrame con las columnas:
            - tema
            - texto
            - embedding
    """

    # ==========================================================
    # Leer el conjunto de datos
    # ==========================================================

    df = pd.read_csv("data/textos_juridicos.csv")

    # ==========================================================
    # Cargar el modelo Sentence-BERT
    # ==========================================================
    # Este modelo multilingüe transforma cada texto en un
    # vector numérico (embedding) que representa su significado
    # semántico.
    # ==========================================================

    modelo = SentenceTransformer(
        "paraphrase-multilingual-MiniLM-L12-v2"
    )

    # ==========================================================
    # Generar los embeddings
    # ==========================================================
    # Se procesa cada fragmento jurídico del dataset y se
    # obtiene un embedding para cada uno de ellos.
    # ==========================================================

    embeddings = modelo.encode(
        df["texto"].tolist(),
        show_progress_bar=True
    )

    # ==========================================================
    # Agregar los embeddings al DataFrame
    # ==========================================================

    df["embedding"] = list(embeddings)

    # ==========================================================
    # Retornar el resultado
    # ==========================================================

    return df


# ==========================================================
# Ejecución individual del script
# Terminal: python src/generar_embeddings.py
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("GENERANDO EMBEDDINGS SEMÁNTICOS")
    print("=" * 60)

    # Obtener el DataFrame con los embeddings generados
    df = generar_embeddings()

    print(f"Total de registros procesados : {len(df)}")

    print("\nPrimeros registros del conjunto de datos:\n")
    print(df[["tema", "texto"]].head())

    print("\nEmbeddings generados correctamente.")