# django-todo-list

![tdd-diagram](.images/img-1.png)

Before start, make sure you've done the configuration set listed on section pre [requisites](#pre-requisites). 

## Pre requisites 

* [Configuring the virtual environment](.doc/prerequisites.md#configuring-the-virtual-environment)
* [Web Driver](.doc/prerequisites.md#web-driver)
  * [Chrome `chromedriver` Driver](.doc/prerequisites.md#chromedriver-chrome)
  * [Firefox `geckodriver` Driver](.doc/prerequisites.md#geckodriver-firefox)
* [Create Project](.doc/prerequisites.md#create-project)
* [Create Apps](.doc/prerequisites.md#create-apps)
  * [Adjust `settings.py` in `super`](#.doc/prerequisites.md#adjust-settingspy-in-super)
* [Run Server](.doc/prerequisites.md#run-server)
* [Functional Test](.doc/prerequisites.md#functional-test)
  * [Test Database with `LiveServerTestCase`](.doc/prerequisites.md#test-database-with-liveservertestcase)
* [Unit Test Runner](.doc/prerequisites.md#unit-test-runner)

## Development
* [URL Mapping](#url-mapping)
* [HTML Template](#html-template)
* [Model](#model)
  * [Database Migration](#database-migration)
* [Redirect after a POST](#redirect-after-a-post)
* [Iterate items in HTML template](#iterate-items-in-html-template)
---

### URL Mapping

Django uses a file called `urls.py` to map URLs to Views functions. The main `urls.py` is located at super project dir

At the example below, the url path `/` is mapped for view function `main`.

```python
from django.contrib import admin
from django.urls import path
from lists.views import main

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main-view')
]
```

### HTML Template

Templates consists of substituting Python variables into HTML text. By default, Django automatically search folders 
called `template` in the app structure `dir`.

```text
create a directory called template in app dir
add a *.html file 
``` 

Adjust the `views.py` to render the proper template when the page loading. 

```python
def main_view(request):
    return render(request, 'main.html')

```

### Model

In the `list/models.py`, create a ORM model called `Item` and make it inherit from the `Model`.

The `Item` class will be used in a HTML5 table.

```python
from django.db import models

class Item(models.Model):
    text = models.TextField(default='')
 ```

#### Database Migration

The ORM role is to model the database, giving the ability to add and remove columns base on changes in models.

```bash
django.db.utils.OperationalError: no such table: lists_item
```

Before migrate, create a file called _db.sqlite3_ at the root project `dir`. Then, migrate models to the database. 

```bash
$ manage.py makemigrations
```

### Redirect after a POST

As a good practice, always redirect after a POST even for the same page, instead of rendering the response on it.

```python
if request.method == 'POST':
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/')
    ...
```

### Iterate items in HTML template

Django template syntax has a tag for iterating through lists

```html
<table id="id_list_table">
    {% for item in items %}
    <tr><td>{{ forloop.counter }}: {{ item.text }}</td></tr>
    {% endfor %}
</table>
```

At the main view, pass the list item while rendering `items`

```python
def main_view(request):
    ...
    items = Item.objects.all()
    return render(request, 'main.html', {'items': items})
```