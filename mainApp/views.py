from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import UserCreationForm



@csrf_protect
def login(request):
    args = {}
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect("/")
        else:
            args['login_error'] = "User not found!"
    return render(request, 'login_form.html')


@csrf_protect
def register(request):
    args = {'form': UserCreationForm}
    if request.POST:
        newuser_form = UserCreationForm(request.POST)
        if newuser_form.is_valid():
            newuser = newuser_form.save(commit=False)
            user_name = newuser_form.cleaned_data['username']
            password = newuser_form.cleaned_data['password']
            newuser.set_password(password)
            newuser_form.save()
            email = newuser_form.cleaned_data["email"]

            newuser.save()

            return HttpResponseRedirect("/")

        else:
            args['form'] = newuser_form

    return render(request, 'register_form.html')


def index(request):
    return render(request, "home_page.html")


def contact(request):
    return render(request, "contact_form.html", {"values": [
        "(063) 673-37-01",
        "Telegram",
        "GitHub"]})
