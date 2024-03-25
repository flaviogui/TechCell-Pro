






























































































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
