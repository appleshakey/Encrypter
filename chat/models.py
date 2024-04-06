from django.db import models

# Create your models here.
class chatMsg(models.Model):
    sender = models.CharField(max_length = 100)
    message = models.CharField(primary_key=True, max_length = 100)