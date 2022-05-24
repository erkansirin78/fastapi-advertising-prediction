## 1. Packaging
Python is dynamically typed and non-compiled language. Python requires that the
environment you run in has an appropriate Python interpreter and the ability to install the
libraries and packages you need.
- Example: https://packaging.python.org/en/latest/tutorials/packaging-projects/

## 2. Create a GitHub repo
https://github.com/erkansirin78/fastapi-advertising-prediction.git

## 3. Activate conda environment
```commandline
conda activate fastapi
```

## 4. Install packaging related packages
```commandline
pip install -r requirements
```
## 5. Add setup.cfg
```commandline
[metadata]
name = fastapi_advertising_prediction
version = 0.0.1
author = Erkan SIRIN
author_email = erkansirin.datalonga@gmail.com
description = ML model deployment of Advertising dataset.
long_description = file: README.md
long_description_content_type = text/markdown
url = https://github.com/erkansirin78/fastapi-advertising-prediction
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
packages = find:
python_requires = >=3.7
include_package_data = True
```
- If you update, change version.

## 6. Add pyproject.toml 
```commandline
[build-system]
requires = [
    "setuptools>=54",
    "wheel"
]
build-backend = "setuptools.build_meta"
```
- Wheels are a component of the Python ecosystem that helps to make package installs just work. They allow for faster installations and more stability in the package distribution process.
- https://realpython.com/python-wheels/#what-is-a-python-wheel

## 7. Add a license
- Create LICENCE file
- Visit https://choosealicense.com/ and pick-up that suits your need.

## 8. Build
```commandline
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

## 9. Create an account on test.pypi.org
- Before sending packages to pypi, first we upload test.pypi to see everything is all right.

## 10. Upload package with twine
```commandline
twine upload --repository testpypi --skip-existing dist/* --verbose
```
- Expected output
```commandline
Uploading distributions to https://test.pypi.org/legacy/
INFO     dist/fastapi_advertising_prediction-0.0.1-py3-none-any.whl (4.6 KB)
INFO     dist/fastapi_advertising_prediction-0.0.1.tar.gz (3.3 KB)
INFO     Querying keyring for username
Enter your username: erkansirin
INFO     Querying keyring for password
WARNING  No recommended backend was available. Install a recommended 3rd party backend
         package; or, install the keyrings.alt package if you want to use the
         non-recommended backends. See https://pypi.org/project/keyring for details.
Enter your password:
INFO     username: erkansirin
INFO     password: <hidden>
Uploading fastapi_advertising_prediction-0.0.1-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 8.9/8.9 kB • 00:00 • 1.6 MB/s
INFO     Response from https://test.pypi.org/legacy/:
         200 OK
Uploading fastapi_advertising_prediction-0.0.1.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.6/7.6 kB • 00:00 • ?
INFO     Response from https://test.pypi.org/legacy/:
         200 OK

View at:
https://test.pypi.org/project/fastapi-advertising-prediction/0.0.1/
```

- Visit page: https://test.pypi.org/project/fastapi-advertising-prediction/0.0.1/

## 11. Install from test.pypi.org
```commandline
pip install -i https://test.pypi.org/simple/ fastapi-advertising-prediction==0.0.1
```
- Ignore following error and try again.
```commandline
ERROR: No matching distribution found for fastapi-advertising-prediction==0.0.1
```
## 12. Test package
- Create test directory
```commandline
mkdir /tmp/fasttest
cd /tmp/fasttest
```
- Create a module for training and saving model.
```commandline
cat <<EOF > train_run.py
from fastapi_advertising_prediction import train

if __name__=='__main__':
    train.read_and_train()
EOF
```
- Run: ` python train_run.py`  

- Expected output
```commandline
   ID     TV  Radio  Newspaper  Sales
0   1  230.1   37.8       69.2   22.1
1   2   44.5   39.3       45.1   10.4
2   3   17.2   45.9       69.3    9.3
3   4  151.5   41.3       58.5   18.5
4   5  180.8   10.8       58.4   12.9
(200, 3)
[[230.1  37.8  69.2]
 [ 44.5  39.3  45.1]
 [ 17.2  45.9  69.3]]
(200,)
0    22.1
1    10.4
2     9.3
3    18.5
4    12.9
5     7.2
Name: Sales, dtype: float64
R2: 0.9825966330409427
current_dir: /home/train/miniconda3/envs/fastapi/lib/python3.8/site-packages/fastapi_advertising_prediction
FileExistsError: File exists.
/home/train/miniconda3/envs/fastapi/lib/python3.8/site-packages/fastapi_advertising_prediction/saved_models
X_manual_test [[230.1, 37.8, 69.2]]
prediction [21.986]
```

## 13. Run uvicorn
-  create a module 
```commandline
cat<<EOF > main.py
from fastapi_advertising_prediction import main
import uvicorn

app = main.app

if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True,
                log_level="debug", debug=True,
                workers=4, limit_concurrency=10, limit_max_requests=10)
EOF
```
- Run:  ` python main.py `  

- Open browser: http://localhost:8000/docs  

- Test API

## 14. Update package
```commandline
# Uninstall
pip uninstall fastapi-advertising-prediction

# Delete all files in the dist folder.
rm -rf dist/
 
# Update the version number in the setup.cfg file.

# Re-create the wheels:
python -m build

# Re-upload the new files:
twine upload --repository testpypi dist/* --verbose
```

## 15. Install new version
```commandline
pip install -i https://test.pypi.org/simple/ fastapi-advertising-prediction==0.0.2
```

## 16. Create an account on pypi

## 17. Upload to pypi
```commandline
twine upload --repository pypi dist/* --verbose
```