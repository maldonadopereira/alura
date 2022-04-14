import io

from django.shortcuts import render, redirect
import csv
from django.core.files.uploadedfile import UploadedFile

def index(request):
    return render(request, 'index.html')

def importa_transacao(request):
    if request.method == 'POST':
        if 'transacao' in request.FILES:
            transacao = request.FILES['transacao']
            print(f'Nome no Arquivo: {transacao.name}\nTamanho: {(transacao.size)/1000000} MegaBytes')
            # Lendo o arquivo csv
            arquivo = transacao.read().decode('utf-8')
            reader = csv.reader(io.StringIO(arquivo), delimiter=',', quotechar='|')

            # Iteração com Linst Comprehension
            dados = [linha for linha in reader]
            print(dados)

            return redirect('index')
        else:
            print('Você não importou nenhum arquivo!!')
            return redirect('index')