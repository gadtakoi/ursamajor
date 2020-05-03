# Ursa Major

## Installation

**CREATE .env**

in folder docker/deploy/, based on dotenv.example

**CREATE database.env** 

in folder docker/deploy/postgres/, based on database.env-EXAMPLE

**CREATE inventory.ini** 

in folder playbooks/, based on inventory.ini-EXAMPLE

**SETUP SERVER** 

`ansible-playbook -i inventory.ini playbook-setup-server.yml`

**UPDATE SERVER** 

`ansible-playbook -i inventory.ini playbook-update-server.yml`

**DB SETUP**

`ansible-playbook -i inventory.ini playbook-setup-db.ym`

**BUILD IMAGES**

`cd /docker/build`

`./build_base.sh`

`./build_app.sh`

**START PROJECT** 

`ansible-playbook playbook-stopstart.yml -e rev=954c8ta9c1392iv85an5f3ch00414en34k5o5164`

**DEPLOY** 

`ansible-playbook playbook-deploy.yml`

or

`ansible-playbook playbook-deploy.yml -e rev=954c8ta9c1392iv85an5f3ch00414en34k5o5164`

- rev is Revision Number from git


### Local development: 
LOCAL.md