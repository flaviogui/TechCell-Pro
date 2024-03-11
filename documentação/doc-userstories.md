
# Documento Lista de User Stories

Documento construído a partido do **Modelo BSI - Doc 004 - Lista de User Stories** que pode ser encontrado no
link: https://docs.google.com/document/d/16em16bsI-rFwi8JUyU3TisPLEVTB6_Gv/edit

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

### User Story US02 - Manter Produto

|               |                                                                |
| ------------- | :------------------------------------------------------------- |
| **Descrição** | Como técnico responsável pela assistência técnica de celulares, eu gostaria de cadastrar informações sobre um produto, incluindo Marca, Modelo e o CPF do proprietário Para que seja possível manter um registro organizado e preciso dos dispositivos em assistência. Além disso, desejo a capacidade de corrigir qualquer dado incorretamente cadastrado e permitir que o cliente consulte essas informações para assegurar a precisão dos registros.

| **Requisitos envolvidos** |                                                    |
| ------------- | :------------------------------------------------------------- |
| RF01          | Cadastrar Produto |
| RF02          | Alterar Produto  |
| RF03          | Consultar Produto        |
| RF04          | Vizualizar detalhes do Produto |

|                           |                                     |
| ------------------------- | ----------------------------------- | 
| **Prioridade**            | Essencial                           | 
| **Estimativa**            | 4 dias                              | 
| **Tempo Gasto (real):**   |                                     | 
| **Tamanho Funcional**     | 7 PF                                | 
| **Analista**              | Gabriel                             | 
| **Desenvolvedor**         | Fábio                               | 
| **Revisor**               | Laian                               | 
| **Testador**              | Samuel                              | 


| Testes de Aceitação (TA) |  |
| ----------- | --------- |
| **Código**      | **Descrição** |
| **TA01.01** | O técnico tenta cadastrar um novo produto com informações válidas. O sistema permite o cadastro do produto. 
                O sistema exibe uma  mensagem de confirmação de cadastro. |
| **TA01.02** | Ao tentar cadastrar o produto,  caso algum dado do aparelho seja inválido, ele será informado e deverá 
                apresentar uma informação válida. |
| **TA01.03** | O técnico informa ao sistema o modelo cadastrado. 2. O sistema exibe na tela todas as informações do aparelho. |
| **TA01.04** | Caso o aparelho não esteja cadastrado, o sistema exibe na tela a mensagem: “O aparelho não foi cadastrado no sistema. |
| **TA01.05** | Técnico altera dados de um produto com informações incorretas.
                O sistema valida as alterações durante a edição. O sistema não permite a alteração se dados inválidos forem detectados. |


