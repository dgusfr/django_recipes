# **Django Recipes**

**Django Recipes** é uma plataforma web desenvolvida em Django que permite a criação, compartilhamento e descoberta de receitas culinárias. O projeto segue princípios de arquitetura limpa para garantir a modularidade, escalabilidade e facilidade de manutenção, organizando o código em camadas bem definidas de domínio, aplicação, interface e infraestrutura.

---

## Interface

<div align="center">
  <img src="img/logo.gif" alt="Imagem do Projeto" >
</div>

## Sumário

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Status](#status)
- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Explicação](#explicação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Usar](#como-usar)
- [Autor](#autor)

<br></br>

## Tecnologias Utilizadas

<div style="display: flex; flex-direction: row;">
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/python.png" alt="Logo Python" width="150"/>
  </div>
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/django.png" alt="Logo Django" width="150"/>
  </div>
</div>

<br></br>

## Status

![Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)

<br></br>

## Descrição

Este projeto é um site de receitas onde os usuários podem criar, visualizar, editar e deletar receitas.

O projeto foi desenvolvido utilizando
Django como framework principal e inclui funcionalidades como autenticação de usuários e interface administrativa.

<br></br>

## Funcionalidades

- Cadastro e autenticação de usuários
- Criação, visualização, edição e deleção de receitas
- Pesquisa de receitas por nome ou ingredientes
- Interface administrativa para gerenciamento do site

<br></br>

## **Arquitetura do Projeto**

O projeto segue uma **Arquitetura Limpa** (Clean Architecture), separando as camadas de domínio, aplicação, interface e infraestrutura para garantir uma clara divisão de responsabilidades. Isso facilita a manutenção, testes e a escalabilidade do sistema.

### **Camadas do Projeto**

1. **Domínio**:

   - **Regras de Negócio e Entidades**: Contém as entidades principais da aplicação, como `Recipe`, `User`, e suas regras de negócio.
   - As regras de negócio são isoladas de qualquer dependência externa.

2. **Casos de Uso (Aplicação)**:

   - Define os fluxos de interação e manipulação de dados entre o domínio e as interfaces de usuário. Aqui estão os casos de uso como **criar receita**, **editar receita**, **autenticação de usuário**, etc.

3. **Interface**:

   - **Interface Web (HTML)**: Responsável por renderizar os templates HTML que serão exibidos no navegador dos usuários.
   - **APIs REST (opcional)**: Serializa os dados para JSON, permitindo a comunicação com APIs externas ou para clientes SPA (Single Page Applications).

4. **Infraestrutura**:
   - **Banco de Dados (Django ORM)**: O Django ORM (Object Relational Mapper) manipula as interações com o banco de dados, abstraindo queries SQL para facilitar o acesso aos dados.
   - **Django Framework**: Lida com o ciclo de vida de requisições HTTP, autenticação e gerenciamento de sessões.

---

## **Fluxo de Funcionamento**

O fluxo de funcionamento da aplicação foi cuidadosamente desenhado para seguir o ciclo de uso comum de uma plataforma de gerenciamento de receitas. Aqui está uma visão detalhada:

### **1. Registro e Autenticação de Usuário**

- **Fluxo**: O usuário se registra através de um formulário de inscrição que valida as credenciais e cria uma conta. Após o registro, o usuário pode fazer login com suas credenciais.
- **Detalhes**: O Django gerencia a autenticação por meio de seu sistema de login/logout, incluindo a criptografia de senhas e a gestão de sessões.

### **2. Criação de Receitas**

- **Fluxo**: O usuário autenticado pode criar novas receitas através de um formulário. Ele fornece informações como título, descrição, ingredientes e instruções.
- **Como funciona**: Quando o formulário é enviado, os dados são validados. Se estiverem corretos, uma nova instância do modelo `Recipe` é criada e salva no banco de dados.

### **3. Visualização de Receitas**

- **Fluxo**: As receitas são exibidas publicamente em uma página dedicada, permitindo que os usuários explorem e descubram receitas criadas por outros usuários.
- **Detalhes**: A visualização pode ser filtrada por ingredientes ou nome da receita, facilitando a navegação.

### **4. Edição e Exclusão de Receitas**

- **Fluxo**: Os usuários podem editar ou excluir suas próprias receitas. Eles acessam suas receitas no dashboard pessoal e fazem alterações conforme necessário.
- **Como funciona**: Ao editar, o formulário é pré-preenchido com os dados existentes da receita. Após o envio, o banco de dados é atualizado com as novas informações.

### **5. Interface Administrativa**

- **Fluxo**: Superusuários têm acesso ao painel administrativo do Django, onde podem gerenciar todos os dados da aplicação, incluindo usuários, receitas e categorias.
- **Como funciona**: Utilizando o Django Admin, os superusuários podem visualizar, editar e excluir qualquer dado do sistema.

---

## Explicação

Abaixo está um pequeno trecho de código do projeto para a criação de uma nova receita:

```python
from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm

def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/create_recipe.html', {'form': form})
```

<br></br>

O trecho de código define uma função create_recipe que lida com a criação de uma nova receita no site.

Quando a função é chamada, ela verifica se o método da solicitação HTTP é POST.

Se for, ela instancia um formulário RecipeForm com os dados enviados pelo usuário.

Se o formulário for válido, a nova receita é salva no banco de dados e o usuário é redirecionado para a lista de receitas (recipe_list).

Se o método não for POST, um formulário vazio é exibido para o usuário preencher.

Em ambos os casos, a função renderiza o template create_recipe.html, passando o formulário como contexto.

<br></br>

## Estrutura do Projeto

```
Django_Recipes/
│
├── authors/
│ ├── forms/
│ ├── migrations/
│ ├── templates/
│ ├── views/
│
├── recipes/
│ ├── models.py
│ ├── templates/
│ ├── views.py
│
├── tag/
│
├── project/
│ ├── settings.py
│ ├── urls.py
│
├── base_static/
├── base_templates/
├── manage.py
└── requirements.txt
```

## Como Usar

Clone o repositório:

`git clone https://github.com/...`

Crie e ative um ambiente virtual:

`python -m venv venv`

`source venv/bin/activate`

No Windows, use venv\Scripts\activate

Instale as dependências:

`pip install -r requirements.txt`

Execute as migrações do banco de dados:

`python manage.py migrate`

Inicie o servidor de desenvolvimento:

`python manage.py runserver`

<br></br>

## Autor

Desenvolvido por Diego Franco
