# website


## Start server without Docker
To start virtual env run "pyenv virtualenv 3.11.0 website@3.11.0"
Can also start by running "pyenv activate website@3.11"
And deactivate runnning "pyenv deactivate"
To start server run "python3 manage.py runserver" in terminal

## Start server with Docker
Run:
make build
make compose-start 
press control+c
make compose-start (a second time)

## Install requirements
Run "pip install -r requirements/prod.txt" to install all requirements


### Error encountered
Failed to activate virtualenv.

Perhaps pyenv-virtualenv has not been loaded into your shell properly.
Please restart current shell and try again.

### Resolution
In terminal type the following:
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"


## Creating new pages
https://www.youtube.com/watch?v=lCREG7J7JMg&list=PL39pssg07dpDJas1vxb7Dyw5f8SkAw6c-&index=4 
First navigate to folder location in terminal
Then,
    make compose-manage-py cmd="startapp {app name} {path to app}"
    python3 manage.py startapp {app name} {path to app}

UPDATE(4/5/2024):
1. 
ssh into synology {name}@nas-ipaddress -p{portNumber}
2. Get container ID
sudo docker ps
3. Enter container
sudo docker exec -t -i {ContainerID} bash
4. Navigate to src
cd src
5. start app
run, python3 manage.py startapp {appname} website/apps/{appname}
6. Update the new apps.py, correct the name value to include "website.apps." at the front

When getting errors about libGL.so.1 run:
apt-get update && apt-get install libgl1

## Webpage not refreshing??
Then restart container.
DO NOT DELETE FILES!


## Production model changes
1. After changing models save changes.
2. ssh into nas
3. Run "sudo docker ps"
4. Locate "web containter ID"
5. Run "sudo docker exec -it {containter ID} bash"
6. cd into src
7. run "python3 manage.py makemigrations"
8. run "python3 manage.py migrate"

