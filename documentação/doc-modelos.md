# Documento de Modelos

Neste documento temos o modelo Conceitual (UML) ou de Dados (Entidade-Relacionamento). Temos também a descrição das entidades e o dicionário de dados.

Para a modelagem pode se usar o Astah UML ou o BrModelo. Uma ferramenta interessante para modelos UML é a [YUML](http://yuml.me), no link temos um exemplo de [Modelo UML com YUML](yuml/monitoria-yuml.md). Atualmente é possível usar a ferramenta **Mermaid** segundo o blog do GitHub [Include diagrams in your Markdown files with Mermaid](https://github.blog/2022-02-14-include-diagrams-markdown-files-mermaid/). A documentação do **Mermaid** pode ser encontrada em [Mermaid in GitHub](https://mermaid-js.github.io/mermaid).

## Modelo Conceitual

### Diagrama de Classes usando Mermaid

```mermaid
classDiagram
    class Aparelho {
        - marca: char
	- modelo: char
          + inserir_aparelho(marca: char, modelo: char): void
          + consultar_Aparelho(modelo: char): Aparelho 
          + excluir_aparelho(aparelho: Aparelho): void 
          + buscar_Aparelho(modelo: char): Aparelho 
          + alterar_Aparelho(aparelho: Aparelho): void 
    }
    
    class Cliente {
        - nome: char
        - email: char
        - telefone: char
        - cpf: char
          + inserir_Cliente(nome: char, email: char, telefone: char, cpf: char): void 
          + consultar_cliente(cpf: char): Cliente 
          + setNome(nome: Cliente, nome: char): void 
	  + setEmail(email: Cliente, email: char): void 
	  + setTelefone(telefone: Cliente, telefone: char): void	
	  + setCpf(cpf: Cliente, cpf: char): void	
	  + getNome(): char	
	  + validar_Cpf(cpf: char): boolean	
	  + buscar_Cliente(cpf: char): Cliente
	  + buscar_Cliente(email: char): Cliente
	  + excluir_Cliente(cliente: Cliente): void 	
	  + alterar_Cliente(c: Cliente): Cliente
	  + alterar_Cliente(cpf: char): Cliente 	
    }
    
    class Pedido {
       - problema: char  
       - status_Pedido: boolean
       - data_Pedido: char   
       - id_Pedido: int   
       - cpf_cliente: char   
       	   + selecionar_Pedido(problema: char): void   
	   + setStatusPedido(pedido: Pedido, status: boolean): void   
	   + setProblema(problema : char ): void
	   + getStatus() : boolean	
	   + gerar_Pagamento(p: Pedido): void  	
	   + finalizar_Pedido(p: Pedido): void  	
    }
    
    class Pagamento {
	- modo_pagamento: int  
	- data_pagamento: char  
	- valor_Pagamento: float  	
	  + gerar_Comprovante(): void  	
	  + efetuar_Pagamento(): void  	
	  + reembolsar(valor_Pagar: float): boolean 	
     }

     class Relatorio{
      	- nome_Relatorio: char  
      	  + gerar_Relatorios(pedidos: Pedido[]): void
	  + exibir_Relatorios(): void
     }

    class AparelhoPedido {
        - aparelho : Aparelho
        - pedido : Pedido
        - serial : char
    }

     Aparelho "1" -- "0..*" Pedido : possui
     Cliente "1" -- "0..*" Pedido : realiza
     Pedido "1" -- "0..*" Pagamento : gera
     Pedido "1" -- "0..*" Relatorio : gera
     Aparelho "1" -- "0..*" AparelhoPedido
     Pedido "1" -- "0..*" AparelhoPedido


```


### Descrição das Entidades

Descrição sucinta das entidades presentes no sistema.

| Entidade | Descrição   |
|----------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aparelho   | Entidade abstrata para representar informações gerais dos aparelhos: marca, modelo, inserir_aparelho(), consultar_aparelho(), excluir_aparelho(), buscar_aparelho(), alterar_aparelho(). A classe Aparelho estende a classe abstrata Pedido                                                  |
| Cliente     | Entidade que representa um Cliente tem as informações: nome, email, email, telefone, cpf, inserir_cliente(), consultar_cliente(), setnome(), setemail(), settelefone(), excluir_cliente(), getnome(), validarcpf(),bucar_cliente(), . A classe Cliente estende a classe abstrata Pedido. |
| AparelhoPedido    | Entidade que representa a conexão entre o aparelho e o pedido e tem as informações: aparelho, pedido, serial. A classe AparelhoPedido estende a classe abstrata Pedido.                                                                   |
| Pedido    | Entidade que representa um Pedido tem as informações: problema, data_pedido, status, id_pedido, cpf, solicita_Pedido(), setStatus(), setProblema(), getStatus(), gerar_pagamento(), finalizar_Pedido(). A classe Pedido estende a classe abstrata Relatorio.
| Pagamento    | Entidade que representa um Pagamento tem as informações: modo_pagar, data_pagamento, valor_Pagar, gerar_Comprovante(), efetuar_Pagamento(), reembolsar(). A classe Pagamento é dependente da classe abstrata Pedido.                                                                   |
| Relatorio    | Entidade que representa um Relatorio tem as informações: nome_Relatorio, gerar_Relatorio(), exibir_Relatorio(). A classe Relatorio estende a classe abstrata Pedido.                                                                   |

### Dicionário de Dados

|   Tabela   | Cliente |
| ---------- | ----------- |
| Descrição  | Armazena as informações dos clientes da assistência tecnica de celulares. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id_cliente    | Número de idenficação do cliente | SERIAL       | ---     | PK / Identity |
| nome          | Nome do cliente                  | VARCHAR      | 150     | Not Null |
| email         | Endereço de e-mail do cliente    | VARCHAR      | 150     | Not Null |
| fone          | Número de telefone do cliente    | VARCHAR      | 150     | Not Null |
| cpf           | Número de CPF do cliente         | VARCHAR      | 250     | Not Null |

|   Tabela   | Aparelho |
| ---------- | ----------- |
| Descrição  | Armazena as informações dos aparelhos da assistência tecnica de celulares. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| IMEI          | IMEI do aparelho                 | SERIAL       | ---     | PK / Identity |
| num_serie     | Número de série do aparelho      | VARCHAR      | 150     | Not Null |
| marca         | Marca do aparelho                | VARCHAR      | 150     | Not Null |
| modelo        | Modelo do aparelho               | VARCHAR      | 150     | Not Null |
| descricao     | Descrição problema pelo cliente  | VARCHAR      | 250     | Not Null |

|   Tabela   | Pedido |
| ---------- | ----------- |
| Descrição  | Armazena as informações dos pedidos da assistência tecnica de celulares. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id_pedido     | Identificador do pedido          | SERIAL       | ---     | PK / Identity |
| status        | Estado do pedido (ativo/inativo) | BOOLEAN      | 150     | Not Null |
| data          | Data do pedido                   | VARCHAR      | 150     | Not Null |
| problema      | Descrição do problema tecnico    | VARCHAR      | 150     | Not Null |
| cpf_cliente   | CPF cliente associado ao pedido  | VARCHAR      | 250     | FK / Not Null |

|   Tabela   | Pagamento |
| ---------- | ----------- |
| Descrição  | Armazena as informações dos pagamentos da assistência tecnica de celulares. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| id_pagamento  | Identificador de pagamento       | SERIAL       | ---     | PK / Identity         |
| modo_pagamento| Modo de pagamento                | BOOLEAN      | 150     | Not Null              |
| valor_pagament| Valor do pagamento               | VARCHAR      | 150     | Not Null              |
| cpf_cliente   | CPF cliente associado ao pedido  | VARCHAR      | 250     | FK / Not Null         |


|   Tabela   | Relatório |
| ---------- | ----------- |
| Descrição  | Armazena as informações da assistência tecnica de celulares. |

|  Nome         | Descrição                        | Tipo de Dado | Tamanho | Restrições de Domínio |
| ------------- | -------------------------------- | ------------ | ------- | --------------------- |
| nome_relatorio| Identificador de pagamento       | VARCHAR      | ---     | Not Null              |
