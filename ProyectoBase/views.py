from django.http import HttpResponse

def mensaje(request): # Esto es una vista, se llama en urls.py
    return HttpResponse("hola")

