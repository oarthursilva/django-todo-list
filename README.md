# django-todo-list

Before start, make sure you've done the configuration set listed on section pre [requisites](#pre-requisites). 

## Pre requisites 

* [Configuring the virtual environment](.doc/prerequisites.md#configuring-the-virtual-environment)
* [Web Driver](.doc/prerequisites.md#web-driver)
  * [Chrome `chromedriver` Driver](.doc/prerequisites.md#chromedriver-chrome)
  * [Firefox `geckodriver` Driver](.doc/prerequisites.md#geckodriver-firefox)
* [Create Project](.doc/prerequisites.md#create-project)
* [Run Server](.doc/prerequisites.md#run-server)

## Creating apps

A feasible approach is to structure the project based on apps, then you could simply mix it up with third-party apps or
even reuse apps from your own repository. 

```bash
python manage.py startapp lists
```

## Test Runner

The automated test runner runs every unit test contained in the project structure, and provides a quick feedback among
the features tested along the project.

```bash
python manage.py test
```
