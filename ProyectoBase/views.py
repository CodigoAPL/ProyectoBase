from django.http import HttpResponse
import datetime

def mensaje(request): # Esto es una vista, se llama en urls.py
    return HttpResponse("hola")

def fecha(request):

    fecha_actual = datetime.datetime.now() 

    documento = '''
        <html>
            <body>
                <h1> Fecha y hora: %s </h1>
            </body>
        </html> ''' % fecha_actual

    return HttpResponse(documento)

def calcula_edad(request, edad, año):

    #edad_presente = 20
    periodo = año - 2021 
    edad_futura = edad + periodo

    documento = '''
        <html>
            <body>
                <h22> En el año %s tendrás %s </h2>
            </body>
        </html> ''' %(año, edad_futura)
    return HttpResponse(documento)