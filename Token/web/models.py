from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Tokens(models.Model):
    char = models.CharField(max_length=255)
    amount = models.BigIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)