"""
URL configuration for todotask project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from mainapp.views import * #Importing the TodoView from the mainapp.views
from rest_framework_simplejwt.views import ( #Importing the views from the rest_framework_simplejwt library to generate the tokens
    TokenObtainPairView,
)
from rest_framework_simplejwt.views import TokenVerifyView #Importing the TokenVerifyView from the rest_framework_simplejwt library to verify the token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/todo/view', Todo_fetch.as_view()),
    path('api/todo/add', Todo_add.as_view()),
    path('api/todo/update', Todo_update.as_view()),
    path('api/todo/delete', Todo_delete.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    
]
