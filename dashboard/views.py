from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from assessment.models import Assessment


@login_required(login_url="/login/")
def index(request):
    user_assessments = Assessment.objects.filter(user=request.user)
    context = {'user_assessments': user_assessments}
    return render(request, 'dashboard/index.html', context)
