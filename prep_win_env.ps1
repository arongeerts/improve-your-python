$env:pathext = $env:pathext + ";.PY"
pip install virtualenvwrapper-win==1.2.6
pip install poetry==1.1.4
python -m venv venv
venv\Scripts\activate
python --version
pip install poetry==1.1.4
poetry install
