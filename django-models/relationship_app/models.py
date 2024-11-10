from django.db import models

# Author Model
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
