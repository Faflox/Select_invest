from django.shortcuts import render
from django.contrib import messages
from webpage.models import Formularz

# Create your views here.
def index(request):
    return render(request, 'index.html')

def uslugi(request):
    return render(request, 'uslugi.html')

def rodo(request):
    return render(request, 'rodo.html')

def kontakt(request):
    return render(request, 'kontakt.html')

def sentFormularz(request):
    if request.method == 'POST':
        name = request.POST['imie']
        email = request.POST.get('email')
        phone = request.POST.get('telefon')
        dodatkowe = request.POST.get('dodatkowe')
        
        formularz = Formularz(
            name=name, 
            email=email, 
            phone=phone, 
            dodatkowe=dodatkowe)
        formularz.save()
        
        messages.success(request, 'Formularz wysłany. Niedługo skontaktujemy się z Toba.')
        return render(request, 'index.html')
    return render(request, 'index.html')