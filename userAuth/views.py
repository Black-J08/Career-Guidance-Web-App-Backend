from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm
from django.contrib.auth import login
# Create your views here.


def home(request):
    return redirect('/login/')


def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print("reached")
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()

    return render(request, 'registration/sign_up.html', {'form': form})
