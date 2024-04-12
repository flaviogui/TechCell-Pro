
# Documento Lista de User Stories

Documento construído a partido do **Modelo BSI - Doc 004 - Lista de User Stories** que pode ser encontrado no
link: https://docs.google.com/document/d/1Ns2J9KTpLgNOpCZjXJXw_RSCSijTJhUx4zgFhYecEJg/edit?usp=sharing

## Descrição

Este documento descreve os User Stories criados a partir da Lista de Requisitos no [Documento 001 - Documento de Visão](doc-visao.md). Este documento também pode ser adaptado para descrever Casos de Uso. Modelo de documento baseado nas características do processo easYProcess (YP).

## Histórico de revisões

| Data       | Versão  | Descrição                          | Autor                          |
| :--------- | :-----: | :--------------------------------: | :----------------------------- |
| 22/06/2020 | 0.0.1   | Template e descrição do documento  | Taciano |
| ...        | ...     | ...                                | ...     |
| 12/07/2020 | 1.0.0   | Detalhamento do User Story US01 | Samuel     |
| 12/07/2020 | 1.1.0   | Detalhamento do User Story US02 | Flávio     |
| 12/07/2020 | 1.2.0   | Detalhamento do User Story US03 | Fábio      |
| 12/07/2020 | 1.3.0   | Detalhamento do User Story US04 | Gabiel     |
| 12/07/2020 | 1.4.0   | Detalhamento do User Story US05 | Laian      |
| 30/04/2022 | 1.5.0   | Adição das informações da equipe: Analista, Desenvolvedor, Revisor e Testador. | Equipe |


### User Story US01 - Manter Cliente

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve manter um cadastro de cliente através do técnico que tem acesso ao sistema via login e senha. Um cliente tem os atributos nome, telefone, email e endereço. O cadastro do(s) técnico(s) será realizados pelos criadores do sistema, e o cadastro dos clientes será realizado pelo(s) técnico(s). o técnico poderá alterar o cliente caso tenha um dado incorreto, como também consultar um cliente caso o mesmo venha a contratar novamente os serviços do técnico, o técnico também poderá vizualizar informações do cliente para um eventual confirmação de dados e por fim, a o técnico poderá excluir o cliente caso seja preciso devido a força maior.

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Cadastrar Cliente |
| RF02          | Alterar Cliente  |
| RF03          | Consultar Cliente        |
| RF04          | Vizualizar detalhes do Cliente |
| RF05          | Excluir Cliente |


|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 8 h                                 | 
| **Tempo Gasto (real):**   | 8 h                                 | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Gabriel José                        | 
| **Desenvolvedor**         | Laian Kevin e Fábio                 | 
| **Revisor**               | Flávio                              | 
| **Testador**              | Samuel                              | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | O técnico informa, na tela Registrar, todos os dados para registrar o cliente corretamente, ao clicar em Salvar ele é notificado com uma mensagem de sucesso. Mensagem: Cadastro do cliente realizado com sucesso, aguardando ativação do administrador. |
| **TA01.02** | O Técnico informa, na tela Registrar, os dados para registrar o cliente incorretamente, ao clicar em Salvar ele é notificado com uma mensagem de erro. Mensagem: Cadastro não realizado, o campo “xxxx” não foi informado corretamente. |
| **TA01.03** | O Técnico informa, na tela Login, os dados para logar corretamente, ao clicar em Entrar ele é notificado com uma mensagem de erro. Mensagem: Técnico não ativado, aguardando ativação do administrador |
| **TA01.04** | O Técnico informa, na tela Login, os dados para logar corretamente, ao clicar em Entrar ele é encaminhado para a tela principal do sistema. É exibida a Mensagem: Login realizado com sucesso. |



