from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Assessment
from .forms import AssessmentForm


@login_required(login_url="/login/")
def index(request):
    if request.method == 'POST':
        # Get the submitted data and display it
        # print(request.POST)
        form = AssessmentForm(request.POST)
        if form.is_valid():
            assessment = form.save(user=request.user)
            uuid = assessment.uuid
            url = reverse('result')+"?uuid="+str(uuid)
            return JsonResponse(status=302, data={'url': url})
        else:
            print(form.errors)
            return HttpResponse(form.errors)
    else:
        return render(request, 'assessment/index.html')


@login_required(login_url="/login/")
def result(request):
    uuid = request.GET.get("uuid")
    a = Assessment.objects.get(uuid=uuid)
    data = {
        "assessment": a.result
    }
    return render(request, 'assessment/result.html', data)


@login_required(login_url="/lohin/")
def delete_assessment(request):
    uuid = request.GET.get("uuid")
    assessment = Assessment.objects.get(uuid=uuid)
    assessment.delete()
    return redirect('dashboard')
