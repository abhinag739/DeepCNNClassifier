import os
from pathlib import Path #displays path in backward slash in windows system, and in forward slash in a Linux system
                        #example print(Path('x/v/z.txt')) --> will print x\v\z.txt
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s: ')        

                        

package_name = "DeepCNNClassifier"
list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/components/__init__.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/config/__init__.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/entity/__init__.py",
    f"src/{package_name}/constants/__init__.py",
    "configs/config.yaml",
    "dvc.yaml",  #dvc.yaml = data version control pipeline
    "params.yaml", #contains all our parameters
    "init_setup.sh",  #initial setup file
    "requirements.txt",  #names of all packages that needs to be installed
    "requirements_dev.txt", #development requirements, requirements thats only used for development
    "setup.py",        #
    "setup.cfg",       # These files are required only when python package is being created
    "pyproject.toml",  #
    "tox.ini",         #Used for Testing of a project locally
    "research/trials.ipynb",  #Trial files of whatever we want to test in an ipynb file
    "example.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass #do nothing, just created an empty file
            logging.info(f"Creating empty file: {filename})")
    else:
        logging.info(f"filename {filename} already exists")

    




                             