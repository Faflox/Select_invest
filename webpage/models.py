from django.db import models

# Create your models here.

class Formularz(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    dodatkowe = models.TextField(max_length=1000, blank=True, null=True)
    answered= models.BooleanField(default=False)
    
    def __str__(self):
        return self.name