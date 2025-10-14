from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ContactView, ProductDetailView, ProductCreateView, ProductDeleteView, \
    ProductUpdateView, CategoryListViews, CategoryProductsDetailView

app_name = CatalogConfig.name

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name="product_list"),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('product_detail/<int:pk>', cache_page(60*10)(ProductDetailView.as_view()), name='product_detail'),
    path("product_create/", ProductCreateView.as_view(), name="product_create"),
    path("product_delete/<int:pk>/", ProductDeleteView.as_view(), name="product_delete"),
    path("product_update/<int:pk>/", ProductUpdateView.as_view(), name="product_update"),
    path("category_list/", CategoryListViews.as_view(), name="category_list"),
    path("product_category/<int:pk>/", cache_page(60 * 10)(CategoryProductsDetailView.as_view()),
         name="product_category"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



