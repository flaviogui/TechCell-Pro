
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
| 12/07/2020 | 1.2.0   | Detalhamento do User Story US03 | Gabriel    |
| 12/07/2020 | 1.3.0   | Detalhamento do User Story US04 | Fabio      |
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


### User Story US03 - Manter Funcionário

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Como gerente, eu quero ser capaz de gerenciar as informações dos funcionários para garantir que todos os dados relevantes estejam atualizados e acessíveis.|
                    

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF15          | Cadastrar Funcionário |
| RF16          | Alterar Funcionário   |
| RF17          | Excluir Funcionário   |
| RF18          | Listar Funcionário    |
| RF19          | Visualizar Funcionário|


|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 3 diaas                             | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Fábio                               | 
| **Desenvolvedor**         | Gabriel                             | 
| **Revisor**               | Flavio                              | 
| **Testador**              | Laian                               | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA03.01** | O gerente deve poder acessar a funcionalidade de cadastro de funcionário.|
| **TA03.02** | O gerente deve poder cadastrar um novo funcionário com nome, email, CPF, telefone e cargo.|
| **TA03.03** | Após o cadastro de um funcionário, o sistema deve confirmar o sucesso do cadastro. |
| **TA03.04** | O gerente deve poder acessar a funcionalidade de alteração de funcionário. |        
| **TA03.05** | O gerente deve poder alterar o nome, email, telefone e cargo de um funcionário existente.  |
| **TA03.06** | Após a alteração das informações de um funcionário, o sistema deve confirmar o sucesso da alteração.|
| **TA03.07** | O gerente deve poder acessar a funcionalidade de exclusão de funcionário.|
| **TA03.08** | O gerente deve poder excluir um funcionário específico. |
| **TA03.09** | Após a exclusão de um funcionário, o sistema deve confirmar o sucesso da exclusão. |
| **TA03.10** | O gerente deve poder acessar a funcionalidade de listagem de funcionários.|
| **TA03.11** | O sistema deve exibir uma lista de todos os funcionários cadastrados, incluindo nome, email, telefone e cargo.|
| **TA03.12** | O gerente deve poder acessar a funcionalidade de visualização de um funcionário específico.|
| **TA03.13** | O sistema deve exibir todas as informações do funcionário selecionado, incluindo nome, email, CPF, telefone e cargo.|

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


### User Story US05 - Manter Fornecedor
               	                                                               
|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema permitirá o gerenciamento completo de fornecedores, garantindo que os dados de fornecedores sejam cadastrados, atualizados, visualizados, listados e excluídos conforme necessário. Isso inclui o registro de informações detalhadas como Nome, CNPJ, Endereço, Telefone, Email, Produtos/Peças Fornecidas e Data de Cadastro. Todas essas operações estarão disponíveis para o Gerente através de uma interface amigável e eficiente. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF0035        | Cadastrar Fornecedor com todos os atributos necessários. |
| RF0036        | Permitir a alteração das informações do fornecedor. |
| RF0037        | Permitir a exclusão das informações cadastradas do fornecedor. |
| RF0038        | Permitir a listagem de todos os fornecedores cadastrados. |
| RF0039        | Permitir a visualização das informações detalhadas de um fornecedor específico. |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 5h                                  | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 6 PF                                | 
| **Analista**              | Gabriel                             | 
| **Desenvolvedor**         | Fábio                               | 
| **Revisor**               | Flávio                              | 
| **Testador**              | Samuel                              | 
| **Desenvolvedor**         | Laian                               |

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | O usuário cadastra um novo fornecedor com todas as informações válidas. O sistema salva os dados e exibe uma mensagem de confirmação do cadastro. |
| **TA02.02** | O usuário tenta alterar as informações de um fornecedor existente. O sistema atualiza os dados e confirma a alteração. |
| **TA03.03** | O usuário tenta excluir um fornecedor. O sistema remove os dados do fornecedor e confirma a exclusão. |
| **TA03.04** | O usuário solicita a listagem de todos os fornecedores. O sistema exibe a lista completa de fornecedores cadastrados. |
| **TA03.05** | O usuário visualiza as informações detalhadas de um fornecedor específico. O sistema exibe todas as informações relevantes de forma clara. |

