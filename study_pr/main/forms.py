from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    """Form for sending an e_mail to the site admin (Page: Contacts)"""
    subject = forms.CharField(label='Topic', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Full text', widget=forms.Textarea(attrs={'class': 'form-control', "rows": 5}))
    captcha = CaptchaField()


class NewUserForm(UserCreationForm):
    """Registration form (page: Sign in)"""
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


