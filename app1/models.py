from django.db import models

# Create your models here.

#https://docs.djangoproject.com/en/4.2/topics/db/models/

#this is the way to create table in sql-lite through python
class Employee(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=15)
    age = models.IntegerField()

    # this method will be useful to display the id in admin interface
    def __str__(self) -> str:
        return self.first_name +' '+ self.last_name

class Sal_details(models.Model):
    emp = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self) -> str:
        return self.emp.first_name +' '+ self.emp.last_name
    

class Signup_info(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    Password = models.IntegerField()

    def __str__(self) -> str:
        return self.name

