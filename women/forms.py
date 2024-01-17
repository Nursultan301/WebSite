import string

from django import forms
from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

from .models import Category, Husband, Women


@deconstructible
class RussianValidator:
    ALLOWED_CHARS = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯабвгдеёжзийклмнопрстуфхцчшщбыъэюя0123456789- "
    code = "russian"

    def __init__(self, message=None):
        self.message = message if message else "Должны присутствовать только русские символы, дефис и пробел"

    def __call__(self, value, *args, **kwargs):
        if not (set(value) <= set(self.ALLOWED_CHARS)):
            raise ValidationError(self.message, code=self.code)


class AddPostForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Выберите категория",
        label="Категория"
    )
    husband = forms.ModelChoiceField(
        queryset=Husband.objects.all(),
        required=False,
        empty_label="Не замужем",
        label="Муж"
    )

    class Meta:
        model = Women
        fields = ["title", "slug", "content", "photo", "is_published", "category", "husband", "tags"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-input", "placeholder": "Имя"}),
            "slug": forms.TextInput(attrs={"class": "form-input", "placeholder": "url"}),
            "content": forms.Textarea(attrs={"class": "form-input", "cols": 50, "rows": 5, "placeholder": "Имя"}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 50:
            raise ValidationError("Длина превышает 50 символов")
        return title
