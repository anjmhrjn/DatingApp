from django.db import models


# Create your models here.
class Interest(models.Model):
    interest = models.CharField(max_length=70)

    def __str__(self):
        return self.interest


class UserDetails(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    gender = models.CharField(max_length=20, blank=True)
    preferences = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)
    interest = models.ManyToManyField(Interest, through='UsersInterest')

    def __str__(self):
        return self.username


class UsersInterest(models.Model):
    user = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    interest = models.ForeignKey(Interest, on_delete=models.CASCADE)
    rating = models.FloatField()


class Photo(models.Model):
    photo = models.ImageField(upload_to='profile')
    userId = models.ForeignKey(UserDetails, on_delete=models.CASCADE)


