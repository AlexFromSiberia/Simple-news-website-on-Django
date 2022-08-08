from django.shortcuts import render, reverse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import NewUserForm
from django.contrib import messages
from news.models import Rubric


def index(request):
    rubrics = Rubric.objects.all()
    context = {'rubrics': rubrics}
    return render(request, 'main/index.html', context)


def about(request):
    return render(request, 'main/about.html')


def contacts(request):
    context = {'something': 'some_what'}
    return render(request, 'main/contacts.html', context)


def success(request):
    return render(request, 'registration/success.html')


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect(reverse("success"))
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})





