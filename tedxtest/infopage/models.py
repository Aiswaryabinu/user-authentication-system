
    

from django.db import models

class User(models.Model):
  username = models.CharField(max_length=50, unique=True)
  email = models.EmailField(max_length=254, unique=True)
  city = models.CharField(max_length=50)
  phone_number = models.CharField(max_length=20)

  def _str_(self):
    return self.username