import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'randomapp.settings')

import django
django.setup()


from faker import Faker
from randomapp.models import UserData
import uuid

fakengen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_email = fakengen.email()
        fake_name = fakengen.first_name()
        fake_last = fakengen.last_name()
        #worker_id = uuid.uuid4()
        worker_id = '718f7b82-7cda-4a60-a318-b15a5cf1620d'
        ud = UserData.objects.get_or_create(email=fake_email, first_name=fake_name, last_name=fake_last, worker_id=worker_id)[0]

def main():
    print('Generating random info')
    populate(20)
    print('Done')

if __name__ == '__main__':
    main()
