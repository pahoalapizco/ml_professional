# Machine Learning Professional

**Version**: 1.0
**Author**: @pahoalapizco

Notes and exercises from Platzi's course [Machine Learning Professional with scikit-learn](https://platzi.com/cursos/scikitlearn/)


Para el curso profesional de machine learning, se proporcionaron tres datasets diferentes. Con cada uno de éstos Datasets, se pretende estudiar un modelo de machine learning especifico. 

- **[World Happiness](https://www.kaggle.com/datasets/unsdsn/world-happiness)**: Contiene información desde 2012 hasta 2019, sobre diferentes aspectos de todos los países para evaluar su calidad de vida y percepción de felicidad de sus habitantes. 
- **[Heart Disease](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)**: Contiene un subconjunto de 14 atributos de los datos tomados en 1988 en cuatro bases de datos médicas diferentes (Cleveland, Hungría, Suiza y Long Beach). Pretende relacionar diferentes variables medidas sobre el estado de saludos en varios pacientes con la presencia o ausencia de una patología cardiaca, para identificar los factores preponderantes en la aparición de estas.
- **[The Ultimate Halloween Candy Power Ranking](https://www.kaggle.com/datasets/fivethirtyeight/the-ultimate-halloween-candy-power-ranking)**: Contiene información de la composición de 86 diferentes golosinas y de la preferencia de varias personas que fueron encuestadas para describir cuál es la favorita de los consumidores.



<div class="alert alert-warning", role="alert">
    <p>
      📌 Los datasets de kaggle no son iguales a los datasets que nos proporcionaron en el curso, el profesor dijo, que éstos fueron curados para propósitos didácticos.
    </p>
</div>


## Prerequisites
- Anaconda >=4.x 

## Create environment
```bash
conda env create -f environment.yml
activate ml_professional
```

## Set up project's module
To move beyond notebook prototyping, all reusable code should go into the modules/ folder package. To use that package inside your project, install the project's module in editable mode, so you can edit files in the final folder and use the modules inside your notebooks :

```bash
pip install --editable .
```

To use the module inside your notebooks, add `%autoreload` at the top of your notebook :

```python
%load_ext autoreload
%autoreload 2
```

Example of module usage:
1. Paths usage:
```python
import sys
sys.path.append("..")

import modules.utils.paths as path
path.data_dir()
```

2. Download data usage:
```python
import modules.utils.download_data
download_data.from_kaggle(("uciml/iris", "Iris.csv"))

```

## Project organization

    ml_professional
        ├── data
        │   ├── processed      <- The final, canonical data sets for modeling.
        │   └── raw            <- The original, immutable data dump.
        │
        ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
        │                         the creator's initials, and a short `-` delimited description, e.g.
        │                         `1.0-initial-data-exploration`.
        │
        ├── .gitignore         <- Files to ignore by `git`.
        │
        ├── environment.yml    <- The requirements file for reproducing the analysis environment.
        │
        ├── README.md          <- The top-level README for developers using this project.
        │
        ├── setup.py           <- Makes project pip installable (pip install -e .)
        │                          so final can be imported.
        ├── .here              <- File that will stop the search if none of the other criteria
        │                         apply when searching head of project.
        │
        └── modules              <- Source code for use in this project.
            └── utils          <- Scripts to help with common tasks.
                └── paths.py   <- Helper functions to relative file referencing across project.

---