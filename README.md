**PARTICIPANTES:** Caio Araújo, Camilo Lima e Henrique Rocha 

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
+ Clientes

# 4. Requisitos do sistema
### 4.1. Regras de Negócio.
| N° | Nome | Descrição |
|:-------|:-----|:----------|
| RN01 | Cobrança mínima | O estacionamento cobra um valor fixo mínimo correspondente à primeira hora, mesmo que o veículo permaneça menos tempo. | É permitido um período de tolerância de 10 minutos sem cobrança, desde que o veículo saia dentro desse tempo. |
| RN02 | Cobrança por fração de hora | Após a primeira hora, o valor é calculado por frações de 15 minutos. |
| RN03 | Tolerância gratuita de tempo | É permitido um período de tolerância de 10 minutos sem cobrança, desde que o veículo saia dentro desse tempo. |
| RN04 | Acesso de assinante mensal | Clientes que assinam o plano mensal têm direito a entrar e sair do estacionamento quantas vezes quiserem no mês. |
| RN05 | Limites de vagas por tipo de veículo | O estacionamento possui quantidade limitada de vagas para cada tipo de veículo. |
| RN06 | Desconto para horários noturnos | Entre 23h e 6h é aplicado um desconto de 30% na tarifa padrão. |
| RN07 | Cobrança diária máxima | Existe um valor máximo a ser cobrado por dia de permanência. |
| RN08 | Veículos com permanência superior a 12 horas | Se um veículo ultrapassar 12 horas de permanência, o valor é cobrado com base em diárias completas. |
| RN09 | Taxa extra por perda de ticket | Caso o cliente peca o ticket de entrada, será cobrada uma taxa fixa adicional. |
| RN10 | Descontos por fidelidade | O cliente receberá descontos com base na sua atividade mensal no estacionamento. |

### 4.2. Requisitos Funcionais.
| N° | Nome | Descrição |
|:-------|:-----|:----------|
| RF01 | Cadastro de veículo | O sistema deve permitir o cadastro de um novo veículo, registrando placa, modelo, cor e funcionário que realizou o cadastro caso ele não esteja presente no banco de dados. |
| RF02 | Registro de entrada de veículo | O sistema deve permitir o registro da entrada de um veículo já cadastrado, vinculando o horário atual, funcionario e dia ao respectivo registro do banco de dados. |
| RF03 | Cálculo de estadia | O sistema deve calcular o preço a ser pago por estadia do veículo no momento de saída dele, com base no horário e data de entrada e regras de cobrança. |
| RF04 | Horas de estadia | O sistema deve armazenar o tempo diário em horas que cada veículo permaneceu no estacionamento. |
| RF05 | Usuários | O sistema deve permitir o cadastro, edição e exclusão de usuários do sistema (operadores e administradores). |
| RF06 | Relatórios | O sistema deve permitir a emissão de relatórios de fluxo de veículos diária, semanal e mensal. Além de exibir as respectivas receitas. |
| RF07 | Planos mensais | O sistema deve permitir o cadastro de clientes mensalistas e calcular a cobrança conforme o plano. |
| RF08 | Ocupação | O sistema deve exibir a quantidade de vagas disponíveis por tipo de veículo. |
| RF09 | Configuração | O sistema deve permitir a configuração dos valores de tarifa, tolerância e teto diário pelo administrador. |


### 4.3. Requisitos Não-Funcionais.
| N° | Nome | Descrição |
|:-------|:-----|:----------|
| RNF01 | Acesso | O sistema deve ser acessível por meio de um navegador web (aplicação web responsiva). |
| RNF02 | Tempo de resposta | O tempo de resposta para registros de entrada ou saída não deve exceder 2 segundos. |
| RNF03 | Armazenamento | O sistema deve armazenar os dados em um banco de dados. |
| RNF04 | Usuários | Apenas usuários autenticados devem acessar o sistema. |
| RNF05 | Permissão | O sistema deve ter níveis de permissão distintos (ex: operador não pode acessar configurações administrativas). |
| RNF06 | UX | O sistema deve seguir boas práticas de usabilidade, com uma interface intuitiva. |
| RNF07 | Compatibilidade | O sistema deve ser compatível com os navegadores modernos (Chrome, Firefox, Edge). |
| RNF08 | Offline | O sistema deve permitir operação offline para registro de entradas/saídas, sincronizando quando a conexão voltar (opcional, mais avançado). |
| RNF09 | Capacidade | O sistema deve ser capaz de atender até 100 usuários simultâneos sem perda de desempenho. |

