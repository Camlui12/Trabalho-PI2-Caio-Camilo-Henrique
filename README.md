# 1. Introdução
Este documento tem o objetivo de apresentar a ideia de um sistema que será implementado com o objetivo de auxiliar e melhorar o desempenho operacional de um estacionamento. Ele tem toda a documentação necessária para basear a construção do software a ser desenvolvido.

# 2. Visão Geral do Produto
### 2.1. Minimundo
O sistema de gerenciamento de estacionamento tem o objetivo de informatizar e automatizar as operações de controle de entrada e saída de veículos em um estacionamento privado. Atualmente, essas operações são feitas de forma manual, o que pode gerar erros e dificultar o controle financeiro e operacional.

O sistema permite o registro da entrada e saída de veículos, armazenando informações como placa, modelo, cor e horário de entrada/saída. Com base no tempo de permanência, o sistema calcula automaticamente o valor a ser pago pelo cliente do estacionamento, considerando regras pré-definidas de tarifação (por exemplo, tarifa por hora ou frações).

Além disso, o sistema oferece funcionalidades para consultar o histórico de veículos que utilizaram o estacionamento, emitir relatórios financeiros, e de lotação. Também será possível cadastrar planos mensais para clientes fixos, permitindo o gerenciamento de mensalistas.

O objetivo principal do sistema é otimizar o processo de controle de veículos, reduzir erros humanos, melhorar a condição de trabalho dos funcionários e fornecer relatórios precisos para o administrador do estacionamento.


### 2.2. Delimitação do Escopo inicial
O escopo inicial do sistema de gerenciamento de estacionamento contempla o desenvolvimento de uma aplicação web responsiva que permita o controle operacional essencial de um estacionamento rotativo. O sistema permitirá o cadastro de veículos mediante preenchimento de dados como placa, modelo, cor e tipo (por exemplo, carro, moto ou utilitário), sempre que a placa informada ainda não estiver registrada no banco de dados. Caso o veículo já esteja cadastrado, será possível apenas registrar o horário de entrada, vinculando a movimentação ao histórico existente. Isso viabiliza funcionalidades como a análise de frequência de clientes. O sistema também será responsável por registrar os horários de saída dos veículos, calcular automaticamente o tempo de permanência e aplicar as regras de tarifação configuradas, incluindo valores por hora ou fração, teto máximo diário e cobrança proporcional por diárias quando o tempo de permanência exceder 24 horas. Além disso, será possível realizar o cadastro de usuários com diferentes níveis de acesso, como operadores e administradores, garantindo a segurança e a integridade das operações. O sistema manterá um histórico completo de entradas e saídas de veículos, bem como dos pagamentos realizados, e permitirá a geração de relatórios simples de movimentação e faturamento diário. Todas essas funcionalidades estarão disponíveis via navegador.

Funcionalidades como integração com sistemas de pagamento online, sensores de vaga, leitura automática de placas, emissão de nota fiscal eletrônica, aplicativo para clientes finais e integração com sistemas de segurança não fazem parte do escopo inicial, mas poderão ser consideradas em versões futuras. Este escopo busca estabelecer uma base robusta para a gestão do estacionamento, priorizando a automação das rotinas mais importantes e a organização das informações operacionais e financeiras.



# 3. Atores (Usuários) e Envolvidos
### a. Atores Principais
+ Administrador
+ Funcionários

### b. Atores secundários (se houver)
escrever aqui

### c. Envolvidos (não utilizarão o sistema, e apenas se houver)
+ Veículos