### User Story US07 - Manter Peças
                                                               
|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema permitirá o gerenciamento completo das peças utilizadas pela loja de assistência técnica. O Gerente poderá cadastrar novas peças, bem como alterar, visualizar, listar e excluir peças existentes. Cada peça incluirá informações como nome, descrição, código, quantidade em estoque, preço de compra e fornecedor, garantindo que todas as operações relacionadas às peças sejam realizadas de maneira eficiente e organizada. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| **RF0030**    | Cadastrar Peça com os atributos necessários: nome, descrição, código, quantidade em estoque, preço de compra e fornecedor. |
| **RF0031**    | Permitir a alteração das informações de uma peça cadastrada, incluindo nome, descrição, código, quantidade em estoque, preço de compra e fornecedor. |
| **RF0032**    | Permitir a exclusão das informações cadastradas de uma peça. |
| **RF0033**    | Permitir a listagem de todas as peças cadastradas. |
| **RF0034**    | Permitir a visualização das informações detalhadas de uma peça específica. |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 6h                                  | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Gabriel                             | 
| **Desenvolvedor**         | Fábio                               | 
| **Revisor**               | Flávio                              | 
| **Testador**              | Samuel                              | 
| **Desenvolvedor**         | Laian                               |

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | O usuário cadastra uma nova peça com todas as informações válidas. O sistema salva os dados e exibe uma mensagem de confirmação do cadastro. |
| **TA02.02** | O usuário tenta alterar as informações de uma peça existente. O sistema atualiza os dados e confirma a alteração. |
| **TA03.03** | O usuário tenta excluir uma peça. O sistema remove os dados da peça e confirma a exclusão. |
| **TA03.04** | O usuário solicita a listagem de todas as peças. O sistema exibe a lista completa de peças cadastradas. |
| **TA03.05** | O usuário visualiza as informações detalhadas de uma peça específica. O sistema exibe todas as informações relevantes de forma clara. |


### User Story US08 - Manter Serviços
               	                                                               
|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | O sistema permitirá o gerenciamento completo dos serviços oferecidos pela loja de assistência técnica. O Gerente poderá cadastrar novos serviços, bem como alterar, visualizar, listar e excluir serviços existentes. Cada serviço incluirá informações como nome, descrição, preço e duração estimada, garantindo que todas as operações relacionadas aos serviços sejam realizadas de maneira eficiente e organizada. |

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF0025        | Cadastrar Serviço com os atributos necessários: nome, descrição, preço e duração estimada. |
| RF0026        | Permitir a alteração das informações de um serviço cadastrado. |
| RF0027        | Permitir a exclusão das informações cadastradas de um serviço. |
| RF0028        | Permitir a listagem de todos os serviços cadastrados. |
| RF0029        | Permitir a visualização das informações detalhadas de um serviço específico. |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 5h                                  | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 6 PF                                | 
| **Analista**              | Gabriel                             | 
| **Desenvolvedor**         | Fábio                               | 
| **Revisor**               | Flávio                              | 
| **Testador**              | Samuel                              | 
| **Desenvolvedor**         | Laian                               |

| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | O usuário cadastra um novo serviço com todas as informações válidas. O sistema salva os dados e exibe uma mensagem de confirmação do cadastro. |
| **TA02.02** | O usuário tenta alterar as informações de um serviço existente. O sistema atualiza os dados e confirma a alteração. |
| **TA03.03** | O usuário tenta excluir um serviço. O sistema remove os dados do serviço e confirma a exclusão. |
| **TA03.04** | O usuário solicita a listagem de todos os serviços. O sistema exibe a lista completa de serviços cadastrados. |
| **TA03.05** | O usuário visualiza as informações detalhadas de um serviço específico. O sistema exibe todas as informações relevantes de forma clara.
