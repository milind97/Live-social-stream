from django.db import models

# Create your models here.


class Url(models.Model):

    url = models.CharField(max_length=100)

    def __str__(self):
        return self.url
