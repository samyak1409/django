# [Django](https://en.wikipedia.org/wiki/Django_(web_framework))


Official Site: [djangoproject.com](https://www.djangoproject.com)

Learnt from: [Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) (~10hr)

> In this series of videos, we're going to learn how to build a full-featured web application using the Django framework in Python.
> Django is a very popular framework that gives us a lot of functionality right out of the box, and makes it really enjoyable to work with these web applications.


## Screenshots

### Homepage of the website
![](Screenshots/01.%20Home1.png)
![](Screenshots/02.%20Home2.png)

### Full post can be read by opening the Post page
![](Screenshots/03.%20PostRead.png)

### Users can Register
![](Screenshots/04.%20Register.png)

### And then, can Log In to the site
![](Screenshots/05.%20Login.png)

### After logging in, links in the header navbar will change
![](Screenshots/06.%20Home3.png)

### Profile page, from where users can see their Posts, Log Out, and update Profile Info
![](Screenshots/07.%20Profile.png)

### Users can Create new posts
![](Screenshots/08.%20PostCreate.png)

### Users can Update/Delete their posts
![](Screenshots/09.%20PostUpdateDelete.png)

### Users can see posts by a particular user
![](Screenshots/10.%20UserPosts.png)

### Users can request Password Reset link to their email if they can't remember the password
![](Screenshots/11.%20PassReset.png)

### A RESTful public API is also available @[/api1](http://localhost:8000/api1):
![](Screenshots/12.%20RESTful%20API.png)
<details>
<summary>Click here to see individual endpoints.</summary> <br>

![](Screenshots/12.a.%20All%20Posts.png)
![](Screenshots/12.b.%20Single%20Post.png)
![](Screenshots/12.c.%20Posts%20by%20a%20User.png)
</details>


## Run on your PC

*Note that [Python](https://www.python.org/downloads) needs to be installed.*

1. [Download the Project](https://github.com/samyak1409/django/archive/refs/heads/main.zip)
2. Extract the downloaded zip (`django-main.zip`).
3. Open the `django-main` directory. (You should see a `requirements.txt` there.)
4. There, open your [Command-line interface](https://en.wikipedia.org/wiki/Command-line_interface) (e.g. Command Prompt for Windows), and run the following (make sure you're connected to the internet):
   ```bash
   pip install -r requirements.txt
   cd django_project
   python manage.py runserver
   exit
   ```
   This will install the project dependencies, and start the server on your on PC.
5. Now, just click/go on the link [127.0.0.1:8000](http://127.0.0.1:8000) to access the website!

*Note that in order to make [Password Reset](#users-can-request-password-reset-link-to-their-email-if-they-cant-remember-the-password) functionality work on your local machine / server, you're needed to create [Google App Password](https://myaccount.google.com/apppasswords), and add environment variables. [Details](#2-page-which-will-input-the-new-pass-added-passwordresetconfirmview-in-urlspy-and-created-a-template-reset_linkhtml-extending-form_basehtml).*


## Video-wise Notes in a Nutshell


### 1. [Python Django Tutorial: Full-Featured Web App Part 1 - Getting Started](https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=1&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how to get started using the Django framework. We will install the necessary packages and get a basic application running in our browser. Let's get started...

#### 1. Install Django:
- ```bash
  pip install Django
  ```

#### 2. Create a new project:
- ```bash
  django-admin startproject project_name
  ```
  e.g.
  ```bash
  django-admin startproject django_project
  ````

#### 3. Looked at the structure of what gets created.

#### 4. Pull up that default site in the browser:
- ```bash
  python manage.py runserver
  ```
  [127.0.0.1:8000](http://127.0.0.1:8000) or [localhost:8000](http://localhost:8000)


### 2. [Python Django Tutorial: Full-Featured Web App Part 2 - Applications and Routes](https://www.youtube.com/watch?v=a48xeeo5Vnk&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=2&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be creating a blog application within our Django project. We will also learn how to create URL patterns that are handled by our application views. Let's get started...

#### 1. Create a new app for our project (Project: [Website](https://en.wikipedia.org/wiki/Website), App: A section of Website (can be [Web Page](https://en.wikipedia.org/wiki/Web_page))):
- ```bash
  python manage.py startapp app_name
  ```
  e.g.
  ```bash
  python manage.py startapp blog
  ```

#### 2. Initialize view(s), route url(s).


### 3. [Python Django Tutorial: Full-Featured Web App Part 3 - Templates](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how to use templates to return more complex HTML to the browser. We'll also see how we can pass variables to our templates as context. Let's get started...

#### 1. Create HTML template(s) and `render` them in views.
1. Don't forget to add our app to the list of installed apps (`settings.INSTALLED_APPS`). ([3:25](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3&ab_channel=CoreySchafer&t=205))

#### 2. Passing data to the template. (Using code in HTML like `{% code %}`, `{{ variable }}`.)

#### 3. Template Inheritance. (`{% block block_name %}{% endblock %}`)

#### 4. Add [Bootstrap](https://en.wikipedia.org/wiki/Bootstrap_(front-end_framework)). ([Home](https://getbootstrap.com), [Docs](https://getbootstrap.com/docs), [Examples](https://getbootstrap.com/examples), [Icons](https://icons.getbootstrap.com))
- *Note: Corey added a lot of HTML & CSS for custom structuring & styling, but didn't walk through those snippets as this is backend course, not frontend (or fullstack), so I did not copy-pasted those snippets, but pulled up minimal snippets from Bootstrap, so now I know what the markup mean + a nice minimal look to the website is not bad for someone who's starting out!*

#### 5. Put any static resources (img etc.) in `static` directory. ([see](https://www.youtube.com/watch?v=qDwdMDQ8oX4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=3&ab_channel=CoreySchafer&t=2079) till 38:47)

#### 6. Don't hardcode the site-URLs in the HTML, use `url` tag instead:
- ```html
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
   *Note: If you want to see the SQL query that's going to be run when we'll apply the migrations, run:*
   ```bash
   python manage.py sqlmigrate app_name migration_id
   ```
   e.g.
   ```bash
   python manage.py sqlmigrate blog 0001
   ```
2. Apply them:
   ```bash
   python manage.py migrate
   ```

#### 2. Create admin ([superuser](https://en.wikipedia.org/wiki/Superuser)):
- ```bash
  python manage.py createsuperuser
  ```
  *Now, we can access the [admin page](http://localhost:8000/admin), and modify any data directly from there.*


### 5. [Python Django Tutorial: Full-Featured Web App Part 5 - Database and Migrations](https://www.youtube.com/watch?v=aHC3uTkT9r8&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=5&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be creating database tables for our application using Django models. We will also see how we can use the Django ORM to query the database and filter through results. Let's get started...

*To work with these databases, Django has its own built-in ORM. Now, if you don't know what an ORM is, it stands for Object Relational Mapper, and basically it allows us to access our database in an easy-to-use object-oriented way, and the thing that I like about it the most is that you can use different databases without changing your code, so if you want to use an SQLite database for testing and a Postgres database for production, then all you need to do is set up a different database in our settings, but all the code to query the database will still be the same. And that's what we'll be doing in this series, we'll use an SQLite database for development and a Postgres database for production. So let's go ahead and get started so that we can see what this looks like. Now, the great thing about the django ORM is that we can represent our database structure as classes, and you'll hear those classes be called models, and doing the database structure this way is actually very intuitive after you get the hang of it.*

#### 1. Creating a Model (class) (`Post`). (Class: DB Table, Class Attributes: Table Fields)

#### 2. In order to update the DB with the changes, rerun the two migration commands. ([#4.1](#1-create-the-database-for-project-which-contains-default-tables-to-work-with-using-following-commands))
- *Why migrations are so useful: So, migrations are useful because it allows us to make changes to our database even after it's created and has data. If we didn't have a way to run migrations, then we would have to run some complicated SQL code to update our database structure, so that it doesn't mess with the current data. But with migrations, we can simply make whatever changes we need, run `makemigrations` and then run `migrate`, and it will make all of those changes for us!*

#### 3. Querying the DB using classes in Python Django shell:
- ```bash
  python manage.py shell
  ```
  See the queries in [`Resources/DB Queries/1. Post`](Resources/DB%20Queries/1.%20Post) folder.

#### 4. Passing the real data from DB in the views to the template.
- *[Formatting the date](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#date) as we want.*

#### 5. Don't forget to register newly created model(s) to `admin.py` so that they show up on admin site:
- ```py
  from .models import ModelName
  admin.site.register(ModelName)
  ```
  e.g.
  ```py
  from .models import Post
  admin.site.register(Post)
  ```


### 6. [Python Django Tutorial: Full-Featured Web App Part 6 - User Registration](https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how to use forms and validate user input by creating a user registration page. We will also learn how to install and use Crispy Form so that our forms match the modern style of our application. Let's get started...

#### 1. Create new app `users` (and add it to `settings.INSTALLED_APPS`), initialize its view.

#### 2. Now, to make a registration form, Django has a builtin `UserCreationForm` (A form that creates a user, with no privileges, from the given username and password.).
- *This is kind of similar to the database models in the sense that, we can create Python classes and these classes generate HTML forms for us.*

#### 3. Create template with form, route url (as "Function views" this time, [see](django_project/django_project/urls.py#L6)).

*- x - Till [17:29](https://www.youtube.com/watch?v=q4jPR-M0TAQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=6&ab_channel=CoreySchafer&t=1049) - x -*

#### 4. Submitting form using POST request, validating form, creating account (saving the data to the DB), and displaying flash messages.

#### 5. Adding a field (`email`) to our form. (by extending the `UserCreationForm` and adding a new field to the extended form (named `RegistrationForm`))

#### 6. To make our form look good, [Crispy Forms: Forms have never been this crispy](https://django-crispy-forms.readthedocs.io):
1. [Installation](https://django-crispy-forms.readthedocs.io/en/latest/install.html#installing-django-crispy-forms):
   ```bash
   pip install django-crispy-forms
   ```
   Once installed add `'crispy_forms'` to your `INSTALLED_APPS`:
   ```py
   INSTALLED_APPS = [
       ...
       'crispy_forms',
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
       ...
       'crispy_forms',
       'crispy_bootstrap5',
   ]
   
   CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
   CRISPY_TEMPLATE_PACK = 'bootstrap5'
   ```
3. [Usage](https://django-crispy-forms.readthedocs.io/en/latest/filters.html#crispy-filter):
   1. Add `{% load crispy_forms_tags %}` to the template.
   2. Append the `|crispy` filter to your form or formset context variable.


### 7. [Python Django Tutorial: Full-Featured Web App Part 7 - Login and Logout System](https://www.youtube.com/watch?v=3aVqWaLjqS4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=7&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how to create an authentication system for our application so that users can log in and log out. We are also going to see how we can restrict certain pages so that users must be logged-in in order to access the page. Let's get started...

#### 1. Using Django's builtin login & logout [class-based views](django_project/django_project/urls.py#L9). (`LoginView`, `LogoutView`)
- *Will handle forms, logic, and all of that stuff for us, but it's not going to handle the templates, which is good because we want to make the templates anyway, so that they match the look & style of our current website.*

#### 2. Make login template, and set `LOGIN_REDIRECT_URL` in `settings.py`.
- *With that in place, users are actually being logged in! We just need to add some visual feedback (next point) for the same.*
1. And logout template.

#### 3. Changing the nav bar links depending on if `user.is_authenticated` or not.

#### 4. Create `Profile` url, view, template.

#### 5. Restrict going to `/profile` if not authenticated (logged in) (using `django.contrib.auth.decorators.login_required` decorator).
1. Also, need to set `LOGIN_URL` in `settings.py`.
- *With `login_required` decorator, `next` parameter will automatically be added in the url so that it remembers where to redirect after logging in.*


### 8. [Python Django Tutorial: Full-Featured Web App Part 8 - User Profile and Picture](https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be creating a user profile that extends the built-in Django User model. We will then use this user profile to store profile pictures for each user. We will also be learning how to set the MEDIA_ROOT, MEDIA_URL, and also make our static files accessible through our URL patterns. Finally, we will create a receiver function for a Django signal that will make sure our profiles are created when a user first registers. Let's get started...

#### 1. Creating a new model (class) (`Profile`) which extends the Django's `User` model, in order to add a `pic` field.
- *Django's default `User` model, doesn't have a field for profile pic, so we can extend the (`User`) model, and add whatever fields we want to the extended model (named `Profile`).*
1. In order to use `models.ImageField`,
   ```bash
   pip install Pillow
   ```
2. [#5.2](#2-in-order-to-update-the-db-with-the-changes-rerun-the-two-migration-commands-41) (Run Migrations)
3. [#5.5](#5-dont-forget-to-register-newly-created-models-to-adminpy-so-that-they-show-up-on-admin-site) (Register Model)

#### 2. Changing where the media is saved & from what url it can be accessed by adding the `MEDIA_ROOT` & `MEDIA_URL` respectively in `settings.py`.
- *By default, `MEDIA_ROOT` is the base dir of our project, so if different models started making different dirs at the base dir, then it will be cluttered up.*

#### 3. [Querying](Resources/DB%20Queries/2.%20Profile) the `Profile` model using `User` model (as they're connected/linked by `OneToOneField`).
1. But no profiles exist currently, so, first add a few from the admin page (as we've not implemented "when the user is created, profile is created with it" yet).

#### 4. Now, the main part, Showing profile pic on the profile page.
1. Update the profile template `profile.html`, with the user profile pic url (`user.profile.pic.url`).
2. Adding `MEDIA_URL` to `urlpatterns`. ([Serving files uploaded by a user during development](https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development)) ([see](https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8&ab_channel=CoreySchafer&t=1258) till 24:33)
   - *Now, we can see the profile pic on profile page.*
3. Adding [Corey's styles](https://github.com/CoreyMSchafer/code_snippets/blob/master/Django_Blog/snippets/main.css) (to the `static` dir) so that profile page look right.
4. Adding the default profile pic. (Remember? Check [`Profile`](django_project/users/models.py))

*- x - Till [26:18](https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8&ab_channel=CoreySchafer&t=1578) - x -*

#### 5. Using Signals: Set to auto create the Profile (with the default profile pic) whenever a new user is created.
- *Till now, we were adding the pic from the admin page only.*
- **But, why are we doing all this? Wouldn't an image (profile pic) input field in the `RegistrationForm` itself be a way better method!?**


### 9. [Python Django Tutorial: Full-Featured Web App Part 9 - Update User Profile](https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be finishing our user profile page. The final page will allow users to update their information and also add a new profile picture. We will also learn how to resize this image when it is uploaded to save space on our web server. Let's get started...

#### 1. For giving the option of updating username, email, and profile pic:
1. Creating 2 update forms (extending `forms.ModelForm`) in `forms.py`. (for `User` & `Profile` model)
2. Add the forms in `profile` view and pass to the template through `context`.
3. Update template with the 2 forms in the `form` HTML tag.
   1. Don't forget to add `enctype="multipart/form-data"` in `form`. (for passing image data properly)
4. Update the `profile` view to handle the post request. (same as [#6.4](#4-submitting-form-using-post-request-validating-form-creating-account-saving-the-data-to-the-db-and-displaying-flash-messages))

#### 2. Override the `save` method in `Profile` model in order to resize whenever a large pic is uploaded for saving space.

#### 3. Add the profile pics on the home page.


### 10. [Python Django Tutorial: Full-Featured Web App Part 10 - Create, Update, and Delete Posts](https://www.youtube.com/watch?v=-s7e_Fy6NRU&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=10&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how to use class-based views in order to create, update, and delete posts. These class-based views are very convenient once we get used to using them properly. Let's get started...

*We'll be using some Django builtin [class-based views](django_project/django_project/urls.py#L9) for adding [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) posts functionality.
There are many class-based views (see `django.views.generic.__all__`), here we'll be using following ones:
`CreateView`, `DetailView`, `UpdateView`, `DeleteView`, `ListView`*

#### 1. Removed function view `home`, & created class-based view `PostListView` for homepage. (List Posts Functionality)
1. Configured some variable names.
2. Changed the ordering of the posts list.
3. Changed view in `urlpatterns` in `urls.py`.
- *And we're done! No need to query the DB, render the template etc. (like we were doing while using function view `home`)*.

#### 2. Dedicated Post Page (Read Post Functionality)
- *Corey didn't follow DRY, and created this view not inheriting from `PostListView` and a new template, which is bad, so I did it the way it should've been done.*
1. Created `PostDetailView` inheriting `PostListView` (overridden `get_queryset` in order to get single post).
2. Added url pattern, with variable in the pattern. (`'/post/<int:pk>/'`)

#### 3. Create Post Functionality
1. Created `PostCreateView` & routed url.
2. Created template `post_form` (inherited from `users/form_base.html`).
3. In view, override `form_valid` method in order to set the author for the post we're creating to the current logged-in user.
- *With that in place, post can be created successfully, but `success_url` is not defined yet, which means, at what url to go once the post creation is successful. (Post will be created, but after that, an error will be raised.)*
4. Defining `get_absolute_url` method in `Post` model, which will be used by `PostCreateView` to redirect to that url.
5. One last thing, like [#7.5](#5-restrict-going-to-profile-if-not-authenticated-logged-in-using-djangocontribauthdecoratorslogin_required-decorator), for class-based views, we have to use `django.contrib.auth.mixins.LoginRequiredMixin`. (Posts shouldn't be created anonymously.)

#### 4. Update Post Functionality
1. Created `PostUpdateView` & routed url.
2. Now, `CreateView` & `UpdateView` uses the same template, so, passed `heading` through `extra_context` from the views themselves.
- *With that in place, posts can be updated successfully.*
3. Here, we need not only `LoginRequiredMixin`, but also `UserPassesTestMixin` (& override `test_func`), using that we forbid users to update the posts they're not the author of.

#### 5. Delete Post Functionality
1. Created `PostDeleteView` w/ `LoginRequiredMixin` & `UserPassesTestMixin` (& same `test_func`), routed url.
2. Created `post_confirm_delete.html`. (It will be just a confirmation form, where submit button will lead to post deletion.)
3. Set `success_url` in view. (Url to redirect on after deleting the post.)
- *Now, posts can be deleted successfully!*

#### 6. Add Create link in the navbar (`if user.is_authenticated`), and Update & Delete buttons in the dedicated post page (`if user == post.author`).


### 11. [Python Django Tutorial: Full-Featured Web App Part 11 - Pagination](https://www.youtube.com/watch?v=acOktTcTVEQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=11&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how to use pagination so that we aren't pulling down too many posts at once. We will also learn how to create a page for posts created by a specific user. Let's get started...

#### 1. First, running an automation [script](Resources/Creating%20Sample%20Posts/code.py), which will create some sample posts (so that we can see pagination better).

#### 2. [See](Resources/Paginator) the `Paginator` object.

#### 3. Just by adding attribute `paginate_by` in our `PostListView`, pagination will be activated on our website.
- ```py
  paginate_by = x
  ```
  where `x` = no. of posts to show on a single page
- *And now max `x` posts will be visible on a single page, and other can be viewed on `?page=2` and so on.*

#### 4. Like before (read comment of [#7.1](#1-using-djangos-builtin-login--logout-class-based-views-loginview-logoutview)), we only need to add template-part of pagination, i.e., links to go to other pages.
- *Implemented my own logic of links to what pages should be shown.*

#### 5. Dedicated page which lists all the posts done by a particular user.
- *This page will be the same as the home page, the only difference is this page will only list the posts by a particular user. Still Corey created a whole new view & template, which is very bad, so I did it the way it should've done.*
1. Created view `UserPostListView` inheriting `PostListView` (overridden `get_queryset` in order to get only posts by a particular author).
2. Added url route, and added links to this page in templates.


### 12. [Python Django Tutorial: Full-Featured Web App Part 12 - Email and Password Reset](https://www.youtube.com/watch?v=-tyBEsHSv7w&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=12&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how we can use email to send a password reset link to a user so that the user can reset their password. Users will be able to fill out a form with their email and have a unique token sent to them, and if their token is verified then they will be able to create a new password. Let's get started...

*We'll be using the same builtin class-based views from `auth_views`, like we did for login, logout.*
<br>
*Note: The names of these class views are pretty stupid (I wonder which stupid wrote them.), take care while using them.*
<br>
**Note: Pattern names for routes containing these views need to be exactly what django expects them to be.**

#### 1. Page which will input the email to send the pass reset link on: Added `PasswordResetView` in `urls.py`, and created a template (`pass_reset.html`) extending `form_base.html`.

#### 2. Page which will input the new pass: Added `PasswordResetConfirmView` in `urls.py`, and created a template (`reset_link.html`) extending `form_base.html`.
1. This is the most imp. view, which will send the reset link. Reset link needs to accept two vars:
   1. `uidb64`: **u**ser **id** encoded in **b**ase **64**
   2. `token`: unique identifier ([read more](https://chat.openai.com/chat/0788ae70-f467-4e47-83a4-6b192e556634))
2. Then, setup mail ([see](https://www.youtube.com/watch?v=-tyBEsHSv7w&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=12&ab_channel=CoreySchafer&t=658) till 15:22):
   1. Created a [Google App Password](https://myaccount.google.com/apppasswords) for our Django Blog.
   2. Added mail setup settings in `settings.py`, and mail id (from which mail will be sent) & pass (we generated above) using environment vars.
- *Done! Now, our Django Blog can send mails.*

#### 3. Page which will output that the reset link has been sent: Added `PasswordResetDoneView` in `urls.py`, and created a template (`reset_link_sent.html`).

#### 4. Page which will output that the reset is successful: Added `PasswordResetCompleteView` in `urls.py`, and created a template (`reset_success.html`).

#### 5. Added "Forgot Password" link in `form_base.html` on condition if on login page.


## Additions I've Done (Major Ones)

- Added a [REST](https://en.wikipedia.org/wiki/Representational_state_transfer)ful public [API](https://en.wikipedia.org/wiki/Web_API) (@[/api1](http://localhost:8000/api1)) (using [Django REST framework](https://www.django-rest-framework.org)) which can be used to get posts from this website. (Tutorial (Basics): [Python Django 7 Hour Course/Django REST Framework](https://youtu.be/PtQiiknWUcI?t=21180))

- Gave the website [my own look](#Screenshots) (using [Bootstrap](https://getbootstrap.com/docs)), didn't copy [Corey's frontend](Screenshots/00.%20Corey's.png). (mainly Header-Navbar, Footer, and Post)

- Didn't create new view and template for the page containing only the posts by a particular user and for the dedicated post page, but inherited the view from `PostListView`, and used the `home.html` template only.

- Set to delete the old profile pic whenever a new one is added, and save the profile pics with name = 'user_id.ext'.

- Limit the post-content (on post-list pages) to show only 5 lines, and add a "Read the full article" link below if the post-content overflows the limit (using [Vanilla JavaScript](https://en.wikipedia.org/wiki/JavaScript#cite_ref-44)).

- If the uploaded profile pic is not square, it will be cropped to square (using [Pillow (PIL Fork)](https://pillow.readthedocs.io)).

- Implemented my own logic of links to what pages should be shown for pagination.


## TODOs

- Display time in local time zone.

   `localtime` template filter (https://docs.djangoproject.com/en/4.1/topics/i18n/timezones/#template-filters) is not working for me.
   I have googled the problem, read stackoverflow answers, and gone through some django doc, everything looks right to me, but localtime doesn't have any effect.
   In `settings.py`, I have `TIME_ZONE = 'UTC'` and `USE_TZ = True`, and in my html template, `{% load tz %}` and `time_posted|localtime` (`time_posted = models.DateTimeField(auto_now_add=True)`).
   But, time is not showing in my time zone (but in UTC), I've tried everything.

- Show email & username when saying link sent, show username & email when setting new pass.

- [Deploy on Heroku](https://www.youtube.com/watch?v=6DI_7Zja8Zc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=17&ab_channel=CoreySchafer)
