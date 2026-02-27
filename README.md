# INFRA.AI

O **INFRA.AI** é uma aplicação web baseada em Django, projetada para auxiliar na tomada de decisões de infraestrutura. Utilizando modelos de linguagem de grande escala (LLMs) da Hugging Face, ele analisa os requisitos de projeto fornecidos pelo usuário e oferece uma recomendação técnica sobre o uso de Máquinas Virtuais (VM) ou Contêineres.

Esta ferramenta é destinada a desenvolvedores, arquitetos de sistemas e estudantes que buscam uma "segunda opinião" baseada em IA para escolhas de infraestrutura, a partir de um resumo descritivo das necessidades do projeto.

## 🚀 Funcionalidades

* **Recomendações via IA:** Obtenha conselhos de nível especialista para escolher entre VMs e contêineres apenas descrevendo os requisitos do seu projeto.
* **Suporte a Múltiplos Modelos:** Utiliza diferentes modelos de IA, incluindo Llama 3.2 (padrão) e Qwen 2.5 (para análise profunda), permitindo perspectivas variadas.
* **Dashboard Interativo:** Um painel visual exibe estatísticas sobre recomendações passadas (VMs vs. Contêineres), fornecendo insights sobre tendências de uso.
* **Histórico de Análises:** Mantém um log detalhado de todas as análises, incluindo os requisitos inseridos, o modelo utilizado e a resposta completa gerada pela IA.
* **Exportação para PDF:** Exporte a análise técnica detalhada para um documento PDF para fins de relatório e documentação.
* **Modo Claro/Escuro:** Interface amigável com alternância de tema para uma visualização confortável.

## ⚙️ Como Funciona

A aplicação oferece uma interface web simples onde o usuário pode inserir os requisitos de infraestrutura do seu projeto.

1.  O usuário descreve as necessidades e seleciona um modelo de IA (Llama ou Qwen).
2.  O backend em Django recebe a requisição e encaminha os requisitos para a API da Hugging Face, instruindo o modelo a agir como um "arquiteto de infraestrutura sênior".
3.  O modelo analisa o texto e fornece uma recomendação detalhada, concluindo com uma escolha definitiva: `DECISÃO FINAL: VM` ou `DECISÃO FINAL: CONTÊINER`.
4.  A resposta é exibida ao usuário na página web.
5.  Cada análise é registrada automaticamente em um arquivo local `historico_ia.json`.
6.  A rota `/dashboard` lê este arquivo JSON para renderizar as estatísticas e o histórico abrangente de todas as consultas anteriores.

## 🛠️ Primeiros Passos

Siga estas instruções para configurar uma cópia local do projeto.

### Pré-requisitos

* Python 3.x
* Uma conta no Hugging Face e um Token de API

### Instalação

1.  **Clonar o repositório:**
    ```sh
    git clone [https://github.com/spellmanking/infra_ai.git](https://github.com/spellmanking/infra_ai.git)
    cd infra_ai
    ```

2.  **Configurar um ambiente virtual:**
    ```sh
    # Para macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    venv\Scripts\activate
    ```

3.  **Instalar as dependências:**
    ```sh
    pip install django requests python-dotenv
    ```

4.  **Configurar variáveis de ambiente:**
    * Crie um arquivo chamado `.env` no diretório raiz do projeto.
    * Adicione seu token de API da Hugging Face neste arquivo:
        ```env
        HF_TOKEN="seu_token_de_api_da_huggingface"
        ```

5.  **Executar a aplicação:**
    O utilitário `manage.py` está localizado dentro do diretório `management`. Execute o servidor a partir da raiz do projeto:
    ```sh
    python management/manage.py runserver
    ```
    A aplicação estará disponível em `http://127.0.0.1:8000`.

## 📖 Como Usar

1.  Acesse a página inicial em `http://127.0.0.1:8000/`.
2.  Na área de texto **"REQUISITOS DO PROJETO"**, descreva as necessidades técnicas da sua aplicação (ex: *"Preciso implantar um microsserviço de baixa latência que precisa escalar horizontalmente de forma muito rápida"*).
3.  Selecione um motor de IA no menu suspenso.
4.  Clique no botão **"Analisar Arquitetura"**.
5.  A recomendação técnica da IA aparecerá no lado direito da tela. Você pode usar o botão **"Exportar PDF"** para salvar esta análise.
6.  Clique no botão **"Estatísticas"** na barra de navegação para visitar o dashboard e visualizar o histórico completo.
