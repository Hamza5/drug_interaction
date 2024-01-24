from django.contrib import admin
from .models import Drug, ATCCode, ProductName

admin.site.register(Drug)
admin.site.register(ATCCode)
admin.site.register(ProductName)
