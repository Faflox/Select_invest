from django.urls import path

from . import views

urlpatterns = [ 
    path("", views.index, name="index"),
    path("uslugi/", views.uslugi, name="uslugi"),
    path("sentFormularz/", views.sentFormularz, name="sentFormularz"),
]
