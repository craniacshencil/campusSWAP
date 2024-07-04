# CampusSwap

An online marketplace for students to sell their used-goods to fellow students at a competitive price point. Made with Vue + Django.

## Prerequisite Downloads

- [Anaconda](https://www.anaconda.com/download) or [Miniconda](https://docs.anaconda.com/free/miniconda/index.html) => For setting up python and javascript virtual environment (You can run node inside the conda environment)
- [PostgreSQL](https://www.postgresql.org/download/) => or any other SQL database (make changes in settings.py)

## Recommended IDE Setup

- [VSCode](https://code.visualstudio.com/) + [Vue - Official](https://marketplace.visualstudio.com/items?itemName=Vue.volar)
- See [Vite Configuration Reference](https://vitejs.dev/config/).

## Setup

### 1. Python setup

#### 1.1. Setup conda environment with python version 3.11.5:

```bash
conda create -n <env-name> python=3.11.5
```

#### 1.2. Activate the environment:

```bash
conda activate <env-name>
```

#### 1.3. Install the python dependencies:

```bash
pip install -r requirements.txt
```

#### 1.4. Install Nodejs(If you don't have it already installed):

```bash
conda install nodejs
```

### 2. Vue setup:

#### 2.1. Go to the frontend folder:

```bash
cd frontend
```

#### 2.2. Install all javascript dependencies:

```bash
npm install
```

### 3. Third-party API Setup:

#### 3.0. Get back to root directory:

```sh
cd ..
```

#### 3.1. In your root directory, create a ".env" file, file-tree should look like this:

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

#### 3.2. Go to [ImgBB's website to get your api key](https://imgbb.com/) (will take ~2 minutes)

#### 3.3. Go to [Razorpay's website to get an rzp_secret and rzp_id](https://razorpay.com/) (will take ~10 minutes):

#### 3.4. Add this in your .env file(**Do not change the names of the variables in the .env STRICTLY**):

```.env
RZP_SECRET=<your_rzp_secret>
RZP_ID=<your_rzp_id>
API_KEY=<your-imgbb-api-key>
```

In case you want to store anything secret, this is the place

### 4. Create database in psql/pgAdmin:

```sql
CREATE DATABASE campusswap;
```

### 5. Django Setup:

#### 5.1. Change password in your settings.py:

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

#### 5.2. Make migrations:

```sh
python manage.py makemigrations
```

#### 5.3. Migrate:

```sh
python manage.py migrate
```

#### 5.4. Create superuser(admin):

```sh
python manage.py createsuperuser --username 1234
```

(make sure username is numerical, i.e just copy the command above as it is)
Then fill out all the fields as you are prompted

#### 5.5 Open the Django shell:

```sh
python manage.py shell
```

#### 5.6 Set first_name, last_name for admin:

```sh
from django.contrib.auth.models import User
user = User.objects.get(username = 1234)
user.first_name = "John"
user.last_name = "Doe"
user.save()
```

### 6. Postgres Setup:

#### 6.1. Go to psql, connect to the database:

```sql
\c campusswap;
```

#### 6.2 In psql, Insert dummy values(use these for registration):

```sql
INSERT INTO college_students ("moodleID", first_name, last_name, email)
VALUES
(1, 'John', 'Doe', 'johndoe@xyz.edu'),
(2, 'Jane', 'Smith', 'janesmith@xyz.edu'),
(3, 'Steve', 'Digg', 'stevedigg@xyz.edu');
```

You are only allowed to use these three accounts to **register(not login, yes, register)**

### 7. Running the Project:

#### 7.1 Run the Django Server:

```bash
python manage.py runserver
```

#### 7.2. Compile and Hot-Reload for Development(make sure you are in the frontend folder):

```sh
cd frontend
npm run dev
```

## FOR PRODUCTION ONLY: Minify for Production

```sh
npm run build
```

## NOTE:

- #### You need not open the django server on your browser, just keep it running in your terminal. On the browser, it will show "Page not found at /" and a "GET 404 Error" don't worry the server is doing what it is intended to do.
- #### To see if register is working as intended, you can check the `auth_user` table.
- #### You don't need to keep the psql shell open for the DB operations to work.
- #### If tables for certain apps are not being created:
  ##### Current apps include: apis, products, admin_actions, payments.
```sh
python manage.py makemigrations <app_name>
```
- #### if you get a vite not found error on running npm run dev:

```sh
npm i vite
```