# 5. Casos de Uso
### 5.1. Diagrama de Caso de Uso
<img src="static/images/Diagrama_casos_de_uso.jpeg" alt="Diagrama de casos de uso" width="500px"/>

### 5.2. Descrição dos Casos de Uso
| Nome | Descrição |
|:-----|-----------|
| UC01 - Cadastrar Veículo | - **Atores**: Operador do estacionamento.<br>- **Objetivo**: Permitir que o operador cadastre um novo veículo no sistema, inserindo dados como placa, modelo, cor e tipo, quando o veículo ainda não estiver registrado no banco de dados.<br>- **Tipo do UC**: Primário<br>- **Pré-Condições**:O operador deve estar autenticado no sistema.<br>- **Pós-Condições**:O veículo fica registrado no banco de dados e disponível para futuras entradas.<br>- **Fluxo Básico**:<br>1. O operador acessa a funcionalidade de cadastro de veículo.<br>2. O sistema solicita os dados: placa, modelo, cor e tipo.<br>3. O operador preenche os dados.<br>4. O sistema verifica se a placa já existe.<br>5. Caso não exista, o sistema armazena os dados.<br>6. O sistema confirma o sucesso do cadastro.<br>- **Fluxo de Exceção**:<br>5a. Caso a placa já exista, o sistema exibe uma mensagem de erro e impede o cadastro.<br>- **Referências Cruzadas**: RF01, RN01 |
| UC02 - Registrar Entrada de Veículo | **Atores**: Operador do estacionamento.<br>**Objetivo**: Registrar a entrada de um veículo já cadastrado, vinculando o horário atual ao seu histórico para controle de permanência.<br>- **Tipo do UC**: Primário<br>- **Pré-Condições**:O veículo deve estar previamente cadastrado.<br>- **Pós-Condições**:O horário de entrada é salvo e associado ao veículo.<br>- **Fluxo Básico**:<br>1. O operador acessa a funcionalidade de registro de entrada.<br>2. Informa a placa do veículo.<br>3. O sistema verifica se o veículo está cadastrado.<br>4. O sistema armazena o horário atual como entrada.<br>5. O sistema confirma o registro.<br>- **Fluxo de Exceção**:<br>3a. Caso o veículo não esteja cadastrado, o sistema exibe uma mensagem de erro.<br>4a. Caso já exista uma entrada sem saída, o sistema bloqueia novo registro.<br>- **Referências Cruzadas**: RF02, RN02 |
| UC03 - Registrar Saída de Veículo | - **Atores**: Operador do estacionamento.<br>- **Objetivo**: Permitir o registro da saída de um veículo, calcular automaticamente o valor a ser pago com base no tempo de permanência e regras de tarifação.<br>- **Tipo do UC**: Primário<br>- **Pré-Condições**:O veículo deve estar com a entrada registrada.<br>- **Pós-Condições**:O horário de saída e valor pago são registrados.<br>- **Fluxo Básico**:<br>1. O operador acessa a funcionalidade de saída de veículo.<br>2. Informa a placa do veículo.<br>3. O sistema calcula o tempo de permanência.<br>4. O sistema aplica as regras de cobrança.<br>5. O valor é exibido ao operador.<br>6. O operador confirma a saída.<br>7. O sistema salva os dados.<br>- **Fluxo de Exceção**:<br>2a. Se não houver entrada registrada, o sistema informa erro.<br>- **Referências Cruzadas**: RF03, RN03 |
| UC04 - Consultar Frequência de Veículos | - **Atores**: Administrador.<br>- **Objetivo**: Exibir a quantidade de horas que um determinado veículo utilizou o estacionamento durante um período de tempo selecionado.<br>- **Tipo do UC**: Secundário<br>- **Pré-Condições**:Veículo com entradas e saídas registradas.<br>- **Pós-Condições**:Frequência consultada e exibida ao administrador.<br>- **Fluxo Básico**:<br>1. O administrador acessa o módulo de consulta de frequência.<br>2. Informa a placa do veículo e o período.<br>3. O sistema busca os registros.<br>4. Calcula o tempo total de permanência.<br>5. Exibe os dados ao administrador.<br>- **Referências Cruzadas**: RF04 |
| UC05 - Gerar Relatórios de Movimentação | - **Atores**: Administrador.<br>- **Objetivo**: Gerar relatórios sobre entradas, saídas e faturamento diário ou por período definido.<br>- **Tipo do UC**: Primário<br>- **Pré-Condições**:O sistema deve conter registros de movimentação.<br>- **Pós-Condições**:Relatório gerado e apresentado ou exportado.<br>- **Fluxo Básico**:<br>1. O administrador acessa a função de relatórios.<br>2. Define o tipo e período do relatório.<br>3. O sistema processa os dados e gera o relatório.<br>4. O relatório é exibido ou exportado.<br>- **Referências Cruzadas**: RF05, RN04 |
| UC06 - Cadastrar Usuário | - **Atores**: Administrador.<br>- **Objetivo**: Permitir o cadastro de novos usuários do sistema, atribuindo níveis de acesso (como operador ou administrador).<br>- **Tipo do UC**: Primário<br>- **Pré-Condições**: Administrador autenticado.<br>- **Pós-Condições**:Novo usuário cadastrado e disponível para acesso.<br>- **Fluxo Básico**:<br>1. O administrador acessa o módulo de usuários.<br>2. Preenche os dados do novo usuário.<br>3. Define o tipo de acesso.<br>4. O sistema salva os dados.<br>- **Referências Cruzadas**: RF06 |
| UC07 - Autenticar Usuário |- **Atores**: Operador, Administrador.<br>- **Objetivo**: Validar as credenciais de acesso do usuário ao sistema, liberando funcionalidades conforme seu nível de permissão.<br>- **Tipo do UC**: Primário<br>- **Pré-Condições**:Usuário registrado.<br>- **Pós-Condições**:Usuário autenticado com sessão ativa.<br>- **Fluxo Básico**:<br>1. O usuário acessa a tela de login.<br>2. Informa usuário e senha.<br>3. O sistema valida os dados.<br>4. Acesso concedido conforme o perfil.<br>- **Fluxo de Exceção**:<br>3a. Dados inválidos: o sistema exibe mensagem de erro.<br>- **Referências Cruzadas**: RF07, RN05 |
| UC08 - Configurar Regras de Cobrança | - **Atores**: Administrador.<br>- **Objetivo**: Permitir a configuração de valores de tarifa, tempo de tolerância e teto máximo diário.<br>- **Tipo do UC**: Secundário<br>- **Pré-Condições**: Administrador autenticado.<br>- **Pós-Condições**:Novas regras salvas e aplicadas nos cálculos.<br>- **Fluxo Básico**:<br>1. O administrador acessa o módulo de configurações.<br>2. Informa os novos valores de tarifa, tolerância e teto.<br>3. O sistema salva as configurações.<br>- **Referências Cruzadas**: RF08, RN06 |
| UC09 - Consultar Vagas Disponíveis | - **Atores**: Operador.<br>- **Objetivo**: Exibir em tempo real a quantidade de vagas disponíveis, separadas por tipo de veículo.<br>- **Tipo do UC**: Secundário<br>- **Pré-Condições**:Sistema com base de dados atualizada de entradas e saídas.<br>- **Pós-Condições**:Informações apresentadas ao operador.<br>- **Fluxo Básico**:<br>1. O operador acessa o painel de vagas.<br>2. O sistema exibe a quantidade de vagas livres por tipo de veículo.<br>- **Referências Cruzadas**: RF09 |

