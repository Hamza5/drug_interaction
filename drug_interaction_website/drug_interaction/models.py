from django.db import models

class Drug(models.Model):
    name = models.CharField(max_length=255)
    atc_codes = models.ManyToManyField('ATCCode', related_name='drugs')
    product_names = models.ManyToManyField('ProductName', related_name='drugs')

class ATCCode(models.Model):
    code = models.CharField(max_length=20)

class ProductName(models.Model):
    name = models.CharField(max_length=255)