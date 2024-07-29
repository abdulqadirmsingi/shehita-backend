create a virtual environment and inside it clone the repository
cd shehita-backend/
pip install -r requirements.txt
cd shehita/
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
