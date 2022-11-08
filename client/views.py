from django.shortcuts import render
from client.forms import RegistrationForm
from client.models import Client


# Create your views here.


def clients_list(request):
    clients = Client.objects.all()
    context = {
        'clients': clients
    }
    return render(request, 'clients.html', context)


def client_detail(request, client_id):
    client = Client.objects.get(id=client_id)
    context = {
        'client': client
    }
    return render(request, 'client_detail.html', context)


def client_register(request):
    form = RegistrationForm()

    return render(request, "client_registration.html", {"form": form})
