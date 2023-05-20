from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from .models import Assessment
from .forms import AssessmentForm


def result(request):
    print("reached")
    uuid = request.GET.get("uuid")
    a = Assessment.objects.get(uuid=uuid)
    data = {
        "assessment": a
    }
    return render(request, 'assessment/result.html', data)


def index(request):
    if request.method == 'POST':
        # Get the submitted data and display it
        print(request.POST)
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
