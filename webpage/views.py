from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def uslugi(request):
    return render(request, 'uslugi.html')

def formularz(request):
    return render(request, 'formularz.html')