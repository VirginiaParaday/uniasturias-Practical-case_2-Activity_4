# JustIA - Embeddings Semánticos para Agrupación de Textos Jurídicos

Hola, soy **Carlos Mauricio Martínez Sarmiento**. Este proyecto corresponde a la **Actividad 4** del Caso Práctico de la Unidad 2 de la Especialización en Desarrollo de Software de la Corporación Universitaria de Asturias.

El objetivo es construir un prototipo que utilice **embeddings semánticos** mediante **SentenceTransformers** para agrupar fragmentos de textos jurídicos según su similitud temática, facilitando la búsqueda contextual dentro del sistema **JustIA**.

---

# Objetivo

Implementar un sistema que permita:

* Generar un conjunto de fragmentos jurídicos clasificados por temática.
* Crear embeddings semánticos utilizando Sentence-BERT.
* Agrupar automáticamente los textos mediante el algoritmo KMeans.
* Reducir la dimensionalidad de los embeddings utilizando t-SNE.
* Visualizar gráficamente los clusters generados.

---

# Tecnologías utilizadas

* Python 3.12
* SentenceTransformers
* Scikit-learn
* Pandas
* NumPy
* Matplotlib

---

# Estructura del proyecto

```text
justia-embeddings/
│
├── data/
│   └── textos_juridicos.csv
│
├── output/
│   └── clusters_tsne.png
│
├── src/
│   ├── generar_dataset.py
│   ├── generar_embeddings.py
│   ├── clustering.py
│   ├── visualizar_clusters.py
│   └── main.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

# Flujo del proyecto

El funcionamiento del proyecto es el siguiente:

1. Generar un conjunto de fragmentos jurídicos.
2. Crear embeddings semánticos utilizando Sentence-BERT.
3. Aplicar el algoritmo KMeans para formar clusters temáticos.
4. Reducir los embeddings a dos dimensiones mediante t-SNE.
5. Generar una visualización gráfica de los clusters.

---

# Funcionalidades implementadas

### `generar_dataset.py`

Genera automáticamente un conjunto de fragmentos jurídicos clasificados por temática y crea el archivo:

```text
data/textos_juridicos.csv
```

---

### `generar_embeddings.py`

Lee el dataset y utiliza el modelo **paraphrase-multilingual-MiniLM-L12-v2** para generar un embedding semántico para cada fragmento jurídico.

---

### `clustering.py`

Obtiene los embeddings generados y aplica el algoritmo **KMeans** para agrupar automáticamente los textos según su similitud semántica.

Cada registro recibe un identificador de cluster.

---

### `visualizar_clusters.py`

Reduce los embeddings a dos dimensiones utilizando **t-SNE** y genera una gráfica de dispersión que representa visualmente los clusters encontrados.

La imagen se almacena automáticamente en:

```text
output/clusters_tsne.png
```

---

### `main.py`

Coordina la ejecución completa del proyecto.

Al ejecutarlo realiza automáticamente los siguientes pasos:

1. Generar el dataset.
2. Crear los embeddings.
3. Generar los clusters.
4. Crear la visualización.

---

# Instalación

Este proyecto fue desarrollado utilizando **Python 3.12**.

## 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
```

## 2. Ingresar al proyecto

```bash
cd justia-embeddings
```

## 3. Verificar la versión de Python

```bash
py -3.12 --version
```

## 4. Crear el entorno virtual

```bash
py -3.12 -m venv venv
```

## 5. Activar el entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3.12 -m venv venv
source venv/bin/activate
```

## 6. Actualizar pip

```bash
python -m pip install --upgrade pip
```

## 7. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución

Para ejecutar todo el proyecto:

```bash
python src/main.py
```

---

También es posible ejecutar cada módulo de forma independiente.

### Generar el dataset

```bash
python src/generar_dataset.py
```

### Generar embeddings

```bash
python src/generar_embeddings.py
```

### Crear clusters

```bash
python src/clustering.py
```

### Generar la visualización

```bash
python src/visualizar_clusters.py
```

---

# Archivos generados

Durante la ejecución del proyecto se crean automáticamente los siguientes archivos:

| Archivo                     | Descripción                                                     |
| --------------------------- | --------------------------------------------------------------- |
| `data/textos_juridicos.csv` | Dataset con los fragmentos jurídicos clasificados por temática. |
| `output/clusters_tsne.png`  | Visualización gráfica de los clusters generados mediante t-SNE. |

---

# Estado del proyecto

Actualmente el proyecto implementa el flujo completo solicitado en la actividad:

* Generación del dataset.
* Obtención de embeddings semánticos.
* Agrupamiento mediante KMeans.
* Visualización utilizando t-SNE.

El siguiente paso será ampliar el conjunto de datos hasta alcanzar los **100 fragmentos jurídicos** requeridos por el enunciado y realizar el análisis de los agrupamientos obtenidos para el informe técnico.
