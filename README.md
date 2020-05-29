# Django

Make sure all prerequisites in the list below matched before start any coding.
 
* [Configuring the virtual environment](#configuring-the-virtual-environment)
* [Web Driver](#web-driver)
  * [Chrome `chromedriver` Driver](#chromedriver-chrome)
  * [Firefox `geckodriver` Driver](#geckodriver-firefox)
* [Run Server](#run-server)

## Configuring the virtual environment

Starting the virtual environment

```
$ pip install virtualenv
$ virtualenv venv -p python3
$ venv\Scripts\activate
$ pip install -r requirements.txt
```

Deactivating the virtual environment

```text
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

```text
$ geckodriver --version
```

- Create the main container

Statement below create the project folder which intent to store project global configuration.

```
$ django-admin.py startproject ${project name} .
```

### Run Server

Perform the statement below to run a local development server

```
$ python manage.py runserver
```

The output should be something similar than below, and Django should now get up and running.

```
System check identified no issues (0 silenced).
May 28, 2020 - 22:51:22
Django version 1.11.17, using settings 'superlists.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

```