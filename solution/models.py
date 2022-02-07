from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    address = models.CharField(max_length=100, blank=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

class Branch(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.TextField(blank=False, null=False)
    host = models.ForeignKey(CustomUser, on_delete=models.CASCADE,null=False,blank=False)
    name = models.CharField(max_length=100, blank=False)
    current = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    link = models.URLField(max_length=5000, blank=False)

    def __str__(self):
        return self.name


class Member(models.Model): 
    id = models.AutoField(primary_key=True)
    voter_id = models.CharField(max_length=10, blank=False)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE,null=False,blank=False)
    token = models.IntegerField(default=0)