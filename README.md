# __TechCell-Pro__
Repositório destinado ao desenvolvimento de um Sistema de Gestão de Assistência Técnica para a disciplina de Engenharia de Software II. 

## __Tecnologias__
* Django(Python)
* PostgreSQL
* Algum framework CSS

## Tutoriais

* __Django :__
<br> Link 1 -> https://www.youtube.com/watch?v=1r_5JOER8-A&t=1s
<br> Link 2 -> https://www.youtube.com/watch?v=-m5ywU8SW9E
<br> Link 3 -> https://www.youtube.com/watch?v=DNGI5aD9MJs&t=837s
<br> Link 4 -> https://www.youtube.com/watch?v=GGBzMpIAgz4&t=1324s 

# Documentos
- [Visão](documentação/doc-visao.md)
- [User Stories](documentação/doc-userstories.md)   
- [Modelo](documentação/doc-modelos.md)
- [Iteração](documentação/plano-iteracoes.md)              
- [Arquitetura](documentação/doc-arquitetura.md)               

# Instruções do Projeto
<h2>Executando o projeto sem docker</h2>

<p>Para rodar o projeto, siga as etapas abaixo:</p>

<ol>

<li>Crie um ambiente virtual para isolar as dependências do projeto:</li>
    <pre>python -m venv venv</pre>

<li>Ative o ambiente virtual:</li>
<ul>
    <li>No Windows:</li>
    <pre>venv\Scripts\activate</pre>
    <li>No Linux/MacOS:</li>
    <pre>source venv/bin/activate</pre>
</ul>

<li>Instale as dependências do projeto:</li>
<pre>pip install -r requirements.txt</pre>

<li>Gere sua SECRET_KEY a partir do seguinte comando no terminal:</li>
<pre>python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
</pre>

<li>Crie um arquivo .env na raiz do diretório do projeto, copie o conteudo de .env.example e adicione sua SECRET_KEY, logo apos crie o bando de dados e preencha os demais campos</li>
<pre>
SECRET_KEY='your-secret-key-here'
#True or False
DEBUG=True
POSTGRES_DB=
POSTGRES_USER=
POSTGRES_PASSWORD=
DB_HOST=
DB_PORT=5432
  </pre>

<li>Faça as migrações do banco de dados:</li>
<pre>python manage.py makemigrations</pre>

<li>Faça as migrações do banco de dados:</li>
<pre>python manage.py migrate</pre>

<li>Inicie o servidor de desenvolvimento:</li>
<pre>python manage.py runserver</pre>

<li>Abra o navegador e acesse o endereço http://localhost:8000 para acessar a aplicação.</li>
</ol>

# Usando Docker
<li>Para rodar os containers:</li>
<pre> docker compose up -d </pre>

<li>Para acessar o projeto:</li>
<pre> http://localhost:8000/ </pre>
