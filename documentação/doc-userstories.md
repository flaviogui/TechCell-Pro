
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


