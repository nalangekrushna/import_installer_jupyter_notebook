# import_installer_jupyter_notebook
finds all import in jupyter notebook, check if they are alredy present if not then install it.

This is mostly useful in the case you got jupyter notebook from someone else and instead of manually installing every requirement it will install all requirements once.

Installation
pip install jupyter_installer

How to use
from jupyter_installer import run
run('file_name.ipynb')
