from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import AssessmentForm


def index(request):
    if request.method == 'POST':
        # Get the submitted data and display it
        print(request.POST)
        form = AssessmentForm(request.POST)
        if form.is_valid():
            form.save(user=request.user)
            return HttpResponse(f"Success")
        else:
            print(form.errors)
            return HttpResponse(form.errors)
    else:
        return render(request, 'assessment/index.html')
