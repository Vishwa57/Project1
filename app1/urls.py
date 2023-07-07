from django.urls import path
from . import views
 # . Since both are from the same directory

app_name = "app1"

#to use app1:name we need to provide this

urlpatterns = [
    path("", views.func, name="func"),
    path("user/", views.users, name="users"),
    path('forms/', views.Form_view, name = 'Forms'),
    path('signuppage/',views.ModelForm, name = 'Sign_up'),
    path('success/',views.sucess_page, name = 'congrats'),
    path('base/',views.base, name = 'base'),
]

# here we can give the multiple urls
