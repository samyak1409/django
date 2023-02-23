from django.db import models
# from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.


# To work with these databases, Django has its own built-in ORM. Now, if you don't know what an ORM is, it stands for
# Object Relational Mapper, and basically it allows us to access our database in an easy-to-use object-oriented way, and
# the thing that I like about it the most is that you can use different databases without changing your code, so if you
# want to use an SQLite database for testing and a Postgres database for production, then all you need to do is set up a
# different database in our settings, but all the code to query the database will still be the same. And that's what
# we'll be doing in this series, we'll use an SQLite database for development and a Postgres database for production. So
# let's go ahead and get started so that we can see what this looks like. Now, the great thing about the django ORM is
# that we can represent our database structure as classes, and you'll hear those classes be called models, and doing the
# database structure this way is actually very intuitive after you get the hang of it.

# Class: Table
# Class Attributes: Table Fields


class Post(models.Model):

    # Title:
    title = models.CharField(max_length=100)

    # Content:
    content = models.TextField()

    # Date:
    # Option 1:
    '''
    date_posted = models.DateField(auto_now=True)
    '''
    # update the date posted to the current date time every time the post was updated
    # that would be great for a last modified field or something like that
    # Option 2:
    '''
    date_posted = models.DateField(default=timezone.now)
    '''
    # set the date posted to the current date time only when this object is created, updatable
    # Option 3:
    date_posted = models.DateField(auto_now_add=True)
    # set the date posted to the current date time only when this object is created
    # can't ever update the value of the date posted

    # Author:
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # `ForeignKey`: because author i.e. user is itself separate model i.e. table. (it'll be one-to-many relationship)
    # `on_delete`: what to do to this post if the user of this post is deleted.
    # `models.CASCADE`: telling django to delete the post in that case.

    # You must know what this is for: (Hint: OOP Course from Corey)
    def __str__(self):
        return self.title


# https://youtu.be/aHC3uTkT9r8?t=466
# Now to make changes to the database we've to make some migrations: `python manage.py makemigrations`
# Note: We can also see the SQL that's going to be run when we'll apply the migrations by:
#       `python manage.py sqlmigrate app_name migration_id`, e.g. `python manage.py sqlmigrate blog 0001`
# And apply them: `python manage.py migrate`


# I should also mention why migrations are so useful:
# So, migrations are useful because it allows us to make changes to our database even after it's created and has data.
# If we didn't have a way to run migrations, then we would have to run some complicated SQL code to update our database
# structure, so that it doesn't mess with the current data! But with migrations, we can simply make whatever changes we
# need, run `makemigrations` and then run `migrate`, and it will make all of those changes for us!


# python manage.py shell


# Additional thing to remember:
# Created by django automatically:
# author_id
# post_set
