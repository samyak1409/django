# [Django](https://en.wikipedia.org/wiki/Django_(web_framework))


Official Site: [djangoproject.com](https://www.djangoproject.com)

Learning from: [Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) (~10hr)

> In this series of videos, we're going to learn how to build a full-featured web application using the Django framework in Python.
Django is a very popular framework that gives us a lot of functionality right out of the box, and makes it really enjoyable to work with these web applications.


## Video-wise Notes


### 1. [Python Django Tutorial: Full-Featured Web App Part 1 - Getting Started](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how to get started using the Django framework. We will install the necessary packages and get a basic application running in our browser. Let's get started...

#### 1. Install Django:
   ```bash
   pip install Django
   ```

#### 2. Create a new project:
   ```bash
   django-admin startproject project_name
   ```
   e.g.
   ```bash
   django-admin startproject django_project
   ````

#### 3. Looked at the structure of what gets created.

#### 4. Pull up that default site in the browser:
   ```bash
   python manage.py runserver
   ```


### 2. [Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes](https://www.youtube.com/watch?v=a48xeeo5Vnk&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=2&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be creating a blog application within our Django project. We will also learn how to create URL patterns that are handled by our application views. Let's get started...

#### 1. Create a new app for our project (Project: [Website](https://en.wikipedia.org/wiki/Website), App: [Web Page](https://en.wikipedia.org/wiki/Web_page)):
   ```bash
   python manage.py startapp app_name
   ```
   e.g.
   ```bash
   python manage.py startapp blog
   ```

#### 2. Create view(s), route URL(s).


### 3. [Python Django Tutorial: Full-Featured Web App Part 3 - Templates](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how to use templates to return more complex HTML to the browser. We'll also see how we can pass variables to our templates as context. Let's get started...

#### 1. Create HTML template(s) and render them in views.
   *Note: Don't forget to add our app to the list of installed apps. ([3:25](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3&ab_channel=CoreySchafer&t=205))*

#### 2. Passing data to the template. (Using code in HTML like `{% code %}`, `{{ variable }}`.)

#### 3. Template Inheritance.

#### 4. Add [Bootstrap](https://getbootstrap.com) (**Imp**: [Docs](https://getbootstrap.com/docs), [Examples](https://getbootstrap.com/examples), [Icons](https://icons.getbootstrap.com)).
   *Note: Corey added a lot of HTML and CSS for custom structuring and styling, but didn't walk through those snippets as this is backend course, not frontend (or fullstack), so I did not copy-pasted those snippets, but pulled up minimal snippets from Bootstrap, so now I know what the markup mean + a nice minimal look to the website is not bad for someone who's starting out!*

#### 5. Put any static resources (img etc.) in `static` directory. ([see](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3&ab_channel=CoreySchafer&t=2079) till 38:47)

#### 6. Don't hardcode the URLs in the HTML, use `url` tag instead.


### 4. [Python Django Tutorial: Full-Featured Web App Part 4 - Admin Page](https://www.youtube.com/watch?v=1PkNiYlkkjo&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=4&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how to access the Django Admin Page for our application. The Administration Page is a great way to see what data is currently in our application, and also gives us a nice GUI for creating or modifying that data. Let's get started...

#### 1. Create the database for project which contains default tables to work with using following commands:
   1. Make migrations for database changes (basically generate some data from our created/updated model(s), which will be used for generating SQL, which will in turn make changes to the database):
      ```bash
      python manage.py makemigrations
      ```
   2. Apply them:
      ```bash
      python manage.py migrate
      ```

#### 2. Create admin ([superuser](https://en.wikipedia.org/wiki/Superuser)):
   ```bash
   python manage.py createsuperuser
   ```

#### 3. Now, we can access the admin page, and modify any data directly from there!

