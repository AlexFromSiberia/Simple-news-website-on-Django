from django.shortcuts import render, reverse, redirect
from django.contrib.auth import login
from .forms import NewUserForm, ContactForm
from django.contrib import messages
from news.models import Rubric
from django.core.mail import send_mail


def index(request):
    rubrics = Rubric.objects.all()
    context = {'rubrics': rubrics}
    return render(request, 'main/index.html', context)


def about(request):
    rubrics = Rubric.objects.all()
    context = {'rubrics': rubrics}
    return render(request, 'main/about.html', context)


def register(request):
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
    rubrics = Rubric.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'],
                             form.cleaned_data['content'],
                             'stibo84@mail.ru',
                             ['id764g@gmail.com'],
                             fail_silently=False)
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