# 6. Diagrama de Classes
### 6.1. Diagrama
![Diagrama de classes](/static/images/Diagrama_de_classes.jpeg)

### 6.2. Descrição das Entidades
#### Classe: `Veiculo`
**Atributos:**
+ placa: String
+ modelo: String
+ cor: String
+ tipo: Enum (Carro, Moto, Utilitario, etc)

**Descrição:** Representa os veículos que acessam o estacionamento. Cada veículo é identificade unicamente pela placa.

**Relacionamentos:**
+ Associação com a classe `Estadia`: um veículo pode ter várias estadias.
+ Associação com a classe `ClienteMensalista`: um veículo pode estar associado a apenas um cliente mensalista.

---

### Classe: `Estadia`
**Atributos:**
+ id: Inteiro
+ dataHoraEntrada: DateTime
+ dataHoraSaida: DateTime
+ valorCobrado: Float

**Descrição:** Representa a permanência de um veículo no estacionamento. Os horários de esntrada e saída são usados para calcular o valor cobrado.

---

#### Classe: `Usuario`
**Atributos:**
+ id: Inteiro
+ nome: String
+ login: String
+ senha: String
+ tipo: Enum (Operador, Administrador)

**Descrição:** Representa os usuários que utilizam o sistema, podendo ser operadores ou administradores com permissões distintas.

