from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'

    # https://github.com/samyak1409/django#5-using-signals-set-to-auto-create-the-profile-with-the-default-profile-pic-whenever-a-new-user-is-created:
    def ready(self):
        import users.signals  # not wrong, should be done like this only, otherwise wrong, django thing
