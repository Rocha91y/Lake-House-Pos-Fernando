# pos-graduacao-lakehouse-fernando-rocha
# Lakehouse-dataops-pos-graduacao
Projeto educacional de Lakehouse na AWS com DataOps e CI/CD

🎯 Objetivo do Projeto Este projeto tem como objetivo demonstrar, na prática: A construção de um Lakehouse na AWS A aplicação da cultura DataOps O uso de CI/CD para pipelines de dados A organização de dados em camadas (Legado, Raw, Trusted e Curated) A entrega de produtos de dados analíticos prontos para BI O projeto utiliza como fonte inicial um arquivo Excel local, simulando um cenário comum de dados legados em empresas.

🏗️ Arquitetura Geral do Lakehouse O Lakehouse será implementado no Amazon S3 com a seguinte organização lógica: pos-graduacao-lakehouse

├── lakehouse-legado

├── lakehouse-raw

├── lakehouse-trusted

└── lakehouse-curated

Cada camada possui um papel específico dentro do ciclo de vida do dado.

📚 Camadas do Lakehouse

🔹 lakehouse-legado - Representa a origem dos dados Contém apenas o arquivo Excel original Upload realizado via pipeline local (VS Code) Nenhuma transformação aplicada

🔹 lakehouse-raw - Armazena o dado bruto com histórico completo

Cada execução gera uma nova versão do arquivo

Registro de timestamp de ingestão

Permite auditoria e reprocessamento

🔹 lakehouse-trusted

Dados padronizados e confiáveis

Conversão para Parquet

Tipos de dados corrigidos

Particionamento por DataEmissao (ano/mês/dia)

Base para consumo analítico

🔹 lakehouse-curated

Camada de consumo analítico

Implementada via CTAS (CREATE TABLE AS SELECT) no Athena

Dados agregados e otimizados

Entregas da Curated neste projeto:

Faturamento por Ano

Faturamento por Vendedor

Quantidade de Vendas por Vendedor

🔄 Processo ELT

O projeto segue o modelo ELT (Extract, Load, Transform):

Extract Extração do arquivo Excel local

Load Carga do dado bruto no S3 (camadas Legado e Raw)

Transform Padronização, agregações e otimizações nas camadas Trusted e Curated

🧠 Cultura DataOps Aplicada

Desde o início, o projeto adota práticas de DataOps:

Versionamento de código com Git

Organização padronizada de pipelines

Separação clara de responsabilidades

Rastreabilidade de alterações

Preparação para automação com CI/CD

Dados tratados como produtos

🔁 CI/CD no Projeto

O repositório Git será utilizado como base para automação:

CI (Continuous Integration)

Validação de código

Testes de qualidade de dados

Validação de SQL

CD (Continuous Deployment)

Deploy controlado de pipelines

Execução de CTAS no Athena

Auditoria e logs automáticos

lakehouse-dataops-pos-graduacao/

├── etl/

│├── legado_to_raw/

│├── raw_to_trusted/

│└── trusted_to_curated/

├── sql/

│└── curated_ctas/

├── tests/

├── docs/

└── README.md

🛠️ Tecnologias Utilizadas AWS

Amazon S3

AWS Glue

AWS Glue Data Catalog

Amazon Athena

AWS IAM

AWS Lake Formation

Amazon CloudWatch

AWS CloudTrail

DataOps & CI/CD

Git / GitHub

CodePipeline / CodeBuild (ou equivalente)

Pytest

Validações de schema e dados

📌 Público-alvo

Estudantes de pós-graduação

Engenheiros de Dados em formação

Profissionais de BI e Analytics

Times que desejam entender DataOps na prática

🚀 Próximas Etapas do Projeto

Fase 4 – Segurança, IAM e Governança

Fase 5 – Ingestão do dado Legado

Fase 6 – Camada Trusted

Fase 7 – Camada Curated com CTAS

Fase 8 – CI/CD em ação

Fase 9 – Observabilidade e Operação

📖 Observação Final Este projeto foi desenhado para ser didático, progressivo e alinhado com práticas reais de mercado, permitindo evolução futura para Machine Learning, streaming e arquiteturas mais avançadas.
Projeto Educacional de Lakehouse na AWS com DataOps e CI/CD