---

#### Classe: `ConfiguracaoTarifa`
**Atributos:**
- id: Inteiro
- valorHora: Float
- toleranciaMinutos: Inteiro
- tetoDiario: Float
- dataVigencia: Date

**Descrição:** Armazena os parâmetros de cobrança do estacionamento. Apenas a configuração vigente na data da Estadia deve ser considerada para o cálculo do valor.

---

#### Classe: `ClienteMensalista`
**Atributos:**
- id: Inteiro
- nome: String
- cpf: String
- valorMensal: Float

**Descrição:** Representa clientes que utilizam planos mensais. A cobrança não é feita por estadia, mas sim por contrato fixo mensal.

**Relacionamentos:**
- Associação com `Veiculo`: cada cliente mensalista possui um veículo vinculado.

---

#### Classe: `Relatorio`
**Atributos:**
- id: Inteiro
- tipo: Enum (Diário, Semanal, Mensal)
- dataGeracao: DateTime
- conteudo: String

**Descrição:** Armazena relatórios gerados sobre fluxo de veículos e receitas.

# 7. Banco de Dados
### 7.1. Esquema Lógico de Banco de Dados Relacional
![Diagrama db](/static/images/Diagrama_banco_de_dados.jpeg)

### 7.2. Descrições
escrever aqui

### 7.3. Observações
escrever aqui

# 8. Projeto Arquitetural do Sistema
### 8.1. Diagrama de Alocação de Componentes
<img src="static/images/Diagrama_alocacao_componentes.jpeg" alt="Diagrama de alocação de componentes" width="500px"/>

# 9. Projeto Funcional do Sistema
### 9.1. Diagrama de Atividades
![Diagrama atividades](/static/images/Diagrama_atividades.jpeg)

### 9.2. Diagrama de Sequência
![Diagrama sequência](/static/images/Diagrama_sequencia.jpeg)

### 9.3. Diagrama de Estados
![Diagrama estados](/static/images/Diagrama_estados.jpeg)

# 10. Banco de Dados Relacional
### 10.1. Criação do Banco de Dados

#### SGBD Usado
**Nome**:MySQL
**Versão**: mysql  Ver 9.3.0 for macos15.2 on arm64 (Homebrew)

