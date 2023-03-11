from django.shortcuts import render, reverse, redirect
from django.contrib.auth import login
from .forms import NewUserForm, ContactForm
from django.contrib import messages
from news.models import Rubric
import os
from dotenv import load_dotenv
from .tasks import send_spam_email

load_dotenv()


def index(request):
    """Main page"""
    rubrics = Rubric.objects.all()
    context = {'rubrics': rubrics, }
    return render(request, 'main/index.html', context)


def about(request):
    """Page 'About us'"""
    rubrics = Rubric.objects.all()
    context = {'rubrics': rubrics}
    return render(request, 'main/about.html', context)


def register(request):
    """Page Sign in + registration form"""
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful!")
            login(request, user)
            return redirect(reverse("index"))
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


def contacts(request):
    """
    Contacts page + settings for sending an e-mail
    """
    rubrics = Rubric.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Put here YOUR e_mail addresses:
            sender_mail = os.getenv('sender_mail')
            receiver_mail = os.getenv('receiver_mail')
            mail = send_spam_email.delay(form.cleaned_data['subject'],
                                         form.cleaned_data['content'],
                                         sender_mail,
                                         receiver_mail
                                         )
            if mail:
                messages.success(request, 'The letter has been sent successfully!')
                return redirect('contacts')
            else:
                messages.error(request, 'There is an error occurred...')
        else:
            messages.error(request, 'Validation error, incorrect input. Maybe wrong CAPTCHA?')
    else:
        form = ContactForm()
    context = {'rubrics': rubrics, "form": form}
    return render(request, 'main/contacts.html', context)


def page_not_found(request, exception):
    """Will show custom-made 404 error page (BASE_DIR/templates)"""
    # Переменная exception содержит отладочную информацию,
    # выводить её в шаблон пользовательской страницы 404 не станем
    return render(request, '404.html', {"path": request.path}, status=404)


def server_error(request):
    """Will show custom-made 505 error page (BASE_DIR/templates)"""
    return render(request, '500.html', status=500)
