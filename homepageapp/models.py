from django.db import models

class PostModel(models.Model):

    title = models.CharField(max_length = 100)
    dateOfPost = models.DateField()
    description = models.CharField(max_length = 1000)
