#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# [Part 1 - Getting Started](https://youtu.be/UmljXZIypDc)


# [Part 4 - Admin Page](https://youtu.be/1PkNiYlkkjo)
# To access /admin for the first time, we first have to run some commands on to the terminal:
# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser

# (Details of created superuser:
# Username: samyak1409
# Email address: samyak65400@gmail.com
# Password: testpass123)

# And with these credentials, you can log in to `/admin`.
