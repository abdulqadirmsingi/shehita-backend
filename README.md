Install python in your PC https://www.python.org/downloads/windows/
create a virtual environment using the command: python -m venv .venv

and inside it clone the repository
cd shehita-backend/
pip install -r requirements.txt
cd shehita/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
