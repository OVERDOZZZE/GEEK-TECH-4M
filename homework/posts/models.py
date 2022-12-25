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
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title


class Reviews(models.Model):
    post = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, related_name='reviews')
    text = models.TextField()
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text


class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

