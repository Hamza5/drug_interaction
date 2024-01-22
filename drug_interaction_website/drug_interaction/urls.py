from django.urls import path
from . import views

urlpatterns = [
    #path('', views.check_drug_drug_interactions, name='interaction'),
    path('check-interactions/', views.check_drug_interactions, name='check_interactions'),
]