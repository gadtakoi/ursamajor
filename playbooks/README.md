**SERVER SETUP** 
ansible-playbook -i inventory.ini playbook-setup.yml

**DB SETUP**
ansible-playbook -i inventory.ini playbook-setup-db.ym

**DEPLOY** 
ansible-playbook playbook-deploy.yml

или

ansible-playbook playbook-deploy.yml -e rev=8d67adea0d1885618b33b65b0fe52900869cd397

- где rev новый Revision Number из git


**SERVER SETUP**

ansible-playbook playbook-setup.yml