"""
Proyecto: JustIA - Embeddings Semánticos
Actividad 4 - Caso Práctico Unidad 2

Este script utiliza los embeddings generados mediante
Sentence-BERT para agrupar automáticamente los textos
jurídicos utilizando el algoritmo KMeans.

Terminal:
python src/clustering.py
"""

import numpy as np
from sklearn.cluster import KMeans

from generar_embeddings import generar_embeddings


# ==========================================================
# Creación de clusters temáticos
# ==========================================================

def crear_clusters():
    """
    Aplica el algoritmo KMeans sobre los embeddings
    generados previamente.

    Retorna:
        pandas.DataFrame:
            DataFrame con las columnas:
            - tema
            - texto
            - embedding
            - cluster
    """

    # ==========================================================
    # Obtener embeddings
    # ==========================================================

    df = generar_embeddings()

    # ==========================================================
    # Convertir embeddings a matriz NumPy
    # ==========================================================

    embeddings = np.vstack(df["embedding"].values)

    # ==========================================================
    # Crear modelo KMeans
    # ==========================================================

    kmeans = KMeans(
        n_clusters=4,
        random_state=42,
        n_init=10
    )

    # ==========================================================
    # Generar clusters
    # ==========================================================

    df["cluster"] = kmeans.fit_predict(embeddings)

    return df


# ==========================================================
# Ejecución individual del script
# Terminal: python src/clustering.py
# ==========================================================

if __name__ == "__main__":

    print("=" * 50)
    print("CREANDO CLUSTERS TEMÁTICOS...")
    print("=" * 50)

    df = crear_clusters()

    print(f"Total de registros: {len(df)}")

    print()
    print(df[["tema", "cluster"]].head(10))

    print()
    print("Clusters generados correctamente.")