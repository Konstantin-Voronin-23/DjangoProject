from django.forms import ModelForm
from django import forms
from django.core.exceptions import ValidationError
from .models import Product


FORBIDDEN_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "бесплатно",
    "обман",
    "полиция",
    "радар"
]

class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput):
                field.widget.attrs.update({'class': 'checkbox-input'})
            else:
                field.widget.attrs.update({'class': 'form-control'})

class ProductForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'category', 'price']



    def clean_name(self):
        name = self.cleaned_data.get('name', '')
        lower_name = name.lower()
        for word in FORBIDDEN_WORDS:
            if word in lower_name:
                raise ValidationError(f'Поле "Наименование продукта" содержит запрещенное слово: "{word}"')
        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        lower_desc = description.lower()
        for word in FORBIDDEN_WORDS:
            if word in lower_desc:
                raise ValidationError(f'Поле "Описание продукта" содержит запрещенное слово: "{word}"')
        return description

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price is not None and price < 0:
            raise ValidationError('Цена продукта не может быть отрицательной.')
        return price

    def clean_image(self):
        image = self.cleaned_data.get('image')
        if image:
            if hasattr(image, 'content_type'):
                if image.content_type not in ['image/jpeg', 'image/png']:
                    raise ValidationError('Поддерживаются только форматы JPEG и PNG.')
                if image.size > 5 * 1024 * 1024:
                    raise ValidationError('Размер изображения не должен превышать 5 МБ.')
        return image