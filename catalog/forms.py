from django.forms import ModelForm, BooleanField
from django.core.exceptions import ValidationError
from catalog.models import Product

EXCEPTION_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = "form-check-input"
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "photo_product", "price", "category"]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name.lower() in EXCEPTION_WORDS:
            raise ValidationError(f"Нельзя использовать слово {name} в названии товара. Пожалуйста, замените его")
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description')

        for word in EXCEPTION_WORDS:
            if word in description.lower():
                raise ValidationError(f"Нельзя использовать слово {word} в описании товара. Пожалуйста, замените его")
        return description


    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise ValidationError("Цена товара не может быть отрицательным числом. Пожалуйста, введите корректное значение цены")
        return price

class ProductModeratorForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ["is_published"]
