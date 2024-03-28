
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
| **Descrição** | O sistema facilitará o processo de pagamento para clientes que procuram suporte técnico para dispositivos móveis. Assim que o cliente decidir pelo serviço e estiver pronto para efetuar o pagamento, ele será direcionado para a página de pagamento, seja através de um botão dedicado na página de suporte técnico. Na página de pagamento, todas as informações relevantes, incluindo os serviços selecionados e seus preços correspondentes, serão exibidas de forma clara para o cliente revisar antes de prosseguir. O cliente terá a opção de escolher entre diferentes métodos de pagamento, como cartão de crédito, débito, transferência bancária, entre outros. |
| **Requisitos envolvidos** |                                                    |
| RF14          | Direcionamento para a página de pagamento. |
| RF15          | Exibição clara das informações de serviço e preços.  |
| RF16          | Opções de métodos de pagamento.        |
| RF17          | Segurança dos dados de pagamento. |
| RF18          | Confirmação de pagamento. |
| RF19          | Gerar comprovante de pagamento. |

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
| **TA05.01** | O usuário tenta realizar o pagamento de um pedido com todas as informações de pagamento válidas. O sistema processa o pagamento com sucesso e exibe uma mensagem de confirmação da transação.  |
| **TA05.02** | Ao tentar realizar o pagamento, se algum dado do cartão de crédito ou informações de pagamento forem inválidos, o sistema informa o usuário sobre os campos incorretos e solicita informações válidas. |
| **TA05.03** |  O usuário seleciona o método de pagamento desejado. O sistema exibe na tela todas as opções disponíveis de pagamento, incluindo cartão de crédito, PayPal, entre outros. |
| **TA05.04** |  Caso o método de pagamento escolhido não esteja disponível, o sistema informa o usuário sobre a falta de opções de pagamento e fornece orientações sobre como proceder. |
| **TA05.05** | O usuário tenta realizar o pagamento de um pedido, mas ocorre uma falha no processamento. O sistema exibe uma mensagem de erro clara e orienta o usuário sobre como resolver o problema, como verificar a conexão com a internet ou entrar em contato com o suporte ao cliente. |