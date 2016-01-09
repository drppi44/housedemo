# coding=utf-8
from __future__ import unicode_literals
from django.db import models


WC_CHOICES = (
    ('1', u"Совместный"),
    ('2', u"Раздельный"),
)


class Flat(models.Model):
    photo = models.ImageField(upload_to='images/photos/',
                              default='/static/images/no_image.png')
    region = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    area = models.CharField('район', max_length=100)
    address = models.CharField(max_length=200)
    level = models.PositiveIntegerField()
    max_level = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    area_total = models.PositiveIntegerField()
    area_living = models.PositiveIntegerField()
    kitchen_area = models.PositiveIntegerField()
    wc_type = models.CharField(choices=WC_CHOICES, max_length=1)
    owners_count = models.PositiveIntegerField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)

    created = models.DateTimeField(auto_now_add=True)

    @property
    def price_per_sq_m(self):
        return self.price / self.area_total


class House(models.Model):
    photo = models.ImageField(upload_to='images/photos/',
                              default='/static/images/no_image.png')
    region = models.CharField(max_length=100)
    town = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    area_total = models.PositiveIntegerField()
    levels = models.PositiveIntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=20)

    created = models.DateTimeField(auto_now_add=True)

    @property
    def price_per_sq_m(self):
        return self.price / self.area_total