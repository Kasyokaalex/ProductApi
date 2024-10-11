from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData),
    path('bulk-insert-products/', views.bulk_insert_products, name='bulk-insert-products'),
]
