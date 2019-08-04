from django.db import models

class Pornstar(models.Model):
    id = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=50)
    alias = models.CharField(max_length=50)

    def __str__(self):
        return self.name