```sql
CREATE DATABASE estacionamento;
USE estacionamento;

-- Tabela USUARIO
CREATE TABLE Usuario (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    login VARCHAR(50) UNIQUE NOT NULL,
    senha VARCHAR(255) NOT NULL,
    tipo ENUM('Administrador', 'Operador') NOT NULL
);

-- Tabela RELATORIO
CREATE TABLE Relatorio (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tipo ENUM('Diário', 'Semanal', 'Mensal') NOT NULL,
    dataGeracao DATETIME NOT NULL,
    conteudo TEXT,
    vigenciaDias INT
);

-- Tabela TARIFA
CREATE TABLE Tarifa (
    id INT PRIMARY KEY AUTO_INCREMENT,
    valorHora DECIMAL(10,2) NOT NULL,
    toleranciaMinutos INT NOT NULL,
    tetoDiario DECIMAL(10,2) NOT NULL,
    dataVigencia DATE NOT NULL,
    id_admin INT NOT NULL,
    FOREIGN KEY (id_admin) REFERENCES Usuario(id)
);

-- Tabela VEICULO
CREATE TABLE Veiculo (
    placa VARCHAR(10) PRIMARY KEY,
    modelo VARCHAR(50),
    cor VARCHAR(30),
    tipo ENUM('Carro', 'Moto', 'Utilitário') NOT NULL
);

-- Tabela CLIENTE_MENSAL
CREATE TABLE ClienteMensal (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nome VARCHAR(100) NOT NULL,
    cpf VARCHAR(14) UNIQUE NOT NULL,
    valorMensal DECIMAL(10,2) NOT NULL
);

-- Tabela VEICULO_CLIENTE_MENSAL (associação N:1)
CREATE TABLE VeiculoClienteMensal (
    placa_veiculo VARCHAR(10) PRIMARY KEY,
    id_plano INT NOT NULL,
    FOREIGN KEY (placa_veiculo) REFERENCES Veiculo(placa),
    FOREIGN KEY (id_plano) REFERENCES ClienteMensal(id)
);

-- Tabela ESTADIA
CREATE TABLE Estadia (
    id INT PRIMARY KEY AUTO_INCREMENT,
    placa_veiculo VARCHAR(10) NOT NULL,
    id_tarifa INT NOT NULL,
    dataHoraEntrada DATETIME NOT NULL,
    dataHoraSaida DATETIME,
    valorCobrado DECIMAL(10,2),
    id_usuario INT NOT NULL,
    FOREIGN KEY (placa_veiculo) REFERENCES Veiculo(placa),
    FOREIGN KEY (id_tarifa) REFERENCES Tarifa(id),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id)
);

-- Tabela ESTADIA_RELATORIO (associação N:N)
CREATE TABLE EstadiaRelatorio (
    id_estadia INT NOT NULL,
    id_relatorio INT NOT NULL,
    PRIMARY KEY (id_estadia, id_relatorio),
    FOREIGN KEY (id_estadia) REFERENCES Estadia(id),
    FOREIGN KEY (id_relatorio) REFERENCES Relatorio(id)
);

-- Excluir a tabela PlanoMensal
DROP TABLE IF EXISTS PlanoMensal;

ALTER TABLE Usuario
ADD COLUMN id_admin INT,
ADD FOREIGN KEY (id_admin) REFERENCES Usuario(id);

ALTER TABLE Tarifa
ADD CONSTRAINT fk_id_admin_usuario FOREIGN KEY (id_admin) REFERENCES Usuario(id),
ADD CHECK (id_admin IS NOT NULL);
```

