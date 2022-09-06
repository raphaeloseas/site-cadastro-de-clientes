from turtle import done
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Client
from .forms import ClientForm
from django.contrib import messages
from django.core.paginator import Paginator
import datetime

# Create your views here.

@login_required
def dashboard(request):
    clients_list = Client.objects.all().order_by('-data_de_criacao').filter(user=request.user)

    cont_client = Client.objects.filter(user=request.user).count()
    cont_client_recent = Client.objects.filter(data_de_criacao__gt=datetime.datetime.now()-datetime.timedelta(days=30), user=request.user).count()

    search_nome =  request.GET.get('search_nome')
    search_id =  request.GET.get('search_id')
    search_email =  request.GET.get('search_email')

    if search_nome:
        clients = Client.objects.filter(nome__icontains=search_nome, user=request.user)
    elif search_id:
        clients = Client.objects.filter(id__icontains=search_id, user=request.user)
    elif search_email:
        clients = Client.objects.filter(email__icontains=search_email, user=request.user)

    else:    
        paginator = Paginator(clients_list, 40)
        page = request.GET.get('page')
        clients = paginator.get_page(page)

    return render (request, 'clients/clients_list.html', {'clients': clients, 'cont_client': cont_client, 'cont_client_recent': cont_client_recent})

@login_required
def clientView(request, id):
    client = get_object_or_404(Client, pk=id, user=request.user)
    return render(request, 'clients/client.html', {'client': client})

@login_required
def createClient(request):
    if request.method == 'POST':
        form =  ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.user = request.user
            #client_save = 'salvando'
            client.save()
            messages.info(request, 'Cliente cadastrado com sucesso!')
            return redirect ('/createClient/')

    else:       
        form = ClientForm
        return render(request, 'clients/client_form.html', {'form':form})
   
@login_required
def editClient(request, id):
    client = get_object_or_404(Client, pk=id, user=request.user)
    form = ClientForm(instance=client)

    if (request.method == 'POST'):
        form = ClientForm(request.POST, instance=client)
        if (form.is_valid()):
            client.save()
            messages.info(request, 'Cliente editado com sucesso!')
            return redirect('/dashboard/')
        else:
            return render(request, 'clients/client_edit.html', {'form': form, 'client': client})

    else:
        return render(request, 'clients/client_edit.html', {'form': form, 'client': client})

@login_required
def deleteClient(request, id):
    client = get_object_or_404(Client, pk=id, user=request.user) 
    client.delete()
    messages.info(request, 'Cliente deletado com sucesso!')
    return redirect('/dashboard/')