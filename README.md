# webCalc

This is a web-based linear multistep method calculator built  as a final year project (2021) in collaboration with [Deborah Adaramola](https://github.com/Dee-ia).

## Setup

- Clone the project and navigate to the project directory

```shell
path_to_dir> git clone https://github.com/IfeOlulesi/webCalc.git

path_to_dir> cd webCalc
```

- Create a virtual environment

```shell
path_to_dir/webCalc> py -m venv env
# Create a virtual environment named `env` in the current directory

path_to_dir> env\Scripts\activate
# Activate the virtual environment

# You should see (env) before path_to_dir after
# activating the virtual environment
```

- Install 3rd party libraries

```shell
(env) path_to_dir/webCalc> pip install -r requirements.txt
```

- Run the Django server

```shell
# Ensure you're at the root directory and run this command
(env) path_to_dir/webCalc> py manage.py runserver

# This should start the server at port 8000 on your localhost

# If you're not automatically redirected to http://localhost:8000, 
# then copy the link and paste in your browser.
```
