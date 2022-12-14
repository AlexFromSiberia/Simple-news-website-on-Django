from django.forms import ModelForm
from .models import NewsArticles
from django.forms.widgets import TextInput, Textarea, Select, ClearableFileInput
from captcha.fields import CaptchaField


class AddArticleForm(ModelForm):
    """Form for creation a new article (Page: Add a news article)"""
    captcha = CaptchaField()

    class Meta:
        # we use the only model we have
        model = NewsArticles
        fields = ['title', 'rubric', 'photo', 'text']

        # widgets will define how it's going to look like
        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': "Name of the article"}),
            "text": Textarea(attrs={'class': 'form-control', 'placeholder': 'Full text'}),
            "rubric": Select(attrs={'class': 'form-control'}),
            "photo": ClearableFileInput(attrs={'class': 'form-control'}),
        }
