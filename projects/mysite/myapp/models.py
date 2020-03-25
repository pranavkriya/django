from django.db import models

# Create your models here.

class userDetails(models.Model):
    """docstring for userDetails."""

    lastName = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    birthDate = models.DateField()
    email = models.EmailField(max_length = 254)
    userName = models.CharField(max_length=15, unique=True)
    passWord = models.CharField(max_length=15)

    USERNAME_FIELD = 'userName'

    def __init__(self, arg):
        super(userDetails, self).__init__()
        self.arg = arg
