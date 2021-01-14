python -m pip install virtualenv

python -m venv venv

call venv\Scripts\activate.bat
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.in
python -m pip freeze > requirements.txt

