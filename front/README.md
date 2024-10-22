main tutorial on django websites: https://www.youtube.com/watch?v=rA4X73E_HV0&list=PL39pssg07dpDJas1vxb7Dyw5f8SkAw6c-&index=1

create project: 
In terminal type:
django-admin startproject namedrop
in the directory you want the project in.

Move files out of nexted directory to main folder. And move manage.py to root directory.

Next to start the server:
Navigate the the "Front" folder in terminal and run:
python manage.py runserver

server will be on http://127.0.0.1:8000 or localhost:8000




# Extra troubleshooting 


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

When getting errors about libGL.so.1 run:
apt-get update && apt-get install libgl1




