from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import product_list, contacts, product_detail

app_name = CatalogConfig.name

urlpatterns = [
    path('product_list/', product_list),
    path('contacts/', contacts, name='contacts'),
    path('product_detail/<int:id>', product_detail, name='product_detail'),
]
