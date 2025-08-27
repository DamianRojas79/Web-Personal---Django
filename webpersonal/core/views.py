from django.shortcuts import render


# Create your views here.
def contact(request):
    return render(request, 'core/contact.html')


# Create your views here.
def about(request):
    return render(request, 'core/about.html')

