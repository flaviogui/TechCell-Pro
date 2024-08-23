from django.shortcuts import render
from pecaApp.models import Peca
from clienteApp.models import Cliente
from aparelhoApp.models import Aparelho
from funcionarioApp.models import Funcionario
from appConfirmarReparo.models import Reparo
from fornecedorApp.models import Fornecedor
from ferramentaApp.models import Ferramenta
from servicoApp.models import Servico
from produtosApp.models import Produto
from django.views.generic import TemplateView

def dashboard_view(request):
    pecas = Peca.objects.all()
    clientes = Cliente.objects.all()
    aparelhos = Aparelho.objects.all()
    funcionarios = Funcionario.objects.all()
    reparos = Reparo.objects.all()
    fornecedores = Fornecedor.objects.all()
    ferramentas = Ferramenta.objects.all()
    servicos = Servico.objects.all()
    produtos = Produto.objects.all()
    
    context = {
        'pecas': pecas,
        'clientes': clientes,
        'aparelhos': aparelhos,
        'funcionarios': funcionarios,
        'reparos': reparos,
        'fornecedores': fornecedores,
        'ferramentas': ferramentas,
        'servicos': servicos,
        'produtos': produtos
    }
    return render(request, 'dashboard.html', context)

