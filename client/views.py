from django.shortcuts import render

from client.models import Client


# Create your views here.


def clients_view(request):
    clients = Client.objects.all()
    contexts = {
        'clients': clients
    }
    return render(request, 'clients.html', contexts)
