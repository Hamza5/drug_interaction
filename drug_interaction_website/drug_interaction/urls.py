from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('check-interactions/', views.check_drug_interactions, name='check_interactions'),
    path('products/', views.ProductListCreate.as_view(), name='products'),
    path('products/<int:pk>/', views.ProductShowUpdate.as_view(), name='product_update'),
    path('atc-codes/', views.ATCCodeListCreate.as_view(), name='atc_codes'),
    path('atc-codes/<int:pk>/', views.ATCCodeShowUpdate.as_view(), name='atc_code_update'),
    path('', lambda request: redirect('check_interactions', permanent=False)),
]