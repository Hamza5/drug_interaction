from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Interaction(models.Model):
    drug1 = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name='interactions1')
    drug2 = models.ForeignKey(Drug, on_delete=models.CASCADE, related_name='interactions2')
    reason = models.TextField(default='')

    def __str__(self):
        return f'{self.drug1} interacts with {self.drug2}'
