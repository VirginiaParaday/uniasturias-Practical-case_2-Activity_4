"""
Proyecto: JustIA - Embeddings Semánticos
Actividad 4 - Caso Práctico Unidad 2

Este script visualiza los clusters generados mediante KMeans,
reduciendo los embeddings a dos dimensiones utilizando t-SNE.

Terminal:
python src/visualizar_clusters.py
"""

import os

import matplotlib.pyplot as plt
import numpy as np
from sklearn.manifold import TSNE

from clustering import crear_clusters


# ==========================================================
# Visualización de clusters
# ==========================================================

def visualizar_clusters():
    """
    Reduce los embeddings a dos dimensiones utilizando
    t-SNE y genera una gráfica de dispersión de los
    clusters temáticos.

    Retorna:
        pandas.DataFrame:
            DataFrame con las columnas:
            - tema
            - texto
            - embedding
            - cluster
            - x
            - y
    """

    # ==========================================================
    # Obtener el DataFrame con los clusters
    # ==========================================================

    df = crear_clusters()

    # ==========================================================
    # Convertir embeddings a matriz NumPy
    # ==========================================================

    embeddings = np.vstack(df["embedding"].values)

    # ==========================================================
    # Reducir dimensiones con t-SNE
    # ==========================================================

    tsne = TSNE(
        n_components=2,
        perplexity=5,
        random_state=42
    )

    coordenadas = tsne.fit_transform(embeddings)

    df["x"] = coordenadas[:, 0]
    df["y"] = coordenadas[:, 1]

    # ==========================================================
    # Crear carpeta de salida
    # ==========================================================

    os.makedirs("output", exist_ok=True)

    # ==========================================================
    # Crear gráfica
    # ==========================================================

    plt.figure(figsize=(10, 7))

    scatter = plt.scatter(
        df["x"],
        df["y"],
        c=df["cluster"],
        s=80,
        alpha=0.8
    )

    plt.title("Clusters temáticos de textos jurídicos", fontsize=14)
    plt.xlabel("Componente 1")
    plt.ylabel("Componente 2")

    plt.grid(True, linestyle="--", alpha=0.4)

    plt.legend(
        *scatter.legend_elements(),
        title="Cluster"
    )

    plt.tight_layout()

    # ==========================================================
    # Guardar imagen
    # ==========================================================

    ruta_imagen = "output/clusters_tsne.png"

    plt.savefig(
        ruta_imagen,
        dpi=300,
        bbox_inches="tight"
    )

    # Cerrar la figura (no abrir ventana)
    plt.close()

    return df


# ==========================================================
# Ejecución individual del script
# Terminal: python src/visualizar_clusters.py
# ==========================================================

if __name__ == "__main__":

    print("=" * 50)
    print("VISUALIZANDO CLUSTERS TEMÁTICOS...")
    print("=" * 50)

    df = visualizar_clusters()

    print(f"Total de registros : {len(df)}")
    print("Imagen generada     : output/clusters_tsne.png")

    print()
    print("Visualización creada correctamente.")