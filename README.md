[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

[contributors-shield]: https://img.shields.io/github/contributors/J-o-n-a-s/LerArquivoExecutaSQL.svg?style=for-the-badge
[contributors-url]: https://github.com/J-o-n-a-s/LerArquivoExecutaSQL/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/J-o-n-a-s/LerArquivoExecutaSQL.svg?style=for-the-badge
[forks-url]: https://github.com/J-o-n-a-s/LerArquivoExecutaSQL/network/members
[stars-shield]: https://img.shields.io/github/stars/J-o-n-a-s/LerArquivoExecutaSQL.svg?style=for-the-badge
[stars-url]: https://github.com/J-o-n-a-s/LerArquivoExecutaSQL/stargazers
[issues-shield]: https://img.shields.io/github/issues/J-o-n-a-s/LerArquivoExecutaSQL.svg?style=for-the-badge
[issues-url]: https://github.com/J-o-n-a-s/LerArquivoExecutaSQL/issues
[license-shield]: https://img.shields.io/github/license/J-o-n-a-s/LerArquivoExecutaSQL.svg?style=for-the-badge
[license-url]: https://github.com/J-o-n-a-s/LerArquivoExecutaSQL/blob/master/LICENSE

# Projeto desenvolvido para coletar informações de arquivos SQL e inserir em banco de dados SQL Server

**SEJA BEM-VINDO A ESTE REPOSITÓRIO!!!**

------------

Note que este é o meu terceiro projeto em Python e o terceiro compartilhado no GitHub. Cada dia que passa eu aprendo um pouco mais sobre o Python e assim irei melhorando o código do programa.

**Instruções**

 - *Fork* este repositório;
 - Clone seu repositório *forked*;
 - Adicione seus scripts;
 - *Commit & Push*;
 - Crie um *pull request*;
 - Dê uma estrela para este repositório;
 - Aguarde que o seu *pull request* solicitado vire um *merge*;
 - Comemore, seu primeiro passo para o mundo de código aberto e continue contribuindo.

## Introdução

A ideia desse projeto é automatizar a leitura de um arquivo com comandos SQL (Structured Query Language). Pegar linha a linha desses comandos e executá-los. Porém, antes de executar os comandos SQL das linhas, será necessário realizar a conexão no banco de dados SQL Server com a base de dados correta.

O que foi citado acima é um resumo das funcionalidades deste projeto.

## Motivação

Eu recebi um arquivo SQL. Porém esse arquivo continha mais de 11 milhões de comandos SQL e mais de 9 GB. Até tentei abrir no SSMS (SQL Server Management Studio), mas sem sucesso. O SSMS informou que não continha memória o suficiente para abertura e execução de um arquivo tão grande. Para não ter que quebrar esse arquivo em diversos arquivos e executá-los um a um, eu decidi que seria benéfico criar um programa em Python que pudesse realizar essa ativadade por mim.

Por esse motivo, que eu iniciei essa aplicação em Python.

## Descrição do projeto

1. Realizada a importação das bibliotecas;
2. Criação de função para conexão com o banco de dados;
3. Função de tratativa de erros (ainda necessário a finalização);
4. Iniciado o programa principal com criação de variável e definicão dos seus valores iniciais;
5. Impressão de informações sobre o que se refere o projeto;
6. Impressão dos passos / comandos que o usuário precisará interagir com o programa (dentre eles o caminho do arquivo SQL e se deseja visualizar o log ou não);
7. Abertura do arquivo SQL com o caminho informado pelo usuário;
8. Conexão com o banco de dados SQL Server e base de dados específica;
9. Tratativa e informação para o usuário no caso de erro ou sucesso na abertura do arquivo e conexão com banco de dados;
10. Em caso de insucesso, finaliza o programa informando o ocorrido ao usuário;
11. Em caso de sucesso, realiza a leitura linha a linha do arquivo SQL e executa os comandos;
12. Ao final da leitura do arquivo será apresentado um resumo do desempenho do programa (quantidade de linhas do arquivo, linhas executadas, linhas em branco ou não executadas e tempo de execução do programa).

 ## Instalação e execução do projeto

 ...

 ## Bibliotecas e recursos utilizados

 - sys
 - time
 - pyodbc

 ## Licença

 ...
