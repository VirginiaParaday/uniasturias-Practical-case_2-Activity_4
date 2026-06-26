"""
Proyecto: JustIA - Embeddings Semánticos
Actividad 4 - Caso Práctico Unidad 2

Este script genera un conjunto de fragmentos jurídicos simulados
que serán utilizados para crear embeddings semánticos y realizar
el agrupamiento por similitud temática.

Terminal:
python src/generar_dataset.py
"""

import os
import random

import pandas as pd


# ==========================================================
# Fragmentos jurídicos por temática
# ==========================================================

laboral = [
    "El trabajador tiene derecho al pago oportuno de su salario.",
    "El empleador debe garantizar condiciones seguras de trabajo.",
    "Las vacaciones remuneradas son un derecho irrenunciable.",
    "El contrato laboral podrá terminar por justa causa.",
    "El pago de prestaciones sociales es obligatorio.",
]

civil = [
    "El contrato de compraventa debe cumplirse de buena fe.",
    "El arrendatario debe pagar el canon acordado.",
    "La propiedad privada está protegida por la ley.",
    "Los daños y perjuicios deben ser indemnizados.",
    "Las obligaciones nacen de los contratos válidamente celebrados.",
]

familia = [
    "Los padres tienen el deber de proteger a sus hijos.",
    "La custodia será determinada por el juez competente.",
    "Los alimentos garantizan el bienestar del menor.",
    "El matrimonio genera derechos y obligaciones.",
    "La adopción protege el interés superior del niño.",
]

penal = [
    "El delito de hurto será investigado por la Fiscalía.",
    "Toda persona se presume inocente hasta sentencia.",
    "La pena dependerá de la gravedad del delito.",
    "El proceso penal garantiza el derecho a la defensa.",
    "Las pruebas deberán obtenerse legalmente.",
]


# ==========================================================
# Generación del dataset
# ==========================================================

def generar_dataset():
    """
    Genera un conjunto de fragmentos jurídicos clasificados
    por temática y los almacena en un archivo CSV.

    Retorna:
        pandas.DataFrame:
            DataFrame con las columnas:
            - tema
            - texto
    """

    fragmentos = []

    # ------------------------------------------------------

    for texto in laboral:
        fragmentos.append({
            "tema": "Laboral",
            "texto": texto
        })

    for texto in civil:
        fragmentos.append({
            "tema": "Civil",
            "texto": texto
        })

    for texto in familia:
        fragmentos.append({
            "tema": "Familia",
            "texto": texto
        })

    for texto in penal:
        fragmentos.append({
            "tema": "Penal",
            "texto": texto
        })

    # ------------------------------------------------------
    # Mezclar registros
    # ------------------------------------------------------

    random.shuffle(fragmentos)

    # ------------------------------------------------------
    # Crear DataFrame
    # ------------------------------------------------------

    df = pd.DataFrame(fragmentos)

    # ------------------------------------------------------
    # Crear carpeta de salida
    # ------------------------------------------------------

    os.makedirs("data", exist_ok=True)

    # ------------------------------------------------------
    # Guardar CSV
    # ------------------------------------------------------

    ruta_archivo = "data/textos_juridicos.csv"

    df.to_csv(
        ruta_archivo,
        index=False,
        encoding="utf-8-sig"
    )

    return df


# ==========================================================
# Ejecución individual del script
# Terminal: python src/generar_dataset.py
# ==========================================================

if __name__ == "__main__":

    print("=" * 50)
    print("GENERANDO DATASET DE TEXTOS JURÍDICOS...")
    print("=" * 50)

    df = generar_dataset()

    print(f"Archivo   : data/textos_juridicos.csv")
    print(f"Registros : {len(df)}")

    print()
    print(df.head())

    print()
    print("Dataset generado correctamente.")