# 4. Requisitos do sistema
### 4.1. Regras de Negócio.
| N° | Nome | Descrição |
|:-------|:-----|:----------|
| RN01 | Cobrança mínima | O estacionamento cobra um valor fixo mínimo correspondente à primeira hora, mesmo que o veículo permaneça menos tempo. | É permitido um período de tolerância de 10 minutos sem cobrança, desde que o veículo saia dentro desse tempo. |
| RN02 | Cobrança por fração de hora | Após a primeira hora, o valor é calculado por frações de 15 minutos. |
| RN03 | Tolerância gratuita de tempo | É permitido um período de tolerância de 10 minutos sem cobrança, desde que o veículo saia dentro desse tempo. |
| RN04 | Acesso de assistente mensal | Clientes que assinam o plano mensal têm direito a entrar e sair do estacionamento quantas vezes quiserem no mês. |
| RN05 | Limites de vagas por tipo de veículo | O estacionamento possui quantidade limitada de vagas para cada tipo de veículo. |
| RN06 | Desconto para horários noturnos | Entre 23h e 6h é aplicado um desconto de 30% na tarifa padrão |
| RN07 | Cobrança diária máxima | Existe um valor máximo a ser cobrado por dia de permanência. |
| RN08 | Veículos com permanência superior a 12 horas | Se um veículo ultrapassar 12 horas de permanência, o valor é cobrado com base em diárias completas. |
| RN09 | Taxa extra por perda de ticket | Caso o cliente peca o ticket de entrada, será cobrada uma taxa fixa adicional. |
| RN10 | Descontos por fidelidade | O cliente receberá descontos com base na sua atividade mensal no estacionamento |

### 4.2. Requisitos Funcionais.
| N° | Nome | Descrição |
|:-------|:-----|:----------|
| RF01 | Cadastro de veículo | O sistema deve permitir o cadastro de um novo veículo, registrando placa, modelo e cor, caso ele não esteja presente no banco de dados |
| RF02 | Registro de entrada de veículo | O sistema deve permitir o registro da entrada de um veículo já cadastrado, vinculando o horário atual e dia ao respectivo registro do banco de dados |
| RF03 | Cálculo de estadia | O sistema deve calcular o preço a ser pago por estadia do veículo no momento de saída dele, com base no horário e data de entrada e regras de cobrança |
| RF04 | Horas de estadia | O sistema deve armazenar o tempo diário em horas que cada veículo permaneceu no estacionamento |
| RF05 | Usuários | O sistema deve permitir o cadastro, edição e exclusão de usuários do sistema (operadores e administradores). |
| RF06 | Relatórios | O sistema deve permitir a emissão de relatórios de fluxo de veículos diária, semanal e mensal. Além de exibir as respectivas receitas. |
| RF07 | Planos mensais | O sistema deve permitir o cadastro de clientes mensalistas e calcular a cobrança conforme o plano. |
| RF08 | Ocupação | O sistema deve exibir a quantidade de vagas disponíveis por tipo de veículo |
| RF09 | Configuração | O sistema deve permitir a configuração dos valores de tarifa, tolerância e teto diário pelo administrador. |


### 4.3. Requisitos Não-Funcionais.
| N° | Nome | Descrição |
|:-------|:-----|:----------|
| RNF01 | Acesso | O sistema deve ser acessível por meio de um navegador web (aplicação web responsiva). |
| RNF02 | Tempo de resposta | O tempo de resposta para registros de entrada ou saída não deve exceder 2 segundos. |
| RNF03 | Armazenamento | O sistema deve armazenar os dados em um banco de dados |
| RNF04 | Usuários | Apenas usuários autenticados devem acessar o sistema. |
| RNF05 | Permissão | O sistema deve ter níveis de permissão distintos (ex: operador não pode acessar configurações administrativas). |
| RNF06 | UX | O sistema deve seguir boas práticas de usabilidade, com uma interface intuitiva. |
| RNF07 | Compatibilidade | O sistema deve ser compatível com os navegadores modernos (Chrome, Firefox, Edge). |
| RNF08 | Offline | O sistema deve permitir operação offline para registro de entradas/saídas, sincronizando quando a conexão voltar (opcional, mais avançado). |
| RNF09 | Capacidade | O sistema deve ser capaz de atender até 100 usuários simultâneos sem perda de desempenho. |

# 5. Casos de Uso
### 5.1. Diagrama de Caso de Uso
Imagem aqui

### 5.2. Descrição dos Casos de Uso
| UC01 - Cadastrar Veículo |
|:-----------------------------|
| 1.1. Atores: Operador do estacionamento |
| 1.2. Objetivo: Permitir que o operador cadastre um novo veículo no sistema, inserindo dados como placa, modelo, cor e tipo, quando o veículo ainda não estiver registrado no banco de dados. |
| 1.3. Pré-Condições |
| 1.4. Pós-Condições |
| 1.5. Trigger |
| 1.6. Fluxo Básico |
| 1.7. Fluxo alternativo |
| 1.8. Fluxo de Exceção |
| 1.9. Referências Cruzadas (Requisitos Associados) |

