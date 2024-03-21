
# Documento Lista de User Stories

Documento construído a partido do **Modelo BSI - Doc 004 - Lista de User Stories** que pode ser encontrado no
link: https://docs.google.com/document/d/1Ns2J9KTpLgNOpCZjXJXw_RSCSijTJhUx4zgFhYecEJg/edit?usp=sharing

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento 001 - Documento de Visão](doc-visao.md). Este documento também pode ser adaptado para descrever Casos de Uso. Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões

| Data       | Versão  | Descrição                          | Autor                          |
| :--------- | :-----: | :--------------------------------: | :----------------------------- |
| 22/06/2020 | 0.0.1   | Template e descrição do documento  | Taciano |
| 23/06/2020 | 0.0.2   | Detalhamento do User Story US01    | Taciano |
| ...        | ...     | ...                                | ...     |
| 12/07/2020 | 1.0.0   | Documento completo com o detalhamento de todos os User Stories | Taciano     |
| 30/04/2022 | 1.6.0   | Adição das informações da equipe: Analista, Desenvolvedor, Revisor e Testador. | Taciano |



### User Story US01 - Manter Usuário

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve manter um cadastro de usuário que tem acesso ao sistema via login e senha. Um usuário tem os atributos name, id, email, username, data de nascimento, tipo de usuário, status, password, avatarURL. O email será o login e ele pode registrar-se diretamente no sistema, o avatarURL é um link para uma foto de seu perfil. Além disso o usuário poderá alterar alguns dados, como o e-mail ou a senha. O usuário administrador do sistema pode realizar as operações de adicionar, alterar, remover e listar os usuários comuns do sistema. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Cadastrar Usuário |
| RF02          | Alterar Usuário  |
| RF03          | Consultar Usuários        |
| RF04          | Excluir Usuário |
| RF05          | Vizualizar detalhes do Usuário |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 8 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Taciano                             | 
| **Desenvolvedor**         | Zé                                  | 
| **Revisor**               | Maria                               | 
| **Testador**              | Xuxa                                | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | Descrever o teste de aceitação 01 do US01 |
| **TA01.02** | Descrever o teste de aceitação 02 do US01 |
| **TA01.03** | Descrever o teste de aceitação 03 do US01 |
| **TA01.04** | Descrever o teste de aceitação 04 do US01 |

### User Story US05 - Realizar Pagamento

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Como cliente que precisa de suporte técnico para celulares, desejo efetuar o pagamento pelo serviço de assistência relacionado a dispositivos móveis. |
| **Requisitos envolvidos** |                                                    |
| RF06          | Acessar Página de Pagamento |
| RF07          | Exibir Informações Relevantes na Página de Pagamento para o cliente  |
| RF08          | Escolher Método de Pagamento        |
| RF09          | Transmissão Segura de Dados Sensíveis do Cliente |
| RF10          | Gerar Comprovante de Pagamento |
| RF11          | Exibir Mensagem de Erro durante o Pagamento |
| RF12          | Confirmar Pagamento com Sucesso |
| RF13          | Registrar Transações de Pagamento de Suporte para Auditoria |
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 12 h                                 | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 8 PF                                | 
| **Analista**              | Gabriel                                    | 
| **Desenvolvedor**         | Laian e Fabio                              | 
| **Revisor**               | Flavio                               | 
| **Testador**              | Samuel                                 | 

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA05.01** | Acessar a página de pagamento a partir da página de suporte técnico  |
| **TA05.02** | Verificar se todos serviços prestados são exibidos corretamente com preços na página de pagamento. |
| **TA05.03** | Testar a escolha do método de pagamento e a transmissão segura de dados. |
| **TA05.04** | Verificar se o comprovante de pagamento é gerado e enviado para o email cadastrado. |
| **TA05.05** | Testar a exibição de mensagens claras em caso de erro durante o pagamento. |
| **TA05.06** | Confirmar a visualização imediata de sucesso no pagamento. |
| **TA05.07** | Verificar se os itens do carrinho são removidos e o estoque é atualizado. |
| **TA05.08** | Testar se as transações de pagamento são registradas corretamente para auditoria. |