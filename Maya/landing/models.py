from django.db import models
from django.contrib.auth.models import User


# Create your models here.
user_preferences = [
    ('Straight', 'Straight'),
    ('Gay', 'Gay'),
    ('Lesbian', 'Lesbian'),
    ('Bisexual', 'Bisexual'),
    ('Asexual', 'Asexual'),
    ('Demisexual', 'Demisexual'),
    ('Pansexual', 'Pansexual'),
    ('Queer', 'Queer'),
    ('Questioning', 'Questioning'),
]


class ExtendedUser(models.Model):
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, blank=True)
    preferences = models.CharField(max_length=50, choices=user_preferences, blank=True)
    bio = models.TextField(blank=True)
    first_login = models.BooleanField(default=True)
    photo = models.ImageField(upload_to='profile')
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Interest(models.Model):
    hobbies = models.CharField(max_length=20)
    users = models.ManyToManyField(User, through='UsersInterest')


class UsersInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    interest = models.ForeignKey(Interest, on_delete=models.SET_NULL, blank=True, null=True)
    rating = models.FloatField()

