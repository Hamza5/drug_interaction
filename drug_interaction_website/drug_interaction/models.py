from django.db import models
from django.urls import reverse

class Drug(models.Model):
    name = models.CharField(max_length=255)
    atc_codes = models.ManyToManyField('ATCCode', related_name='drugs')
    product_names = models.ManyToManyField('ProductName', related_name='drugs')

class ATCCode(models.Model):
    code = models.CharField(max_length=20)

class ProductName(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])
