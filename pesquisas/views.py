import csv
import io
from django.urls import reverse
from django.http import HttpResponseRedirect

from django.shortcuts import render
from pesquisas.models import Pesquisa


def save_data(data):
    '''
    Salva os dados no banco.
    '''
    aux = []
    for item in data:
        name = item.get('Name')
        address = item.get('Address')
        country = item.get('Country')
        publication_title = item.get('Publication Title')
        publication_number = item.get('Publication Number')
        year = item.get('Year')
        match = item.get('Match')
        type_organization = item.get('Type organization')
        obj = Pesquisa(
            name = name,
            address = address,
            country = country,
            publication_title = publication_title,
            publication_number = publication_number,
            year = year,
            match = match,
            type_organization = type_organization,
        )
        aux.append(obj)
    Pesquisa.objects.bulk_create(aux)

def cadastrarPesquisa(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        # Lendo arquivo InMemoryUploadedFile
        file = myfile.read().decode('utf-8')
        reader = csv.DictReader(io.StringIO(file))
        # Gerando uma list comprehension
        data = [line for line in reader]
        save_data(data)
        return HttpResponseRedirect(reverse('consultarPesquisa'))

    template_name = 'cadastrarPesquisa.html'
    return render(request, template_name)
 
def consultarPesquisa(request):
    pesquisas = Pesquisa.objects.all()
    context = {
        'pesquisas': pesquisas
    }
    return render(request, 'consultarPesquisa.html', context)

def filtrar_Pais(request):
    pesquisas = Pesquisa.objects.all()
    context = {
        'pesquisas': pesquisas
    }
    return render(request, 'filtrarPais.html', context)



