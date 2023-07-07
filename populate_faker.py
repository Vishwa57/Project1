import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Project1.settings')


import django
# Import settings
django.setup()

import random
from app1.models import Employee, Sal_details
from faker import Faker

fakegen = Faker()


def populate(N=5): #default 5 but we can pass any number here

    for entry in range(N):

        # create random ids
        new_id = random.randint(1000,9999)

        # create rest values for employees
        new_fname = fakegen.name()
        new_lname = fakegen.name()
        new_mail = fakegen.email()
        new_age = random.randint(10,99)
        new_pwd = fakegen.phone_number()
        new_sal = random.randint(10000,99999)

        emp_new, _ = Employee.objects.get_or_create(id=new_id, first_name = new_fname, last_name = new_lname, email = new_mail, password = new_pwd, age = new_age)

        sal, _ = Sal_details.objects.get_or_create(emp = emp_new, salary = new_sal)


if __name__ == '__main__':
    print("Populating the databases...Please Wait")
    populate(60)
    print('Populating Complete')