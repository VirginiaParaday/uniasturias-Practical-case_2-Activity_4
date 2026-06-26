# JustIA - Embeddings Semánticos para Agrupación de Textos Jurídicos

Hola soy Carlos Maruicio Martinez Sarmiento, este proyecto corresponde a la **Actividad 4** del Caso Práctico de la Unidad 2 de la Especialización en Desarrollo de Software de la Corporación Universitaria de Asturias.

El objetivo es construir un prototipo que utilice **embeddings semánticos** mediante **SentenceTransformers** para agrupar fragmentos de textos jurídicos según su similitud temática, facilitando la búsqueda contextual dentro del sistema **JustIA**.

---

## Objetivo

Implementar un sistema que:

- Lea un conjunto de fragmentos jurídicos.
- Genere embeddings utilizando Sentence-BERT.
- Agrupe automáticamente los textos mediante KMeans.
- Visualice los grupos obtenidos utilizando t-SNE.

---

## Tecnologías utilizadas

- Python 3.x
- SentenceTransformers
- Scikit-learn
- Pandas
- NumPy
- Matplotlib

---

## Estructura del proyecto

```
justia-embeddings/
│
├── data/
│   └── textos_juridicos.csv
│
├── src/
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

## Flujo del proyecto

El funcionamiento del proyecto es el siguiente:

1. Leer el conjunto de textos jurídicos.
2. Generar embeddings con SentenceTransformer.
3. Agrupar los textos mediante KMeans.
4. Reducir las dimensiones con t-SNE.
5. Visualizar los grupos obtenidos.

---

## Estado del proyecto

Actualmente el proyecto se encuentra en la fase inicial de desarrollo, donde se ha definido la estructura base del repositorio y la organización de los archivos que se implementarán durante el desarrollo de la actividad.

Las siguientes etapas incluirán la generación de embeddings, el agrupamiento de textos y la visualización de los resultados.


---

## Instalación

Este proyecto fue desarrollado utilizando **Python 3.12**.

1. Clona el repositorio:

```bash
git clone <URL_DEL_REPOSITORIO>
```

2. Ingresa a la carpeta del proyecto:

```bash
cd justia-embeddings
```

3. Verifica que Python 3.12 esté instalado:

```bash
py -3.12 --version
```

4. Crea el entorno virtual utilizando Python 3.12:

```bash
py -3.12 -m venv venv
```

5. Activa el entorno virtual:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3.12 -m venv venv
source venv/bin/activate
```

6. Actualiza `pip` (recomendado):

```bash
python -m pip install --upgrade pip
```

7. Instala las dependencias del proyecto:

```bash
pip install -r requirements.txt
```

---

## Ejecución

Con el entorno virtual activado, ejecuta el proyecto desde la raíz del repositorio:

```bash
python src/main.py
```