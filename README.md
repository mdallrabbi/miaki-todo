### Miaki To Do APP ###

``
to install the app
``
```angular2html
database configuration

db_type: postgresql
db_name: miakitodo
db_user: miaki
db_password: password
```
```angular2html
git clone https://github.com/mdallrabbi/miaki-todo.git
cd miakiToDo
virtualenv -p python3 venv
source venv/bin/activate
pip3 install -r "requirements.txt"
python3 manage.py makemigrations
python3 manage.py runserver 
```
``
log can be found at 127.0.0.1:8000
``
```angular2html
python3 manage.py migrate
python3 manage.py createsuperuser
cd frontend
npm start
```
```angular2html
frontend can be found at 127.0.0.1:3000
where api's are browsable at 127.0.0.1:8000
```
###### -EOF- ######