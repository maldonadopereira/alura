from django.shortcuts import render, redirect
import csv

def index(request):
    return render(request, 'index.html')

def importa_transacao(request):
    if request.method == 'POST':
        if 'transacao' in request.FILES:
            transacao = request.FILES['transacao']
            print(f'Nome no Arquivo: {transacao.name}\nTamanho: {(transacao.size)/1000000} MegaBytes')
            arquivo = open(transacao)
            linhas = csv.reader(arquivo)

            for linha in linhas:
                print(linha)
            return redirect('index')
        else:
            print('Você não importou nenhum arquivo!!')
            return redirect('index')