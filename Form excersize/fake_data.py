import os
# Configure settings for project
# Need to run this before calling models from application!
os.environ.setdefault('DJANGO_SETTINGS_MODULE','mysite.settings')

import django
django.setup()

#*Faker script
from forms.models import User1s
from faker import Faker

#*asign faker to some variable and use selected countrys language
fake_data = Faker(['pl_PL','en_GB'])

#*function to create 5 fake entrys for User database
def populate(N=10):
    for entry in range(N):
        #*create fake fullname and split on white space
        #*.so it would be possible to select name and surname seperately
        fake_fullname = fake_data.name().split()
        fake_first_name = fake_fullname[0]
        fake_last_name = fake_fullname[1]
        #*fake email
        fake_email = fake_data.email()

        #*Create new entry... use data from models.py to create "key:values"...and return object so strat from[0]
        user = User1s.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]

if __name__ == '__main__':
    print("POPULATING DATABASE")
    populate(10)
    print("POPULATION COMPLETED!")
