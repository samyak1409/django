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
from django.contrib.auth import views as auth_views

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
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # by default these views look in 'registration/login.html', so passing template_name
]