### User Story US02 - Registrar Aparelho

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema deve manter um registro de todos os aparelhos defeituosos, com os atributos, marca, modelo, IMEI, número de série, e descrição do problema pelo cliente. O sistema ainda deve permitir a alteração dos dados que estejam incorretos, além da opção de buscar por determinado aparelho, como também, visualizar detalhes do dispositivo. E ao final do processo de registro será gerado um número de ordem de serviço do aparelho. O sistema também vai permitir a exclusão dos dados de algum aparelho em especifico.

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Cadastrar Aparelho |
| RF02          | Alterar Aparelho  |
| RF03          | Consultar Aparelho  | 
| RF04          | Vizualizar detalhes do Aparelho |
| RF05          | Excluir Aparelho |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 4 dias                              | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Gabriel José                        | 
| **Desenvolvedor**         | Laian Kevin e Fábio                 | 
| **Revisor**               | Flávio                              | 
| **Testador**              | Samuel                              | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**  | **Descrição** |
| **TA01.01** | O técnico tenta cadastrar um novo produto com informações válidas. O sistema permite o cadastro do produto. O sistema exibe uma  mensagem de confirmação de cadastro. |
| **TA01.02** | Ao tentar cadastrar o produto,  caso algum dado do aparelho seja inválido, ele será informado e deverá apresentar uma informação válida. |
| **TA01.03** | O técnico informa ao sistema o modelo cadastrado. 2. O sistema exibe na tela todas as informações do aparelho. |
| **TA01.04** | Caso o aparelho não esteja cadastrado, o sistema exibe na tela a mensagem: “O aparelho não foi cadastrado no sistema". |
| **TA01.05** | Técnico altera dados de um produto com informações incorretas. O sistema valida as alterações durante a edição. O sistema não permite a alteração se dados inválidos forem detectados. |


### User Story US03 - Análise do Problema

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema necessita de um campo que permita ao técnico realizar uma análise detalhada do problema. Este campo deve proporcionar acesso ao histórico de reparos do aparelho e disponibilizar ferramentas que auxiliem o técnico no diagnóstico do problema. O técnico deve ser capaz de registrar o problema e a solução proposta no sistema, e ao final, o sistema deve gerar o tempo e o custo estimado do reparo. |
                    

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF10          | Cadastrar Descrição|
| RF12          | Gerar Protocolo    |
| RF13          | Calcular Prazo |
| RF17          | Solicitar Assistencia |


|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 5 diaas                             | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Fábio                               | 
| **Desenvolvedor**         | Laian                               | 
| **Revisor**               | Gabriel                             | 
| **Testador**              | Samuel                              | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** |O técnico deve ter acesso ao histórico de reparos do aparelho |
| **TA01.02** | Ao tentar ter acesso ao histórico de reparo do apareho se não aparecer deve aparecer uma mensagem mostrando que o aparelho não teve reparos anteriores |
| **TA01.03** | O sistema deve fornecer ferramentas para auxiliar no diagnóstico do problema |
| **TA01.04** | Caso não seja possível fornecer ferramentas para auxiliar no diagnóstico do problema, pode-se considerar a implementação de recursos alternativos para facilitar a identificação dos problemas apresentados pelo aparelho |        |
| **TA01.05** | O técnico deve poder registrar o problema e a solução proposta no sistema  |
| **TA01.06** | Caso não seja possivel registrar o problema e a solução, deve se dar uma opção alternativa para o técnico fazer esse regisstro, por exemplo em um formulário físico |
| **TA01.07** |  O sistema deve emitir o tempo e custo do reparo|
| **TA01.08** |  Caso não seja possível implementar a funcionalidade de emitir automaticamente o tempo e custo do reparo pelo sistema, uma alternativa viável seria que o técnico responsável fornecesse uma estimativa do tempo necessário para o reparo e do custo envolvido manualmente. |

### User Story US04 - Confirmar Reparo

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Como técnico, após realizar todas as etapas necessárias de diagnóstico e reparo do aparelho, quero poder confirmar oficialmente que o reparo foi concluído com sucesso. Isso envolve verificar se todos os problemas identificados foram corrigidos, se o aparelho está funcionando conforme esperado e se todas as peças e componentes estão em seu devido lugar. Além disso, quero garantir que o aparelho esteja pronto para ser devolvido ao cliente em um estado totalmente funcional. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF012          | Gerar Protocolo |
| RF013          | Calcular Prazo  |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 3 dias                              | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 5 PF                                | 
| **Analista**              | Gabriel                             | 
| **Desenvolvedor**         | Fábio                               | 
| **Revisor**               | Flávio                              | 
| **Testador**              | Samuel                              | 
| **Desenvolvedor**         | Laian                               |

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | Técnico informa o cliente sobre o custo do reparo. O cliente confirma o reparo antes de ele ser iniciado. O sistema gera um comprovante de reparo. O sistema notifica o cliente quando o reparo estiver concluído. |
| **TA02.02** | Técnico registra o pagamento do reparo no sistema. O sistema valida o pagamento e atualiza o status do reparo para concluído. |


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


|                           |                                     |
| ------------------------- | ----------------------------------- | 
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