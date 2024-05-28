import os
import sys
import logging
from pathlib import Path
logging.basicConfig(level = logging.INFO,format ='[%(asctime)s]:%(messages)s')
project_name = "Cnnclassifier"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configurationmanager.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/constants.py",
    f"src/{project_name}/pipeline/__init__.py",
    "config/config.yaml",
    "research/trails.ipynb",
    "requirements.txt",
    "templates/index.html",
    "setup.py",
    "dvc.yaml",
    "params.yaml"
    ]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")
