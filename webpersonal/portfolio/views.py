from django.shortcuts import render
from .models import Project


# Vista Portfolio
def portfolio(request):
    projects=Project.objects.all()
    return render(request, 'portfolio/portfolio.html', {'projects': projects})