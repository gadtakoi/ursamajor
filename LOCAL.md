## Local setup

### Python
```shell script
sudo apt install python3.8
sudo apt install python3.8-dev
```

### Setup DB
```shell script
sudo -u postgres psql -c 'create database ursamajor;'
sudo -u postgres psql
CREATE ROLE ursamajor WITH LOGIN PASSWORD 'ursamajor';
GRANT ALL PRIVILEGES ON DATABASE ursamajor TO ursamajor;
ALTER USER ursamajor CREATEDB;
```
### Virtualenv

```shell script
cd ursamajor
virtualenv -p /usr/bin/python3.8 venv
source venv/bin/activate
```


### Setup project
```shell script
pip install -r requirements.txt
```

```shell script
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
```

### Run dev server
```shell script
python manage.py runserver
```
