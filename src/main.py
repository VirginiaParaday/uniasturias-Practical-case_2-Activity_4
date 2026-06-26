"""
Proyecto: JustIA - Embeddings Semánticos
Actividad 4 - Caso Práctico Unidad 2

Este script coordina la ejecución completa del proyecto,
desde la generación del dataset hasta la visualización
de los clusters temáticos.

Terminal: python src/main.py
"""

from generar_dataset import generar_dataset
from generar_embeddings import generar_embeddings
from clustering import crear_clusters
from visualizar_clusters import visualizar_clusters


# ==========================================================
# Ejecución principal del proyecto
# ==========================================================

def main():
    """
    Ejecuta el flujo completo del proyecto.
    """

    print("=" * 60)
    print("JUSTIA - EMBEDDINGS SEMÁNTICOS")
    print("=" * 60)

    # ------------------------------------------------------
    # Paso 1
    # ------------------------------------------------------

    print("\n[1/4] Generando dataset...")

    df_dataset = generar_dataset()

    print(f"Registros generados: {len(df_dataset)}")

    # ------------------------------------------------------
    # Paso 2
    # ------------------------------------------------------

    print("\n[2/4] Generando embeddings...")

    df_embeddings = generar_embeddings()

    print("Embeddings generados correctamente.")

    # ------------------------------------------------------
    # Paso 3
    # ------------------------------------------------------

    print("\n[3/4] Creando clusters...")

    df_clusters = crear_clusters()

    print(f"Clusters generados: {df_clusters['cluster'].nunique()}")

    # ------------------------------------------------------
    # Paso 4
    # ------------------------------------------------------

    print("\n[4/4] Generando visualización...")

    visualizar_clusters()

    print("Imagen guardada en:")
    print("output/clusters_tsne.png")

    print("\n" + "=" * 60)
    print("PROCESO FINALIZADO CORRECTAMENTE")
    print("=" * 60)


# ==========================================================
# Ejecución del programa
# Terminal: python src/main.py
# ==========================================================

if __name__ == "__main__":
    main()