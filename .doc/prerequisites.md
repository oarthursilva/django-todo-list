## Configuring the virtual environment

Starting the virtual environment

```bash
$ pip install virtualenv
$ virtualenv venv -p python3
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ cp contrib/env-sample .env
```

Deactivating the virtual environment

```bash
$ venv\Scripts\deactivate
```

## Web Driver

WebDriver is an open source tool for automated testing of webapps across many browsers. It provides capabilities for navigating to web pages, user input, JavaScript execution, and more.

### chromedriver (Chrome)

Download and unpack geckp driver from https://sites.google.com/a/chromium.org/chromedriver/home and unpack into `Python\Python{version}\Scripts`

Make sure the chromedriver version matches with the Chrome version, otherwise it won't work.

### geckodriver (Firefox)

Download and unpack gecko driver from https://github.com/mozilla/geckodriver/releases and unpack into `Python\Python{version}\Scripts`

Open the terminal and you'll be able to run

```bash
$ geckodriver --version
```

## Create Project

Statement below create the project folder which intent to store project global configuration.

```bash
$ django-admin.py startproject ${project name} .
```

## Create Apps

A feasible approach is to structure the project based on apps, then you could simply mix it up with third-party apps or
even reuse apps from your own repository. 

```bash
$ python manage.py startapp lists
```

#### Adjust THE `settings.py` in `config`

In the settings.py of your `config_project` dir, add the newly app in `INSTALLED_APPS` 

#### Using Postgres as default database

- see `docker-compose.yml` to manage `postgres` before proceed.

Point the default `database` to postgres in `config/settings.py` file

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'pguser',
        'PASSWORD': 'pguser',
        'HOST': 'db',
        'PORT': 5432,
    }
}
```

Run `manage.py migrate` to migrate, and postgres is now configured and accessible.

#### Providing initial data

Database data for fixture or fixtures. It pre populates the database with hardcoded data

- entire project

```bash
# export
manage.py dumpdata > fixture/initial.json
# import
manage.py loaddata fixture/initial.json
```

- app-specific

```bash
# export
manage.py dumpdata lists > fixture/lists-initial-data.json
# import
manage.py loaddata fixture/lists-initial-data.json
```

## Run Server

Perform the statement below to run a local development server

```bash
$ python manage.py runserver
```

The output should be something similar than below, and Django should now get up and running.

```bash
System check identified no issues (0 silenced).
May 28, 2020 - 22:51:22
Django version 1.11.17, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

## Functional Test

It ensures that end products, modules & components are working exactly as specified

```bash
$ python test/test_functional.py
```

#### Test Database with `LiveServerTestCase`

It will automatically create a test database, and start up a development server for the functional tests to run against

```bash
$ python manage.py test functional_tests
```

## Unit Test Runner

The automated test runner runs every unit test contained in the project structure, and provides a quick feedback among
the features tested along the project. Make the functional test class inherit `LiveServerTestCase`.

```bash
$ python manage.py test
```

Write a dummy test in `lists/views`, and execute the test runners. An assert fail message is displayed indicating the 
test ran successfully.

```python
def test_should_return_an_error_when_math_failed(self):
    self.assertEquals(1 + 1, 3)
```