### 10.2. População inicial do banco
```sql
-- Usuários
INSERT INTO Usuario (nome, login, senha, tipo) VALUES 
('Carlos Silva', 'carlos', 'senha123', 'Administrador'),
('Fernanda Lima', 'fernanda', 'senha456', 'Operador'),
('Mariana Souza', 'mariana', 'senha789', 'Operador'),
('Lucas Rocha', 'lucas', 'senha321', 'Administrador'),
('Patrícia Gomes', 'patricia', 'senha654', 'Operador');

-- Atualiza id_admin nos usuários (exemplo de hierarquia)
UPDATE Usuario SET id_admin = 1 WHERE id IN (2, 3, 5);
UPDATE Usuario SET id_admin = 4 WHERE id = 4;

-- Tarifas
INSERT INTO Tarifa (valorHora, toleranciaMinutos, tetoDiario, dataVigencia, id_admin) VALUES 
(10.00, 15, 50.00, '2025-01-01', 1),  
(12.00, 10, 60.00, '2025-02-01', 4),  
(8.50, 20, 45.00, '2025-03-01', 1),   
(11.00, 15, 55.00, '2025-04-01', 4), 
(9.75, 10, 48.00, '2025-05-01', 1);

-- Veículos
INSERT INTO Veiculo (placa, modelo, cor, tipo) VALUES 
('ABC1234', 'Civic', 'Prata', 'Carro'),
('XYZ5678', 'Biz', 'Vermelha', 'Moto'),
('DEF3456', 'Corolla', 'Preto', 'Carro'),
('HIJ7890', 'Fazer 250', 'Azul', 'Moto'),
('LMN1122', 'HB20', 'Branco', 'Carro');

-- Clientes mensais
INSERT INTO ClienteMensal (nome, cpf, valorMensal) VALUES 
('João Almeida', '123.456.789-00', 200.00),    
('Ana Paula', '234.567.890-11', 220.00),       
('Bruno Costa', '345.678.901-22', 180.00),     
('Carla Mendes', '456.789.012-33', 250.00),     
('Diego Torres', '567.890.123-44', 190.00);  

-- Veículo de cliente mensal
INSERT INTO VeiculoClienteMensal (placa_veiculo, id_plano) VALUES 
('XYZ5678', 1),
('DEF3456', 2),
('HIJ7890', 3),
('LMN1122', 4),
('ABC1234', 5);

-- Estadias
INSERT INTO Estadia (placa_veiculo, id_tarifa, dataHoraEntrada, dataHoraSaida, valorCobrado, id_usuario) VALUES 
('ABC1234', 1, '2025-05-21 08:00:00', '2025-05-21 11:00:00', 30.00, 2),  
('XYZ5678', 1, '2025-05-21 09:00:00', '2025-05-21 09:30:00', 0.00, 2), 
('DEF3456', 2, '2025-05-22 08:30:00', '2025-05-22 10:30:00', 24.00, 3), 
('HIJ7890', 3, '2025-05-22 09:00:00', '2025-05-22 09:45:00', 0.00, 3), 
('LMN1122', 4, '2025-05-22 07:00:00', '2025-05-22 12:00:00', 48.00, 2);

-- Relatórios
INSERT INTO Relatorio (tipo, dataGeracao, conteudo, vigenciaDias) VALUES 
('Diário', '2025-05-21 18:00:00', 'Relatório do dia 21/05', 1),       
('Semanal', '2025-05-23 18:00:00', 'Relatório semanal', 7),          
('Mensal', '2025-05-01 18:00:00', 'Relatório mensal', 30),            
('Diário', '2025-05-22 18:00:00', 'Relatório do dia 22/05', 1),        
('Mensal', '2025-04-01 18:00:00', 'Relatório de Abril', 30); 

-- Associação Estadia-Relatório
INSERT INTO EstadiaRelatorio (id_estadia, id_relatorio) VALUES 
(1, 1),
(2, 1),
(3, 2),
(4, 3),
(5, 3);

```

# 11. Banco de Dados Não-Convencional
### CockroachDB v25.1
### 11.1. Diagrama do banco NewSQL
![Diagrama banco de dados NewSQl](/static/images/Diagrama_bd_newsql.jpg)

