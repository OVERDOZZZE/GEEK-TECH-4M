from django.db import models

# Create your models here.


class Product(models.Model):
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now_add=True)
    rate = models.FloatField()
    price = models.IntegerField()

    def __str__(self):
        return self.title