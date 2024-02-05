from django.db import models
from django.urls import reverse


class Drug(models.Model):
    name = models.CharField(max_length=255)
    atc_codes = models.ManyToManyField('ATCCode', related_name='drugs')
    product_names = models.ManyToManyField('ProductName', related_name='drugs')

    def get_absolute_url(self):
        return reverse('drug_update', args=[str(self.id)])

    def __str__(self):
        return self.name


class ATCCode(models.Model):
    code = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('atc_code_update', args=[str(self.id)])

    def __str__(self):
        return self.code


class ProductName(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('product_detail', args=[str(self.id)])

    def __str__(self):
        return self.name
