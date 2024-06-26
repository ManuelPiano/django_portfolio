from django.db import models
import datetime

class post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(datetime.date.today())
    image = models.ImageField(upload_to='blog/images/')
