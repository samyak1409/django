# [Django](https://en.wikipedia.org/wiki/Django_(web_framework))


Official Site: [djangoproject.com](https://www.djangoproject.com)

Learning from: [Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) (~10hr)

> In this series of videos, we're going to learn how to build a full-featured web application using the Django framework in Python.
Django is a very popular framework that gives us a lot of functionality right out of the box, and makes it really enjoyable to work with these web applications.


## Installing the Dependencies

After downloading this project to your PC, open the project folder, there, open your [Command-line interface](https://en.wikipedia.org/wiki/Command-line_interface) (e.g. Command Prompt for Windows), and run the following:
```
pip install -r requirements.txt
```


## Video-wise Notes in a Nutshell


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

#### 1. Create a new app for our project (Project: [Website](https://en.wikipedia.org/wiki/Website), App: A section of Website (can be [Web Page](https://en.wikipedia.org/wiki/Web_page))):
   ```bash
   python manage.py startapp app_name
   ```
   e.g.
   ```bash
   python manage.py startapp blog
   ```

#### 2. Initialize view(s), route URL(s).


### 3. [Python Django Tutorial: Full-Featured Web App Part 3 - Templates](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how to use templates to return more complex HTML to the browser. We'll also see how we can pass variables to our templates as context. Let's get started...

#### 1. Create HTML template(s) and render them in views.
   *Note: Don't forget to add our app to the list of installed apps (`settings.INSTALLED_APPS`). ([3:25](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3&ab_channel=CoreySchafer&t=205))*

#### 2. Passing data to the template. (Using code in HTML like `{% code %}`, `{{ variable }}`.)

#### 3. Template Inheritance.

#### 4. Add [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)). ([Home](https://getbootstrap.com), [Docs](https://getbootstrap.com/docs), [Examples](https://getbootstrap.com/examples), [Icons](https://icons.getbootstrap.com))
   *Note: Corey added a lot of HTML and CSS for custom structuring and styling, but didn't walk through those snippets as this is backend course, not frontend (or fullstack), so I did not copy-pasted those snippets, but pulled up minimal snippets from Bootstrap, so now I know what the markup mean + a nice minimal look to the website is not bad for someone who's starting out!*

#### 5. Put any static resources (img etc.) in `static` directory. ([see](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3&ab_channel=CoreySchafer&t=2079) till 38:47)

#### 6. Don't hardcode the site-URLs in the HTML, use `url` tag instead:
   ```html
   href="{% url 'url_path_name' %}"
   ```
   e.g.
   ```html
   href="{% url 'about' %}"
   ```


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
   *Now, we can access the admin page, and modify any data directly from there.*


### 5. [Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations](https://www.youtube.com/watch?v=aHC3uTkT9r8&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=5&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be creating database tables for our application using Django models. We will also see how we can use the Django ORM to query the database and filter through results. Let's get started...

*To work with these databases, Django has its own built-in ORM. Now, if you don't know what an ORM is, it stands for Object Relational Mapper, and basically it allows us to access our database in an easy-to-use object-oriented way, and the thing that I like about it the most is that you can use different databases without changing your code, so if you want to use an SQLite database for testing and a Postgres database for production, then all you need to do is set up a different database in our settings, but all the code to query the database will still be the same. And that's what we'll be doing in this series, we'll use an SQLite database for development and a Postgres database for production. So let's go ahead and get started so that we can see what this looks like. Now, the great thing about the django ORM is that we can represent our database structure as classes, and you'll hear those classes be called models, and doing the database structure this way is actually very intuitive after you get the hang of it.*

#### 1. Creating a Model (class). (Class: DB Table, Class Attributes: Table Fields)

#### 2. In order to update the DB with the changes, rerun the two migration commands. ([#4.1](#1-create-the-database-for-project-which-contains-default-tables-to-work-with-using-following-commands))
   *Why migrations are so useful: So, migrations are useful because it allows us to make changes to our database even after it's created and has data. If we didn't have a way to run migrations, then we would have to run some complicated SQL code to update our database structure, so that it doesn't mess with the current data. But with migrations, we can simply make whatever changes we need, run `makemigrations` and then run `migrate`, and it will make all of those changes for us!*

#### 3. Querying the DB using classes in Python Django shell:
   ```bash
   python manage.py shell
   ```
   *See the queries in [`Screenshots/DB Queries`](Screenshots/DB%20Queries) folder.*

#### 4. Passing the real data from DB in the views to the template.
   *[Formatting the date](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#date) as we want.*

#### 5. Don't forget to register newly created model(s) to `admin.py` so that they show up on admin site:
   ```py
   admin.site.register(ClassName)
   ```
   e.g.
   ```py
   admin.site.register(Post)
   ```


### 6. [Python Django Tutorial: Full-Featured Web App Part 6 - User Registration](https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how to use forms and validate user input by creating a user registration page. We will also learn how to install and use Crispy Form so that our forms match the modern style of our application. Let's get started...

#### 1. Create new app `users` (& add it to `settings.INSTALLED_APPS`), initialize its view.

#### 2. Now, to make a registration form, Django has a builtin `UserCreationForm` (A form that creates a user, with no privileges, from the given username and password.).
   *This is kind of similar to the database models in the sense that, we can create Python classes and these classes generate HTML forms for us.*

#### 3. Create template with form, route url (as "Function views" this time, [see](django_project/django_project/urls.py#L6)).

*- x - Till [17:29](https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=7&ab_channel=CoreySchafer&t=1049) - x -*

#### 4. Submitting form using POST request, validating form, creating account (saving the data to the DB), and displaying flash messages.

#### 5. Adding a field (`email`) to our form.

#### 6. To make our form look good, [Crispy Forms: Forms have never been this crispy](https://django-crispy-forms.readthedocs.io):
   1. [Installation](https://django-crispy-forms.readthedocs.io/en/latest/install.html#installing-django-crispy-forms):
      ```bash
      pip install django-crispy-forms
      ```
      Once installed add `'crispy_forms'` to your `INSTALLED_APPS`:
      ```py
      INSTALLED_APPS = [
          '...',
          'crispy_forms'
      ]
      ```
   2. Set [Template Pack](https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs):  
      You can set your default template pack for your project using the `CRISPY_TEMPLATE_PACK` Django settings variable:
      ```py
      CRISPY_TEMPLATE_PACK = 'bootstrap4'
      ```
      For `Bootstrap 5`: Support for newer versions of Bootstrap will be in separate template packs. This starts with version 5 and is available through [crispy-bootstrap5](https://github.com/django-crispy-forms/crispy-bootstrap5):
      ```bash
      pip install crispy-bootstrap5
      ```
      ```py
      INSTALLED_APPS = [
          '...',
          'crispy_forms',
          'crispy_bootstrap5'
      ]
      
      CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
      CRISPY_TEMPLATE_PACK = 'bootstrap5'
      ```
   3. [Usage](https://django-crispy-forms.readthedocs.io/en/latest/filters.html#crispy-filter):
      1. Add `{% load crispy_forms_tags %}` to the template.
      2. Append the `|crispy` filter to your form or formset context variable.


### 7. [Python Django Tutorial: Full-Featured Web App Part 7 - Login and Logout System](https://www.youtube.com/watch?v=3aVqWaLjqS4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=7&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how to create an authentication system for our application so that users can log in and log out. We are also going to see how we can restrict certain pages so that users must be logged-in in order to access the page. Let's get started...

#### 1. Using Django's builtin login & logout views. (`LoginView`, `LogoutView`)
   *Will handle the forms and the logic and all of that stuff for us, but it's not going to handle the templates, which is good because we want to make the templates anyway, so that they match the look and style of our current website.*

#### 2. Make login template, and set `LOGIN_REDIRECT_URL`.
   *With that in place, users are basically being logged in! We just need to add some visual feedback for the same.*
   1. And logout template.

#### 3. 
