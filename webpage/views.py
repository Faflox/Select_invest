from django.shortcuts import render
from webpage.models import Formularz

# Create your views here.
def index(request):
    return render(request, 'index.html')

def uslugi(request):
    return render(request, 'uslugi.html')


def sentFormularz(request):
    if request.method == 'POST':
        name = request.POST['imie']
        email = request.POST.get('email')
        phone = request.POST.get('telefon')
        message = request.POST.get('message')
        formularz = Formularz(
            name=name, 
            email=email, 
            phone=phone, 
            message=message)
        formularz.save()
        return render(request, 'sentFormularz.html')