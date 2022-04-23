## Packaging
Python is dynamically typed and non-compiled language. Python requires that the
environment you run in has an appropriate Python interpreter and the ability to install the
libraries and packages you need.

## Add setup.cfg
```commandline
[metadata]
name = fastapi_advertising_prediction
version = 0.0.1
author = Erkan SIRIN
author_email = erkansirin.datalonga@gmail.com
description = ML model deployment of Advertising dataset.
long_description = file: README.md
long_description_content_type = text/markdown
url = ""
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
packages = find:
python_requires = >=3.7
include_package_data = True
```

## Add pyproject.toml 
```commandline
[build-system]
requires = [
    "setuptools>=54",
    "wheel"
]
build-backend = "setuptools.build_meta"
```
## Add a license
- Visit https://choosealicense.com/ and pick-up that suits your need.

## Build
```commandline
pip install build

python -m build
```
- Build will create new files
```commandline
.
├── dist
│   ├── fastapi_advertising_prediction-0.0.1-py3-none-any.whl
│   └── fastapi_advertising_prediction-0.0.1.tar.gz
├── fastapi_advertising_prediction
│   ├── Dockerfile
│   ├── __init__.py
│   ├── main.py
│   ├── __pycache__
│   │   ├── __init__.cpython-38.pyc
│   │   ├── main.cpython-38.pyc
│   │   ├── schemas.cpython-38.pyc
│   │   └── train.cpython-38.pyc
│   ├── requirements.txt
│   ├── saved_models
│   │   └── 03.randomforest_with_advertising.pkl
│   ├── schemas.py
│   └── train.py
├── fastapi_advertising_prediction.egg-info
│   ├── dependency_links.txt
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   └── top_level.txt
├── LICENSE
├── pyproject.toml
├── README.md
└── setup.cfg

5 directories, 21 files
```

- Check dist folder
```commandline
 tree dist/
dist/
├── fastapi_advertising_prediction-0.0.1-py3-none-any.whl
└── fastapi_advertising_prediction-0.0.1.tar.gz
```

## Create an account on test.pypi.org
- Before pypi one we upload test.pypi to see everything is good.

## Install twine
` pip install twine `  

## Upload package with twine
```commandline
python -m twine upload --repository testpypi dist/*
```
