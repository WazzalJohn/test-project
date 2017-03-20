import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## Fake population scripts
import random
from first_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):

        #create the fake data for the entry
        fname = fakegen.first_name()
        lname = fakegen.last_name()
        useremail = fakegen.free_email()
        userpwd = fakegen.password()

        #create the new user entry
        webpg = User.objects.get_or_create(firstname=fname, lastname=lname, email=useremail, password=userpwd)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populate complete")
