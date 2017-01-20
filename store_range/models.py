from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200)
    image = models.FileField(null=True, blank=True)
    description = models.CharField(max_length=1000)
    price = models.FloatField()

    def __str__(self):
        return 'Назва: ' + self.name
