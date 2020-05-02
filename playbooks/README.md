**CREATE .env in docker/deploy based on dotenv.example **

**SETUP SERVER** 
ansible-playbook -i inventory.ini playbook-setup-server.yml

**UPDATE SERVER** 
ansible-playbook -i inventory.ini playbook-update-server.yml

**DB SETUP**
ansible-playbook -i inventory.ini playbook-setup-db.ym

**DEPLOY** 
ansible-playbook playbook-deploy.yml

или

ansible-playbook playbook-deploy.yml -e rev=8d67adea0d1885618b33b65b0fe52900869cd397

- где rev новый Revision Number из git


**SERVER SETUP**

ansible-playbook playbook-setup.yml