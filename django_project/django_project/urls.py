"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path, include
from users import views as users_views  # but it's a Django convention, & it works, see example 1 above in documentation
from django.contrib.auth.views import LoginView, LogoutView, \
    PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    # Including another URLconf:
    path('', include('blog.urls')),
    # note that: django will only send the remaining part of the url to the `include`
    # e.g. if we went to "blog/", if the whole string matched here, only empty string will be sent further

    # Function views:
    path('register/', users_views.register, name='register'),
    path('profile/', users_views.profile, name='profile'),

    # Class-based views:
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # by default these views look in 'registration/login.html', so passing template_name

    # Note: For following views (password reset views), `name` can't be custom, but exactly what django expects them to
    # be.

    path('pass-reset/',
         PasswordResetView.as_view(template_name='users/pass_reset.html', title=None),
         name='password_reset'),

    path('pass-reset/link-sent/',
         PasswordResetDoneView.as_view(template_name='users/reset_link_sent.html', title=None),
         name='password_reset_done'),

    path('pass-reset/link/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='users/reset_link.html', title=None),
         name='password_reset_confirm'),

    path('pass-reset/success/',
         PasswordResetCompleteView.as_view(template_name='users/reset_success.html', title=None),
         name='password_reset_complete'),

    # Including APIs' URLconf:
    path('api0/', include('api0.urls')),
    path('api1/', include('api1.urls')),
]


# https://github.com/samyak1409/django#4-now-the-main-part-showing-profile-pic-on-the-profile-page:
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# Note that it will only be added in the DEBUG mode (see the source code of `static`).
# Not recommended:
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
