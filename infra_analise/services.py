import requests
import json
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()  # Carrega variáveis do .env
token = os.getenv("HF_TOKEN")  # Certifique-se de ter HF_TOKEN no seu .env  

URL = "https://router.huggingface.co/v1/chat/completions"

def analisar_com_ia(requisitos, modelo_alias):
    headers = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
    
    modelos_disponiveis = {
        "llama": "meta-llama/Llama-3.2-3B-Instruct",
        "qwen": "Qwen/Qwen2.5-72B-Instruct"
    }
    
    modelo_id = modelos_disponiveis.get(modelo_alias, modelos_disponiveis["llama"])
    
    payload = {
        "model": modelo_id,
      "messages": [
    {
        "role": "system", 
        "content": (
            "Você é um arquiteto de infraestrutura sênior. Analise e escolha entre VM ou CONTÊINER. "
            "Ao final, você DEVE obrigatoriamente escrever uma das duas opções exatamente assim: "
            "DECISÃO FINAL: VM ou DECISÃO FINAL: CONTÊINER. "
            "Não use outras variações na frase de decisão final."
        )
    },
    { "role": "user", "content": f"Requisitos: {requisitos}" }
],
        "max_tokens": 1000,
        "temperature": 0.4
    }

    try:
        response = requests.post(URL, headers=headers, json=payload, timeout=40)
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        return f"Erro na API (Status {response.status_code}): {response.text}"
    except Exception as e:
        return f"Erro local: {str(e)}"

def salvar_log(requisitos, recomendacao, modelo_alias):
    log_entry = {
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "modelo_utilizado": modelo_alias,
        "requisitos_inseridos": requisitos,
        "analise_ia": recomendacao
    }
    with open("historico_ia.json", "a", encoding="utf-8") as f:
        f.write(json.dumps(log_entry, ensure_ascii=False) + "\n")