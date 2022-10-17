from django.db import models

class Item(models.Model):
    name = models.CharField('Product name:', max_length=50)
    image = models.ImageField(upload_to='products/%Y-%m-%d/')
    price = models.CharField('Price:', max_length=15)
    description = models.TextField('Description:')

    def __str__(self):
        return self.name


class Letters(models.Model):
    name = models.CharField('Name:', max_length=30)
    email = models.EmailField('Email:', max_length=254)
    message = models.TextField('Message:')

    def __str__(self):
        return self.name


