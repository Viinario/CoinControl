# CoinControl

## Descrição do Projeto

**CoinControl** é uma aplicação web desenvolvida com o objetivo de demonstrar as diversas possibilidades oferecidas por uma arquitetura de microserviços aplicada ao gerenciamento de criptomoedas. A plataforma permite que os usuários façam login, gerenciem suas carteiras de criptomoedas e realizem conversões de moedas digitais em tempo real, tudo isso de maneira modular e escalável. 

Este projeto serve como uma vitrine para o uso de microserviços em um sistema financeiro, enfatizando a flexibilidade, segurança e capacidade de expansão que essa arquitetura oferece.

## Funcionalidades

- **Sistema de Login e Sessão**: Cada usuário pode criar sua própria sessão, com informações de login e senha armazenadas de forma segura através de hashes criptografados.
- **Gerenciamento de Carteiras**: Os usuários podem adicionar, remover e visualizar suas criptomoedas em tempo real. 
- **Conversão de Criptomoedas**: Microserviço dedicado para conversões entre Bitcoin e Ethereum, com possibilidade de expansão para outras moedas.
- **Histórico de Sessão**: Informações sobre a carteira do usuário são salvas durante a sessão ativa, permitindo continuidade nas operações até o logout.
- **Microserviço de Portfólio**: Rastreamento e visualização do valor do portfólio do usuário em tempo real, com possibilidade de exibição de gráficos sobre o crescimento ou variação dos ativos.
- **Segurança**: Todos os dados sensíveis, como e-mails e senhas, são armazenados de maneira segura e encriptada.

## Estrutura do Projeto

O projeto está dividido em microserviços independentes, cada um responsável por uma funcionalidade específica da aplicação. Isso torna o CoinControl altamente modular, facilitando a manutenção, adição de novas funcionalidades e escalabilidade. Os principais componentes incluem:

- **Microserviço de Autenticação**: Responsável por verificar as credenciais do usuário e gerenciar sessões.
- **Microserviço de Portfólio**: Gerencia as transações e o saldo das criptomoedas de cada usuário.
- **Microserviço de Conversão**: Fornece a funcionalidade de conversão entre diferentes criptomoedas.
- **Interface de Frontend**: Fornece uma interface interativa para que os usuários possam visualizar suas carteiras e realizar conversões.

## Tecnologias Utilizadas

- **Node.js**: Ambiente de execução para o backend e microserviços.
- **Express.js**: Framework utilizado para construir a API REST que suporta o sistema de microserviços.
- **SCSS**: Utilizado para o design e estilização do frontend.
- **JSON**: Armazenamento de dados de sessões e usuários.
- **Criptografia**: Hashing seguro para senhas e proteção de dados sensíveis.
  
## Possibilidades de Expansão

Este projeto foi projetado para ser facilmente extensível. Novos microserviços podem ser adicionados para suportar diferentes funcionalidades, como:

- **Suporte para novas criptomoedas**: Expandir a plataforma para incluir conversões entre outras moedas digitais.
- **Notificações em tempo real**: Adicionar um sistema de notificações para informar o usuário sobre mudanças nos preços de criptomoedas.
- **Integração com exchanges**: Conectar a plataforma com exchanges de criptomoedas para realizar transações reais.

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues, sugerir melhorias ou submeter pull requests para evoluir o projeto.
