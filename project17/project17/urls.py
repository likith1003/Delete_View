"""
URL configuration for project17 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('School_list_fbv', School_list_fbv, name='School_list_fbv'),
    path('School_list', School_list.as_view(), name='School_List_cbv'),
    path('Insert_School', insert_school.as_view(), name='insert_school'), 
    path('update<pk>', updateschool.as_view(), name='updateschool'),
    path('delete<pk>', SchoolDelete.as_view(), name='SchoolDelete'),
    path("display<pk>", displayschool.as_view(), name='displayschool')  
]
