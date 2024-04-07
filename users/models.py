from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

class Client(User):
    phone_number = models.CharField(max_length=20)

class Agent(User):
    company_name = models.CharField(max_length=100)
