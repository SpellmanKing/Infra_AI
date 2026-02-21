from django.shortcuts import render, redirect
from .services import analisar_com_ia, salvar_log
import json
import os
import unicodedata

def remover_acentos(texto):
    if not texto: return ""
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                  if unicodedata.category(c) != 'Mn')

def index(request):
    resultado = None
    requisitos = ""
    modelo_selecionado = "llama"
    if request.method == "POST":
        requisitos = request.POST.get("requisitos")
        modelo_selecionado = request.POST.get("modelo")
        resultado = analisar_com_ia(requisitos, modelo_selecionado)
        salvar_log(requisitos, resultado, modelo_selecionado)
    return render(request, "index.html", {"resultado": resultado, "requisitos": requisitos, "modelo_selecionado": modelo_selecionado})

def dashboard_estatisticas(request):
    caminho = "historico_ia.json"
    if request.GET.get('limpar') == 'true':
        if os.path.exists(caminho): os.remove(caminho)
        return redirect('dashboard')

    historico = []
    total_vm = 0
    total_container = 0

    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            for linha in f:
                linha = linha.strip()
                if not linha: continue
                try:
                    item = json.loads(linha)
                    analise = remover_acentos(item.get('analise_ia', '').upper())
                    
                    # Define a decisão
                    dec = "VM"
                    if "DECISAO FINAL" in analise:
                        concl = analise.split("DECISAO FINAL")[-1]
                        if any(x in concl for x in ["CONTAINER", "CONTEINER", "DOCKER"]): dec = "CONTÊINER"
                    elif analise.count("CONTAINER") + analise.count("CONTEINER") > analise.count("VM"):
                        dec = "CONTÊINER"
                    
                    item['decisao_calculada'] = dec
                    historico.append(item)
                    if dec == "CONTÊINER": total_container += 1
                    else: total_vm += 1
                except: continue

    return render(request, "dashboard.html", {
        "historico": historico[::-1], "total_vm": total_vm, "total_container": total_container
    })