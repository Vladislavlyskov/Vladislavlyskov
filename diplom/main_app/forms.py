from .models import News
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ['title', 'anons', 'full_text', 'date']

    widgets = {
        "title": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Название'
        }),
        "anons": TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Анонс'
        }),
        "full_text": Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Текст статьи'
        }),
        "date": DateTimeInput(attrs={
            'class': 'form-control',
            'placeholder': 'Дата публикации'
        })
    }