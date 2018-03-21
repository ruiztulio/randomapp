from django.db import models

class UserData(models.Model):
    first_name = models.CharField(max_length=100, unique=False)
    last_name = models.CharField(max_length=100, unique=False)
    email = models.EmailField(max_length=100, unique=True)
    worker_id = models.CharField(max_length=36, unique=False)
