$env:pathext = $env:pathext + ";.PY"
pip install virtualenvwrapper-win==1.2.6
pip install -r requirements.txt
python -m venv venv
venv\Scripts\activate
python --version
pip install -r requirements.txt
poetry install
