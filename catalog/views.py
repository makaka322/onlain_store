from django.shortcuts import render

from catalog.models import Product


def contacts(request):
    return render(request, 'contacts.html')

def product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'product_list.html', context)


def product_detail(request, id):
    product_detail = Product.objects.get(id=id)
    context = {'product_detail': product_detail}
    return render(request, 'product_detail.html', context)
