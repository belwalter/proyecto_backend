from django.db import models

# Create your models here.

class Funko(models.Model):
    name = models.CharField(max_length=128)
    number = models.IntegerField()
    collection = models.CharField(max_length=128)
    is_backlight = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.number} - {self.name}'


class User(models.Model):
    name = models.CharField(max_length=128)
    funkos = models.ManyToManyField(Funko, blank=True)

    def __str__(self):
        return self.name