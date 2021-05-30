"""redcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from userss import views
from userss.forms import LoginForm
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm),name='login'),
    path('signup/',views.signup,name='signup'),
    path('all_loan/',views.all_loan,name='all_loan'),
    path('apply_loan/',views.apply_loan,name='apply_loan'),
    path('accounts/profile/',views.profile,name='profile'),
]
