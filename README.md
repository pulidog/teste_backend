# Teste Inceres

Testes basicos para mexer com Python e Django



## Como desenvolver?

1. Clone o repositorio.
2. Crie un virtualenv com python 2.7.
3. Ative o virtualenv.
4. Instale as dependencias.
5. Configure a instancia com o .env.
6. Execute os testes.

```console
git clone git@github.com/pulidog/teste_inceres.git teste
cd testes
virtualenv .teste
source .teste/bin/activate
pip install -r requirements.txt
python manage.py test
se não funcionar tentar python manage.py test --nomigrations
```

## Instruções

Cenário 1

Dado que temos um usuário,

Quando ele acessa o endereço /modulo_1/

Então ele entra na pagina modulo_1,
    e a pagina possui uma mensagem ‘Olá! Calcula o SIN de’ SIN é o SENO
    e a pagina possui um formulário,
    e o formulário possui 1 campo onde digitar o angulo para calcular o SIN,
    e o campo é ratio.
    e o formulário possui um botão calcular.
    
fa





## Como entregar?

1. Envie o código para o seu git https://github.com. 
2. Envie um mail com o link do git.
3. configure https://travis-ci.org
4. configure https://landscape.io

```console
lembre de fazer commit
tente comentar o codigo

```