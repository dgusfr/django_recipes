# Django Recipes

Este projeto é um site de receitas desenvolvido em Django, onde os usuários podem compartilhar e descobrir novas receitas.

<br></br>

## Sumário

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Status](#status)
- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Explicação](#explicação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Usar](#como-usar)
- [Autor](#autor)

## Sumário

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Status](#status)
- [Descrição](#descrição)
- [Funcionalidades](#funcionalidades)
- [Explicação](#explicação)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Como Usar](#como-usar)
- [Autor](#autor)

## Tecnologias Utilizadas

<div style="display: flex; flex-direction: row;">
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/python.png" alt="Logo Python" width="100"/>
  </div>
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/django.png" alt="Logo Django" width="250"/>
  </div>
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/html.png" alt="Logo HTML" width="100"/>
  </div>
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/css.png" alt="Logo CSS" width="100"/>
  </div>
  <div style="margin-right: 20px; display: flex; justify-content: flex-start;">
    <img src="img/js.png" alt="Logo JavaScript" width="100"/>
  </div>
</div>

## Status

![Concluído](http://img.shields.io/static/v1?label=STATUS&message=CONCLUIDO&color=GREEN&style=for-the-badge)

## Descrição

Este projeto é um site de receitas onde os usuários podem criar, visualizar, editar e deletar receitas. O projeto foi desenvolvido utilizando Django como framework principal e inclui funcionalidades como autenticação de usuários e interface administrativa.

## Funcionalidades

- Cadastro e autenticação de usuários
- Criação, visualização, edição e deleção de receitas
- Pesquisa de receitas por nome ou ingredientes
- Interface administrativa para gerenciamento do site

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

O trecho de código define uma função create_recipe que lida com a criação de uma nova receita no site. 

Quando a função é chamada, ela verifica se o método da solicitação HTTP é POST. Se for, ela instancia um formulário RecipeForm com os dados enviados pelo usuário. Se o formulário for válido, a nova receita é salva no banco de dados e o usuário é redirecionado para a lista de receitas (recipe_list). 

Se o método não for POST, um formulário vazio é exibido para o usuário preencher. Em ambos os casos, a função renderiza o template create_recipe.html, passando o formulário como contexto.


## Como Usar

Clone o repositório:

`git clone https://github.com/seu-usuario/curso-django-projeto1.git`

Crie e ative um ambiente virtual:

`python -m venv venv`

`source venv/bin/activate  # No Windows, use venv\Scripts\activate`

Instale as dependências:

`pip install -r requirements.txt`

Execute as migrações do banco de dados:

`python manage.py migrate`

Inicie o servidor de desenvolvimento:

`python manage.py runserver`


## Autor
Desenvolvido por Diego Franco