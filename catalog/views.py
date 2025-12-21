from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView,  CreateView, DeleteView, UpdateView
from django.core.cache import cache

from catalog.forms import ProductForm
from catalog.models import Product, Category
from catalog.services import get_products_by_category


class ContactView(TemplateView):
    template_name = "catalog/contacts.html"

class ProductListView(ListView):
    model = Product


    def get_queryset(self):
        queryset = cache.get('product_queryset')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('product_queryset', queryset, 60 * 10)
        return queryset

class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        if product.owner != self.request.user:
            raise PermissionDenied("Вы не можете удалять этот продукт.")
        return product


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_object(self, queryset=None):
        product = super().get_object(queryset)
        if product.owner != self.request.user:
            raise PermissionDenied("Вы не можете редактировать этот продукт.")
        return product

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

class UnpublishProductView(LoginRequiredMixin, View):

    def post(self, request, pk):
        product = get_object_or_404(Product, id=pk)

        if not request.user.has_perm("catalog.can_publish_product"):
            raise PermissionDenied("У вас нет права на публикацию продукции")

        product.is_published = True
        product.save()

        return redirect("catalog:product_detail", pk=pk)


class CategoryListViews(ListView):
    model = Category
    template_name = "category_list.html"


class CategoryProductsDetailView(DetailView):
    model = Category
    template_name = "catalog/product_category.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.object.id
        context['products_category'] = get_products_by_category(category)
        return context
