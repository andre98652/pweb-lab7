from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    send_mail('Hola esto es una prueba',
              'Hola esto es una mensaje automatico.',
              'chullachaqui875410@hotmail.com',
              ['woyaxa6596@nasskar.com'],
              fail_silently=False)
    return render(request, 'send/index.html')