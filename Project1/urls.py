"""
URL configuration for Project1 project.

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



 # This is 1st method
'''
from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('', views.func, name = "func"),
    path('admin/', admin.site.urls),
]

'''
#2nd method - we will put what are the urls needed in the app1 itself
# and then include that urls.py path here

from django.contrib import admin
from django.urls import path, include
from app1 import views

urlpatterns = [
    path('', include("app1.urls")),
    path('admin/', admin.site.urls),
]

 