### 11.2. Criação e População do Banco de Dados
```python

# Criando tabelas
class TipoRelatorioEnum(enum.Enum):
    ANALITICO = 'analitico'
    SINTETICO = 'sintetico'
    COMPARATIVO = 'comparativo'

class MetricasUso(Base):
    __tablename__ = 'metricas_uso'

    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    acessos = Column(Integer)
    registros_entrada = Column(Integer)
    registros_saida = Column(Integer)
    relatorios_gerados = Column(Integer)

class LogPedidoRelatorio(Base):
    __tablename__ = 'log_pedido_relatorio'

    id_usuario = Column(Integer, primary_key=True)
    data_pedido = Column(Date, primary_key=True)
    tipo_relatorio = Column(Enum(TipoRelatorioEnum), nullable=False)

Base.metadata.create_all(engine)

#Inserindo dados
metricas = [
    MetricasUso(id=1, data=datetime.date(2025, 6, 1), acessos=120, registros_entrada=300, registros_saida=280, relatorios_gerados=10),
    MetricasUso(id=2, data=datetime.date(2025, 6, 2), acessos=90, registros_entrada=200, registros_saida=190, relatorios_gerados=7),
    MetricasUso(id=3, data=datetime.date(2025, 6, 3), acessos=150, registros_entrada=350, registros_saida=330, relatorios_gerados=12),
    MetricasUso(id=4, data=datetime.date(2025, 6, 4), acessos=80, registros_entrada=180, registros_saida=170, relatorios_gerados=5),
    MetricasUso(id=5, data=datetime.date(2025, 6, 5), acessos=110, registros_entrada=270, registros_saida=260, relatorios_gerados=8),
]

logs = [
    LogPedidoRelatorio(id_usuario=101, data_pedido=datetime.date(2025, 6, 1), tipo_relatorio=TipoRelatorioEnum.ANALITICO),
    LogPedidoRelatorio(id_usuario=102, data_pedido=datetime.date(2025, 6, 1), tipo_relatorio=TipoRelatorioEnum.SINTETICO),
    LogPedidoRelatorio(id_usuario=101, data_pedido=datetime.date(2025, 6, 2), tipo_relatorio=TipoRelatorioEnum.COMPARATIVO),
    LogPedidoRelatorio(id_usuario=103, data_pedido=datetime.date(2025, 6, 3), tipo_relatorio=TipoRelatorioEnum.ANALITICO),
    LogPedidoRelatorio(id_usuario=104, data_pedido=datetime.date(2025, 6, 4), tipo_relatorio=TipoRelatorioEnum.SINTETICO),
]

session.add_all(metricas + logs)
session.commit()
```

# 12. Implementação
escrever aqui

# 13. Testes de carga
### 13.1. Primeira Fase de Testes
#### 13.1.1. Medições

##### Teste 1
- Registro de Entrada de Veículo
- O serviço realiza principalmente operações de Leitura e Inserção.
    - Leitura: Ao tentar registrar uma entrada (/confirmarEntrada), o sistema primeiro realiza uma consulta no banco de dados para verificar se a placa       fornecida já pertence a um veículo cadastrado.
    - Inserção:
        1. Se o veículo não existe, os dados do novo veículo (placa, modelo, cor, tipo) são inseridos na tabela de veículos através do endpoint /cadastrarVeiculo.
        2. Uma vez que o veículo existe (seja por cadastro prévio ou pelo fluxo acima), uma nova linha é inserida na tabela de movimentações para registrar a data e hora da entrada, associada ao veículo correspondente.

- Arquivos envolvidos:
    - app.py
    - models.py
    - templates/registrar_entrada.html
    - templates/cadastrar_veiculo.html
    - templates/confirmar_entrada.html
  
- Arquivos com o código fonte de medição do SLA:
    - medicoes-sla/teste_sla_servico1.js
- Data da medição: 30/06/2025
- Descrição das configurações: Macbook Pro M3 macOS Sequoia 15.4.1 8gb
- 1 usuário virtual realizando 100 operações
- LEVANTAMENTO DE HIPÓTESES:
    - A análise dos resultados do teste aponta para um gargalo de desempenho claro e significativo, evidenciado pela grande disparidade de performance entre as operações: enquanto o cadastro de um novo veículo via POST /cadastrarVeiculo é extremamente rápido, com uma média de 5.4ms, o serviço principal de POST /confirmarEntrada apresenta uma performance muito inferior e inconsistente, com uma média de 177ms e picos que chegam a 533ms. Como essa lentidão foi observada com a carga de um único usuário, descarta-se a concorrência como causa, apontando a hipótese principal para a operação de escrita (INSERT) na tabela de relacionamento Movimentacao, que ocorre a cada confirmação de entrada. O gargalo é provavelmente causado pela falta de um índice de banco de dados otimizado para esta tabela, especialmente na coluna de chave estrangeira veiculo_id, forçando o sistema a realizar um trabalho de reorganização ineficiente a cada nova inserção. Conclui-se, portanto, que o sistema sofre de um gargalo de escrita que já se mostra severo e que se tornaria um ponto de falha crítico sob carga, sendo a implementação de índices na tabela Movimentacao a otimização fundamental para garantir a escalabilidade e a performance do serviço.
    
