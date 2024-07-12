from django.shortcuts import render, redirect  # type: ignore
from django.views.generic import CreateView  # type: ignore
from .models import Cliente

# Função para criar um cliente


class ClienteCreateView(CreateView):
    model = Cliente
    fields = ['nome', 'email', 'telefone', 'cpf']
    template_name = 'cliente_form.html'
    # Redireciona para a lista de clientes após a criação
    success_url = '/clientes/lista/'

    # Opcional: Sobrescrever o método form_valid para realizar ações adicionais após a criação do cliente
    def form_valid(self, form):
        # Realizar alguma ação, como enviar um email de boas-vindas ao cliente
        cliente = form.save(commit=False)
        # ... sua lógica aqui ...
        cliente.save()
        return super().form_valid(form)
