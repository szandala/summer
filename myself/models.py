from django.db import models

class Post(models.Model):
    author = models.CharField(max_length=160)
    body = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.author + ": " +self.body[:30]