##### Teste 2
- Registro de Saída de Veículo
- O serviço realiza principalmente operações de Leitura e Atualização.
    1. Leitura: Ao acessar /registro-saida, o sistema faz uma leitura para renderizar a página HTML.
    2. Na rota /confirmarSaida, o sistema precisa primeiro ler o banco de dados para encontrar o veículo pela placa fornecida e, em seguida, localizar a sua movimentação de entrada que ainda está em aberto (ou seja, sem data de saída).
    - Atualização:
        - Após encontrar o registro de entrada em aberto, a principal ação do serviço é atualizar essa linha na tabela de movimentações. Isso envolve preencher a coluna data_saida com o horário atual e a coluna valor_pago com o custo calculado.

- Arquivos envolvidos:
    - app.py
    - models.py
    - templates/registro-saida.html
    - templates/confirmar_saida.html
  
- Arquivos com o código fonte de medição do SLA:
    - medicoes-sla/teste_sla_servico2.js
- Data da medição: 30/06/2025
- Descrição das configurações: Macbook Pro M3 macOS Sequoia 15.4.1 8gb
- 5 usuários virtuais realizando operações simultâneamente
- LEVANTAMENTO DE HIPÓTESES:
    - A análise dos resultados do segundo teste, que simulou uma carga de 5 usuários simultâneos por um minuto no serviço de "Registro de Saída", revela um severo gargalo de desempenho na operação principal. Enquanto o acesso à página de registro (GET /registro-saida) é extremamente rápido, com uma média de 6.18ms, a submissão da saída via POST /confirmarSaida apresenta uma latência crítica, com tempo médio de resposta de 937.66ms e picos que chegam a 1.2 segundos. A hipótese principal para esta lentidão é a combinação de uma consulta e uma atualização no banco de dados (SELECT e UPDATE na tabela Movimentacao) sob concorrência. Com múltiplos usuários tentando encontrar e atualizar registros simultaneamente, o sistema provavelmente enfrenta contenção de recursos, como bloqueios de linha (row locks) no banco de dados, forçando as operações a esperarem em fila. Adicionalmente, a consulta para encontrar a movimentação em aberto de um veículo pode ser ineficiente se não houver um índice otimizado para essa busca. Conclui-se que o serviço de saída não escala bem, pois uma carga moderada de 5 usuários já eleva o tempo de resposta a níveis inaceitáveis, indicando que a otimização da consulta e da transação de atualização na rota /confirmarSaida é fundamental.
 
#### 13.1.2. Resultados
##### Teste 1
<img src="static/images/k6 report_servico1.png" alt="teste1V1" width="1000px"/>

##### Teste 2
<img src="static/images/k6 report2.png" alt="teste2V1" width="1000px"/>
#### 13.1.3. Hipóteses de Potenciais Gargalos do Sistema
escrever aqui

### 13.2. Segunda Fase de Testes
#### 13.2.1. Otimização
Foram criados novos índices para as colunas consultadas nos cenários de teste e a otimização do código na rota 'cadastrarVeiculo' para melhorar o tempo de insert no BD. Acreditamos que essas mudanças melhorariam principalmente o tempo de insert e update no banco de dados pois isso era o que estava sendo mais custoso pelas nossas hipóteses. Os testes foram realizados da mesma maneira e ambiente para que haja uma comparação justa.

#### 13.2.2. Medições `(Refaça os Testes de Carga após otimização)`
escrever aqui

#### 13.2.3. Resultados Comparativos `(Gráficos e Interpretação)`
##### teste 1.2
<img src="static/images/k6 report1_2.png" alt="teste1V2" width="1000px"/>


##### teste 2.2
<img src="static/images/k6 report2_2.png" alt="teste2V2" width="1000px"/>

#### 13.2.4. Conclusão dos Testes
escrever aqui
