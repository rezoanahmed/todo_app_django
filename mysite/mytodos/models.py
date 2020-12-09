from django.db import models

# Create your models here.
class todo(models.Model):
    name = models.CharField(max_length=1000)

    def ___str__(self):
        return self.name