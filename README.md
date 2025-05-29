# Django Blog

[![Live Site](https://img.shields.io/badge/Live_Site-🚀_Click_Here-brightgreen?style=for-the-badge)](https://samyak1409-django-blog.onrender.com)
<img src="https://img.shields.io/badge/Python-gray?style=for-the-badge&logo=python&logoColor=white&labelColor=3776AB" alt="Python">
<img src="https://img.shields.io/badge/Django-gray?style=for-the-badge&logo=django&logoColor=white&labelColor=092E20" alt="Django">
<img src="https://forthebadge.com/images/badges/built-with-love.svg" height=28 alt="Made with ❤️">

✅ Developed a full-stack blog website using Django, with user registration, authentication, profile customization, [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) operations on posts, email-based password reset, and auto square-cropping of profile images.

✅ Designed a responsive, minimalistic [OLED-black](https://en.wikipedia.org/wiki/OLED#Advantages:~:text=High%20dynamic%20range%20support) UI using HTML, CSS, and Bootstrap, with additional features like custom [pagination](https://en.wikipedia.org/wiki/Pagination#In_web_browsers) logic and dynamic content truncation for enhanced UX.

✅ Added a public [REST](https://en.wikipedia.org/wiki/REST)ful API with read-only access to blog posts, using Django REST framework.

✅ Followed [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself) principle to cut redundancy and boost maintainability by [inheriting](https://en.wikipedia.org/wiki/Inheritance_(object-oriented_programming)) from [class-based views](https://docs.djangoproject.com/en/stable/topics/class-based-views) and [templates](https://docs.djangoproject.com/en/stable/topics/templates).

> ⚡ **Live Site**: [samyak1409-django-blog.onrender.com](https://samyak1409-django-blog.onrender.com)



## 📸 Screenshots

### 🏠 Homepage
Browse recent blog posts and navigate easily via the header.
![](Project%20Screenshots/01.%20Home1.png)
![](Project%20Screenshots/02.%20Home2.png)

### 📝 Read Full Posts
Clicking a post opens the detailed view.
![](Project%20Screenshots/03.%20PostRead.png)

### 🧑‍💻 User Registration
New users can sign up with a simple registration form.
![](Project%20Screenshots/04.%20Register.png)

### 🔐 User Login
Registered users can securely log in.
![](Project%20Screenshots/05.%20Login.png)

### 🔄 Dynamic Navigation
Navbar updates based on user login status.
![](Project%20Screenshots/06.%20Home3.png)

### 👤 Profile Page
Users can update profile info, view their posts and log out.
![](Project%20Screenshots/07.%20Profile.png)

### ➕ Create New Posts
Authenticated users can create new posts.
![](Project%20Screenshots/08.%20PostCreate.png)

### ✏️ Edit or Delete Posts
Users can update or delete only their own posts.
![](Project%20Screenshots/09.%20PostUpdateDelete.png)

### 👀 View Posts by User
Browse posts written by a specific user.
![](Project%20Screenshots/10.%20UserPosts.png)

### 🔁 Forgot Password?
Users can request a password reset link via email.
![](Project%20Screenshots/11.%20PassReset.png)

### 🌐 RESTful Public API  
A REST API is available at [/api1](https://samyak1409-django-blog.onrender.com/api1).
![](Project%20Screenshots/12.%20RESTful%20API.png)

<details>
<summary>Click here to view individual endpoints</summary>

- **All Posts**
  ![](Project%20Screenshots/12.a.%20All%20Posts.png)

- **Single Post**
  ![](Project%20Screenshots/12.b.%20Single%20Post.png)

- **Posts by a User**
  ![](Project%20Screenshots/12.c.%20Posts%20by%20a%20User.png)

</details>



## Additions I've Made (Major Ones)

- Added a [REST](https://en.wikipedia.org/wiki/REST)ful public [API](https://en.wikipedia.org/wiki/Web_API) (@[/api1](https://samyak1409-django-blog.onrender.com/api1)) using the [Django REST framework](https://www.django-rest-framework.org), which can be used to fetch posts from this website. (Tutorial (Basics): [Python Django 7 Hour Course/Django REST Framework](https://youtu.be/PtQiiknWUcI?t=21180))

- Gave the website [my own look](#Screenshots) using [Bootstrap](https://getbootstrap.com/docs); didn't copy [Corey's template](Project%20Screenshots/00.%20Corey's.png).

- Didn't create a new view and template for the page containing only the posts by a particular user or for the dedicated post page, but instead inherited the view from `PostListView` and used the `home.html` template only.

- Set it to delete the old profile pic whenever a new one is uploaded, and save profile pics with the name format: `user_id.ext`.

- Limited the post-content (on post-list pages) to show only 5 lines, and added a "Read the full article" link below if the post-content exceeds the limit (using [Vanilla JavaScript](https://en.wikipedia.org/wiki/JavaScript#cite_ref-44)).

- If the uploaded profile pic is not square, it is cropped to a square (using [Pillow (PIL Fork)](https://pillow.readthedocs.io)).

- Implemented custom logic to control which pagination links should be displayed.



<!--
## TODOs

- Display time in the local time zone.

   `localtime` template filter (https://docs.djangoproject.com/en/4.1/topics/i18n/timezones/#template-filters) is not working for me.
   I have googled the problem, read stackoverflow answers, and gone through some django doc, everything looks right to me, but localtime doesn't have any effect.
   In `settings.py`, I have `TIME_ZONE = 'UTC'` and `USE_TZ = True`, and in my HTML template, `{% load tz %}` and `time_posted|localtime` (`time_posted = models.DateTimeField(auto_now_add=True)`).
   But, time is not showing in my time zone (but in UTC), I've tried everything.

- Show email & username when saying link sent, show username & email when setting new pass.
-->



## Run Locally

<details>
<summary>Click here to expand</summary> <br>

> ⚠️ Make sure [Python](https://www.python.org/downloads) is installed on your system.

1. **Download the Project**

   [Click here](https://github.com/samyak1409/django/archive/refs/heads/main.zip) to download the zip file.

2. **Extract the Archive**

   Unzip the downloaded file (`django-main.zip`), and navigate into the extracted `django-main` directory.

3. **Set Up Environment Variables**

   - 🔐 **SECRET_KEY**:

     Django requires a secret key. You can generate one using the following Python code:
     ```python
     import secrets
     print(secrets.token_urlsafe(50))
     ```
     Add it as an environment variable:
     ```
     SECRET_KEY=your_generated_secret_key
     ```

   - ✉️ **Email Setup (Optional)**:

     To enable [Password Reset](#users-can-request-password-reset-link-to-their-email-if-they-cant-remember-the-password) functionality:

     1. Generate a [Google App Password](https://myaccount.google.com/apppasswords).
     2. Set the following environment variables:
        ```
        EMAIL_USER=your_email@gmail.com
        EMAIL_PASS=your_app_password
        ```
     > [More Details](#12-python-django-tutorial-full-featured-web-app-part-12---email-and-password-reset)

4. **Run the App**

   Open your [Command Line Interface](https://en.wikipedia.org/wiki/Command-line_interface) (e.g., Terminal, Command Prompt), and run:

   ```bash
   cd django_project
   pip install -r requirements.txt
   python manage.py runserver
   ```

   This will install all dependencies and start the Django development server.

5. **Open the Web App**

   Visit [127.0.0.1:8000](http://127.0.0.1:8000) in your browser to view your site running locally! 🎉

</details>



---



Official Site: [djangoproject.com](https://www.djangoproject.com)

Learnt from: [Corey Schafer](https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p) (~10hr)

## Video-wise Notes in a Nutshell

<details>
<summary>Click here to expand</summary>


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
- *Note: Corey added a lot of HTML & CSS for custom structuring & styling, but didn't walk through those snippets as this is a backend course, not frontend (or fullstack), so I did not copy-paste those snippets, but pulled up minimal snippets from Bootstrap, so now I know what the markup means + a nice minimal look to the website is not bad for someone who's starting out!*

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

#### 1. Create the database for our project which contains default tables to work with using the following commands:
1. Make migrations for database changes (basically generate some data from our created/updated model(s), which will be used for generating SQL, which will in turn make changes to the database):
   ```bash
   python manage.py makemigrations
   ```
   *Note: If you want to see the SQL query that's going to be run when we apply the migrations, run:*
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
  *Now, we can access the [admin page](http://127.0.0.1:8000/admin), and modify any data directly from there.*


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
  See the queries in [`Misc Resources/DB Queries/1. Post`](Misc%20Resources/DB%20Queries/1.%20Post) folder.

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
- *This is kind of similar to the database models in the sense, that we can create Python classes, and these classes generate HTML forms for us.*

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

#### 2. Changing where the media is saved and from what url it can be accessed by adding the `MEDIA_ROOT` & `MEDIA_URL` respectively in `settings.py`.
- *By default, `MEDIA_ROOT` is the base dir of our project, so if different models started making different dirs at the base dir, then it will be cluttered up.*

#### 3. [Querying](Misc%20Resources/DB%20Queries/2.%20Profile) the `Profile` model using `User` model (as they're connected/linked by `OneToOneField`).
1. But no profiles exist currently, so, first add a few from the admin page (as we've not implemented "when the user is created, profile is created with it" yet).

#### 4. Now, the main part, Showing profile pic on the profile page.
1. Update the profile template `profile.html`, with the user profile pic url (`user.profile.pic.url`).
2. Adding `MEDIA_URL` to `urlpatterns`. ([Serving files uploaded by a user during development](https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development)) ([see](https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8&ab_channel=CoreySchafer&t=1258) till 24:33)
   - *Now, we can see the profile pic on the profile page.*
3. Adding [Corey's styles](https://github.com/CoreyMSchafer/code_snippets/blob/master/Django_Blog/snippets/main.css) (to the `static` dir) so that profile page looks right.
4. Adding the default profile pic. (Remember? Check [`Profile`](django_project/users/models.py))

*- x - Till [26:18](https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8&ab_channel=CoreySchafer&t=1578) - x -*

#### 5. Using Signals: Set to auto-create the Profile (with the default profile pic) whenever a new user is created.
- *Till now, we were adding the pic from the admin page only.*
- **But, why are we doing all this? Wouldn't an image (profile pic) input field in the `RegistrationForm` itself be a way better method!?**


### 9. [Python Django Tutorial: Full-Featured Web App Part 9 - Update User Profile](https://www.youtube.com/watch?v=CQ90L5jfldw&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=9&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be finishing our user profile page. The final page will allow users to update their information and also add a new profile picture. We will also learn how to resize this image when it is uploaded to save space on our web server. Let's get started...

#### 1. For giving the option of updating username, email, and profile pic:
1. Creating two update forms (extending `forms.ModelForm`) in `forms.py`. (for `User` & `Profile` model)
2. Add the forms in `profile` view and pass to the template through `context`.
3. Update template with the two forms in the `form` HTML tag.
   1. Don't forget to add `enctype="multipart/form-data"` in `form`. (for passing image data properly)
4. Update the `profile` view to handle the POST request. (same as [#6.4](#4-submitting-form-using-post-request-validating-form-creating-account-saving-the-data-to-the-db-and-displaying-flash-messages))

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
- *Corey didn't follow DRY, and created this view not inheriting from `PostListView` and a new template, which is not good, so I did it the way it should've been done.*
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
2. Created `post_confirm_delete.html`. (It will be just a confirmation form, where the submit button will lead to post deletion.)
3. Set `success_url` in view. (Url to redirect on after deleting the post.)
- *Now, posts can be deleted successfully!*

#### 6. Add Create link in the navbar (`if user.is_authenticated`), and Update & Delete buttons in the dedicated post page (`if user == post.author`).


### 11. [Python Django Tutorial: Full-Featured Web App Part 11 - Pagination](https://www.youtube.com/watch?v=acOktTcTVEQ&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=11&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how to use pagination so that we aren't pulling down too many posts at once. We will also learn how to create a page for posts created by a specific user. Let's get started...

#### 1. First, running an automation [script](Misc%20Resources/Creating%20Sample%20Posts/code.py), which will create some sample posts (so that we can see pagination better).

#### 2. [See](Misc%20Resources/Paginator) the `Paginator` object.

#### 3. Just by adding attribute `paginate_by` in our `PostListView`, pagination will be activated on our website.
- ```py
  paginate_by = x
  ```
  where `x` = no. of posts to show on a single page
- *And now max `x` posts will be visible on a single page, and other can be viewed on `?page=2` and so on.*

#### 4. Like before (read comment of [#7.1](#1-using-djangos-builtin-login--logout-class-based-views-loginview-logoutview)), we only need to add template-part of pagination, i.e., links to go to other pages.
- *Implemented my own logic of links to what pages should be shown.*

#### 5. Dedicated page which lists all the posts done by a particular user.
- *This page will be the same as the home page, the only difference is this page will only list the posts by a particular user. Still Corey created a whole new view & template, which is terrible, so I did it the way it should've been done.*
1. Created view `UserPostListView` inheriting `PostListView` (overridden `get_queryset` in order to get only posts by a particular author).
2. Added url route, and added links to this page in templates.


### 12. [Python Django Tutorial: Full-Featured Web App Part 12 - Email and Password Reset](https://www.youtube.com/watch?v=-tyBEsHSv7w&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=12&ab_channel=CoreySchafer)

> In this Python Django Tutorial, we will be learning how we can use email to send a password reset link to a user so that the user can reset their password. Users will be able to fill out a form with their email and have a unique token sent to them, and if their token is verified, then they will be able to create a new password. Let's get started...

*We'll be using the same builtin class-based views from `auth_views`, like we did for login, logout.*
<br>
*Note: The names of these class views are pretty stupid (I wonder who wrote them.), take care while using them.*
<br>
**Note: Pattern names for routes containing these views need to be exactly what django expects them to be.**

#### 1. Page which will input the email and send the reset link to that: Added `PasswordResetView` in `urls.py`, and created a template (`pass_reset.html`) extending `form_base.html`.
- Mail Setup ([see](https://www.youtube.com/watch?v=-tyBEsHSv7w&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=12&ab_channel=CoreySchafer&t=658) till 15:22):
   1. Created a [Google App Password](https://myaccount.google.com/apppasswords) for our Django Blog.
   2. Added mail setup settings in `settings.py`, and mail id (from which mail will be sent) & pass (we generated above) using environment vars.
- *Done! Now, our Django Blog can send mails.*

#### 2. Page which will output that the reset link has been sent: Added `PasswordResetDoneView` in `urls.py`, and created a template (`reset_link_sent.html`).

#### 3. Page which will input the new pass and set it: Added `PasswordResetConfirmView` in `urls.py`, and created a template (`reset_link.html`) extending `form_base.html`.
- Reset link needs to accept two vars:
   1. `uidb64`: **u**ser **id** encoded in **b**ase **64**
   2. `token`: unique identifier ([read more](https://chat.openai.com/chat/0788ae70-f467-4e47-83a4-6b192e556634))

#### 4. Page which will output that the reset is successful: Added `PasswordResetCompleteView` in `urls.py`, and created a template (`reset_success.html`).

#### 5. Added "Forgot Password" link in `form_base.html` on condition if on login page.

</details>



## Notes: Deploying a Full-Stack Django Web App on Render

<details>
<summary>Click here to expand</summary>

### 🔧 Setup on [Render Dashboard](https://dashboard.render.com/web/new)

1. **Name**:  
   Give your Web Service a *unique* name (e.g., `samyak1409-django-blog`).  
   > ⚠️ If left blank, Render will append random characters to the name, which is undesirable.

2. **Root Directory**:  
   If your Django project is inside a subdirectory, provide that directory name here. It doesn’t have to be at the root of the repo.

3. **Build Command**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Command**:
   ```bash
   gunicorn project_name.wsgi
   # Example:
   gunicorn django_project.wsgi
   ```
   Ensure your `requirements.txt` includes:
   ```
   gunicorn
   ```

5. **Environment Variables**:  
   Add all required variables (e.g., `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, DB creds, etc.).

### ⚠️ Problem with Free Instances on Render

> *Free instances spin down after periods of inactivity. They do not support SSH access, scaling, one-off jobs, or **PERSISTENT DISKS**. Select any paid instance type to enable these features.*  
> — [Render Docs](https://render.com)

### ✅ Solution

#### 📦 For Static Files

Your `requirements.txt` should include:
```
whitenoise
```

In `settings.py`:

```python
# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # location where collectstatic gathers all static content

# WhiteNoise Middleware for serving static files
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')  # right after SecurityMiddleware

# Compressed storage for caching and versioning
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

Run:
```bash
python manage.py collectstatic
```

**How it works**:  
WhiteNoise serves static files from the `STATIC_ROOT` folder. These files are included in the deployment slug (i.e., the Render package).  
Even if the instance restarts, static files are **not lost** because they’re embedded in the deployment, **not** stored on the ephemeral disk. ✅

#### 🖼️ For Media Files

> ⚠️ This is **not recommended** for production. It's a temporary workaround.

In `urls.py`, use:

```python
import re
from django.urls import re_path
from django.views.static import serve

urlpatterns += [
    re_path(
        r"^%s(?P<path>.*)$" % re.escape(settings.MEDIA_URL.lstrip("/")),
        serve,
        kwargs={"document_root": settings.MEDIA_ROOT},
    ),
]
```

Instead of:

```python
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Note that it will only be added in DEBUG mode (see the source code of `static`).
```

> 🔍 A free, reliable media hosting service should be integrated in the future.

#### 🗄️ For Database (SQLite on Free Tier)

- The `db.sqlite3` file from your GitHub repo is used by Render on deploy.
- Any changes made to the database on production **do not persist**.
- After ~15 minutes of inactivity, the site spins down and the DB resets to its state from the last deployment.

> 🔍 A free cloud-based database service (like Supabase, Neon, etc.) should be integrated in the future.

</details>
