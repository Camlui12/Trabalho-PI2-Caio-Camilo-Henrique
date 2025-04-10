# 1. Introdução
escrever aqui

# 2. Visão Geral do Produto
### 2.1. Minimundo
O sistema de gerenciamento de estacionamento tem o objetivo de informatizar e automatizar as operações de controle de entrada e saída de veículos em um estacionamento privado. Atualmente, essas operações são feitas de forma manual, o que pode gerar erros e dificultar o controle financeiro e operacional.

O sistema permite o registro da entrada e saída de veículos, armazenando informações como placa, modelo, cor e horário de entrada/saída. Com base no tempo de permanência, o sistema calcula automaticamente o valor a ser pago pelo cliente do estacionamento, considerando regras pré-definidas de tarifação (por exemplo, tarifa por hora ou frações).

Além disso, o sistema oferece funcionalidades para consultar o histórico de veículos que utilizaram o estacionamento, emitir relatórios financeiros, e de lotação. Também será possível cadastrar planos mensais para clientes fixos, permitindo o gerenciamento de mensalistas.

O objetivo principal do sistema é otimizar o processo de controle de veículos, reduzir erros humanos, melhorar a condição de trabalho dos funcionários e fornecer relatórios precisos para o administrador do estacionamento.


### 2.2. Delimitação do Escopo inicial
escrever aqui

# 3. Atores (Usuários) e Envolvidos
### a. Atores Principais
+ Administrador
+ Funcionários

### b. Atores secundários (se houver)
escrever aqui

### c. Envolvidos (não utilizarão o sistema, e apenas se houver)
+ Carros

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
| RN07 | Cobrança diária máxima |  |

### 4.2. Requisitos Funcionais.
| N° | Nome | Descrição |
|:-------|:-----|:----------|
| RF01 | Título | Descrição |

### 4.3. Requisitos Não-Funcionais.
| N° | Nome | Descrição |
|:-------|:-----|:----------|
| RNF01 | Título | Descrição |

# 5. Casos de Uso
### 5.1. Diagrama de Caso de Uso
Imagem aqui

### 5.2. Descrição dos Casos de Uso
| UC01 - Título do Caso de Uso |
|:-----------------------------|
| 1.1. Identificador |
| 1.2. Título |
| 1.3. Atores |
| 1.4. Objetivo |
| 1.5. Pré-Condições |
| 1.6. Pós-Condições |
| 1.7. Trigger |
| 1.8. Fluxo Básico |
| 1.9. Fluxo alternativo |
| 1.10. Fluxo de Exceção |
| 1.11. Referências Cruzadas (Requisitos Associados) |

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
