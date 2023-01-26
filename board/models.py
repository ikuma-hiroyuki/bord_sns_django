from django.db import models


class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    snsimages = models.ImageField(upload_to='', null=True, blank=True)
    good = models.IntegerField(default=0)
    read = models.IntegerField(default=0)
    readtext = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
