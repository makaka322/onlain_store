from catalog.models import Product, Category


def get_products_by_category(category_id):

    try:
        category = Category.objects.get(id=category_id)
        products = category.products.all()
        return products
    except Category.DoesNotExist:
        return []
