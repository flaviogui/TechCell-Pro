
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
| RF06          | O sistema deve fornecer uma página de pagamento acessível a partir da página de suporte técnico. |
| RF07          | As informações relevantes, incluindo serviços selecionados e preços correspondentes, devem ser exibidas claramente na página de pagamento.  |
| RF08          | Os clientes devem ter a capacidade de escolher entre diferentes métodos de pagamento, como cartão de crédito, débito, transferência bancária, entre outros.        |
| RF09          | Assegurar a transmissão segura de dados sensíveis do cliente durante o processo de pagamento, utilizando protocolos de criptografia padrão. |
| RF10          | Após a conclusão bem-sucedida do pagamento, o sistema deve gerar automaticamente um comprovante de pagamento e enviá-lo para o email cadastrado pelo cliente. |
| RF11          | Em caso de erros durante o processo de pagamento, o sistema deve exibir mensagens claras para orientar o cliente sobre como proceder. |
| RF12          | Após o pagamento ser confirmado com sucesso, o sistema deve fornecer uma confirmação imediata na página, indicando que o processo foi concluído com êxito. |
| RF13          | Todas as transações de pagamento devem ser registradas de forma precisa e segura para fins de auditoria. |
| RF14          | O sistema deve integrar-se a gateways de pagamento confiáveis para processar transações financeiras de forma eficiente e segura. |
| RF15          | Os clientes devem ter a opção de salvar métodos de pagamento para facilitar transações futuras. |
| RF16          | O sistema deve permitir que os clientes revisem e editem os detalhes do pagamento antes de confirmar a transação. |
| RF17          | Os clientes devem receber notificações por email e/ou SMS após a conclusão bem-sucedida do pagamento. |
| RF18          | O sistema deve disponibilizar um histórico de transações de pagamento para os clientes visualizarem suas compras anteriores. |
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
| **TA05.01** | Garantir que os usuários possam acessar a página de pagamento facilmente a partir da página de suporte técnico.  |
| **TA05.02** | Verificar se todos os serviços prestados são exibidos corretamente, incluindo detalhes e preços, na página de pagamento. |
| **TA05.03** | Testar a funcionalidade de escolha do método de pagamento, assegurando que os dados sensíveis do cliente sejam transmitidos de forma segura. |
| **TA05.04** | Verificar se o sistema gera e envia corretamente o comprovante de pagamento para o email cadastrado pelo cliente. |
| **TA05.05** | Testar a exibição de mensagens claras em caso de erro durante o processo de pagamento, garantindo uma experiência de usuário amigável. |
| **TA05.06** | Confirmar que os clientes visualizam imediatamente uma confirmação de sucesso após efetuar o pagamento. |
| **TA05.07** | Verificar se os itens do carrinho são removidos e se o estoque é atualizado após a conclusão do pagamento. |
| **TA05.08** | Testar se as transações de pagamento são registradas corretamente para fins de auditoria. |
| **TA05.09** | Verificar a integração com gateways de pagamento, garantindo eficiência e segurança no processamento das transações financeiras. |
| **TA05.10** | Testar a funcionalidade de salvar métodos de pagamento para facilitar transações futuras. |
| **TA05.11** | Garantir que os clientes possam revisar e editar os detalhes do pagamento antes de confirmar a transação. |
| **TA05.12** | Verificar se os clientes recebem notificações por email e/ou SMS após a conclusão bem-sucedida do pagamento. |
| **TA05.13** | Testar a disponibilização de um histórico de transações de pagamento para os clientes visualizarem suas compras anteriores. |
| **TA05.14** | Verificar se o pagamento é processado com sucesso quando todos os dados fornecidos pelo cliente estão corretos. |
| **TA05.15** | Testar a exibição de mensagem de erro quando ocorre falha no processamento do pagamento devido a dados inválidos ou erro no sistema. |