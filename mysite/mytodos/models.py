from django.db import models

# Create your models here.
class todo(models.Model):
    todo = models.CharField(max_length=1000)

    def __str__(self):
        return self.todo