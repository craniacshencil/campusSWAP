# CampusSwap
An online marketplace for students to sell their used-goods to fellow students at a competitive price point. Made with Vue + Django.

## Prerequisite Downloads

- [Anaconda](https://www.anaconda.com/download) or [Miniconda](https://docs.anaconda.com/free/miniconda/index.html) => For setting up python and javascript virtual environment (You can run node inside the conda environment)
- [PostgreSQL](https://www.postgresql.org/download/) => or any other SQL database (make changes in settings.py)

## Recommended IDE Setup

- [VSCode](https://code.visualstudio.com/) + [Vue - Official](https://marketplace.visualstudio.com/items?itemName=Vue.volar)
- See [Vite Configuration Reference](https://vitejs.dev/config/).

## Setup

### 1. Setup conda environment with python version 3.11.5:
```bash
conda create -n <env-name> python=3.11.5
```

### 2. Activate the environment:
```bash
conda activate <env-name>
```

### 3. Install the python dependencies: 
```bash
pip install -r requirements.txt
```

### 4. Install Nodejs:
```bash
conda install nodejs
```

### 4. Go to the frontend folder:
```bash
cd frontend
```

### 5. Install all javascript dependencies:
``` bash
npm install
```

### 6. In your root directory, create a ".env" file, file-tree should look like this:
```
.
├── .vscode
├── apis
├── campusSwap
├── frontend
├── products
├── .
├── . (random folders that might be added to the repo in the future)
├── .
├── .gitignore
├── manage.py
├── README.md
├── requirements.txt
└── .env
```

### 7. Go to [imgBB's website to get your api key](https://imgbb.com/) (will take ~2 minutes)

### 8. Add it to your .env file
``` .env
API_KEY=<your-api-key>
```
In case you want to store anything secret, this is the place

### 9. Open your psql shell and create database("INSIDE YOUR SQL SHELL NOT CMD/POWERSHELL"):
``` sql
CREATE DATABASE campusswap;
```

### 10. Change password in your settings.py:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "campusswap",
        "USER": "postgres", #don't change this(unless you know what you are doing)
        "PASSWORD": "YOUR_PASSWORD_HERE",
        "HOST": "localhost",
        "PORT": "5432"
    }
}
```

### 11. Come back to your shell where you are in your python-environment and navigate to the root folder(the folder that you have cloned):
(this assumes that you are in the `frontend` folder from step `4`)
``` bash
cd ..
```

### 12. Make migrations:
```bash
python manage.py makemigrations
```

### 13. Migrate:
```bash
python manage.py migrate
```

### 14. Go to psql, connect to the database and add dummy values to college_students:
``` sql
\c campusswap;
```

### 15. In psql, Insert dummy values(use these for registration):
``` sql
INSERT INTO college_students ("moodleID", first_name, last_name, email) 
VALUES 
(1, 'John', 'Doe', 'johndoe@xyz.edu'), 
(2, 'Jane', 'Smith', 'janesmith@xyz.edu'), 
(3, 'Steve', 'Digg', 'stevedigg@xyz.edu');
```
You are only allowed to use these three accounts to register(not login, yes, register)

### 16. Back to cmd/powershell, Compile and Hot-Reload for Development(make sure you are in the frontend folder):

```sh
npm run dev
```

### 17. Run the Django Server (go back to the root folder):

```bash
python manage.py runserver
```

## FOR PRODUCTION ONLY: Minify for Production

```sh
npm run build
```

## NOTE: 
- #### You need not open the django server on your browser, just keep it running in your terminal. On the browser, it will show "Page not found at /" and a "GET 404 Error" don't worry the server is doing what it is intended to do.
- #### To see if register is working as intended, you can check the `auth_user` table.
- #### You don't need to keep the psql shell open for the DB operations to work.
