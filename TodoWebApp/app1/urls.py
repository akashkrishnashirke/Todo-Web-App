"""TodoWebApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from app1 import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('all_tasks/admin/', admin.site.urls),
    path('PendingStatus/admin/', admin.site.urls),
    path('CompleteStatus/admin/', admin.site.urls),
    path('SearchTask/admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',views.HomePage),
    path('all_tasks/',views.all_tasks_view),
    path('logout/', views.signuot),
    path('add_task/', views.add_task),
    path('signup/', views.SignUp),
    path('accounts/login/signup/', views.SignUp),
    path('all_tasks/delete/<id>',views.DeleteData),
    path('SearchTask/delete/<id>',views.DeleteData),
    path('UpdateData/<id>',views.UpdateData),
    path('CompleteStatus/',views.CompleteStatus),
    path('PendingStatus/',views.PendingStatus),
    path('SearchTask/',views.SearchTask),
]
