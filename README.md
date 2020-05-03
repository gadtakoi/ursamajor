# Ursa Major

## Installation

**1. CREATE .env**

in folder docker/deploy/, based on dotenv.example

**2. CREATE database.env** 

in folder docker/deploy/postgres/, based on database.env-EXAMPLE

**CREATE inventory.ini** 

in folder playbooks/, based on inventory.ini-EXAMPLE

**3. SETUP SERVER** 

`ansible-playbook -i inventory.ini playbook-setup-server.yml`

**4. UPDATE SERVER** 

`ansible-playbook -i inventory.ini playbook-update-server.yml`

######Здесь возможно придётся зайти на сервер и запустить
`apt upgrade`

######Также после этой команды возможна перезагрузка сервера
 
**5. DB SETUP**

`ansible-playbook -i inventory.ini playbook-setup-db.ym`

**6. BUILD IMAGES**

`cd /docker/build`

`./build_base.sh`

`./build_app.sh`

**7. START PROJECT** 

`ansible-playbook playbook-stopstart.yml -e rev=954c8ta9c1392iv85an5f3ch00414en34k5o5164`

**8. DEPLOY** 

`ansible-playbook playbook-deploy.yml`

or

`ansible-playbook playbook-deploy.yml -e rev=954c8ta9c1392iv85an5f3ch00414en34k5o5164`

- rev is Revision Number from git


### Local development: 
LOCAL.md