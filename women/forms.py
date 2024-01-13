from django import forms
from .models import Category, Husband


class AddPostForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        label='Заголовок',
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Имя'})
    )
    slug = forms.CharField(
        max_length=255,
        label="URL",
        widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'URL'})
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={'cols': 50, 'rows': 5, 'class': 'form-input'}),
        required=False, label="Описание"
    )
    is_published = forms.BooleanField(required=False, initial=True, label="Статус")
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