| UC02 - Registrar Entrada de Veículo |
|:---------------------------------------|
| 1.1. Atores: Operador do estacionamento |
| 1.2. Objetivo: Registrar a entrada de um veículo já cadastrado, vinculando o horário atual ao seu histórico para controle de permanência. |

| UC03 - Registrar Saída de Veículo |
|:-------------------------------------|
| 1.1. Atores: Operador do estacionamento |
| 1.2. Objetivo: Permitir o registro da saída de um veículo, calcular automaticamente o valor a ser pago com base no tempo de permanência e regras de tarifação. |

| UC04 - Consultar Frequência de Veículos |
|:-------------------------------------------|
| 1.1. Atores: Administrador |
| 1.2. Objetivo: Exibir a quantidade de horas que um determinado veículo utilizou o estacionamento durante um período de tempo selecionado. |

| UC05 - Gerar Relatórios de Movimentação |
|:-------------------------------------------|
| 1.1. Atores: Administrador |
| 1.2. Objetivo: Gerar relatórios sobre entradas, saídas e faturamento diário ou por período definido. |

| UC06 - Cadastrar Usuário |
|:-----------------------------|
| 1.1. Atores: Administrador |
| 1.2. Objetivo: Permitir o cadastro de novos usuários do sistema, atribuindo níveis de acesso (como operador ou administrador). |

| UC07 - Autenticar Usuário |
|:-----------------------------|
| 1.1. Atores: Operador, Administrador |
| 1.2. Objetivo: Validar as credenciais de acesso do usuário ao sistema, liberando funcionalidades conforme seu nível de permissão. |

| UC08 - Configurar Regras de Cobrança |
|:----------------------------------------|
| 1.1. Atores: Administrador |
| 1.2. Objetivo: Permitir a configuração de valores de tarifa, tempo de tolerância e teto máximo diário. |

 UC07 - Consultar Vagas Disponíveis |
|:---------------------------------------|
| 1.1. Atores: Operador |
| 1.2. Objetivo: Exibir em tempo real a quantidade de vagas disponíveis, separadas por tipo de veículo. |

# 6. Diagrama de Classes
### 6.1. Diagrama
escrever aqui

### 6.2. Descrição das Entidades
escrever aqui

# 7. Banco de Dados
### 7.1. Esquema Lógico de Banco de Dados Relacional
imagem aqui

### 7.2. Descrições
escrever aqui

### 7.3. Observações
escrever aqui

# 8. Projeto Arquitetural do Sistema
### 8.1. Diagrama de Componentes
imagem aqui

### 8.2. Diagrama de Implantação
imagem aqui

# 9. Projeto Funcional do Sistema
### 9.1. Diagrama de Atividades
imagem aqui

### 9.2. Diagrama de Sequência
imagem aqui

### 9.3. Diagrama de Estados
imagem aqui

# 10. Banco de Dados Relacional
### 10.1. Criação do Banco de Dados
```sql
escrever código aqui
SELECT n sei oq n sei oq la
```

### 10.2. População inicial do banco
escrever aqui

# 11. Banco de Dados Não-Convencional
### 11.1. Diagrama do banco NOSQL
imagem aqui

### 11.2. Criação e População do Banco de Dados
escrever aqui

# 12. Implementação
escrever aqui

# 13. Testes de carga
### 13.1. Primeira Fase de Testes
#### 13.1.1. Medições
escrever aqui

#### 13.1.2. Resultados
escrever aqui

#### 13.1.3. Hipóteses de Potenciais Gargalos do Sistema
escrever aqui

### 13.2. Segunda Fase de Testes
#### 13.2.1. Otimização
escrever aqui

#### 13.2.2. Medições `(Refaça os Testes de Carga após otimização)`
escrever aqui

#### 13.2.3. Resultados Comparativos `(Gráficos e Interpretação)`
escrever aqui e imagem aqui

#### 13.2.4. Conclusão dos Testes
escrever aqui
