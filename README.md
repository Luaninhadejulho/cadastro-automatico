## Automação de Cadastro de Clientes com Python

Este projeto demonstra como automatizar o preenchimento de um formulário online com base em dados armazenados em uma planilha Excel, utilizando `pandas` para leitura dos dados e `pyautogui` para simular ações humanas (como clicar, digitar e pressionar teclas).

## Objetivo

Automatizar a entrada de dados de clientes em um sistema web, simulando o processo manual feito por um atendente. Ideal para cenários repetitivos como cadastros de pedidos, formulários internos ou integrações sem API.

## Tecnologias Utilizadas

- [Python 3.13](https://www.python.org/)
- [pandas](https://pandas.pydata.org/) – para leitura e manipulação da planilha
- [pyautogui](https://pyautogui.readthedocs.io/) – para automação da interface gráfica
- [openpyxl](https://openpyxl.readthedocs.io/) – suporte à leitura de arquivos Excel `.xlsx`

## Estrutura do Projeto

cadastro-automatico/
├─ cadastro_automatico_clientes.py # Script principal de automação
├─ gerar_excel.py # (Opcional) Gera o Excel com dados fictícios
├─ clientes.xlsx # Planilha de clientes com até 5 registros
└─ README.md # Você está aqui :)

## Como funciona

1. O script lê os dados da planilha `clientes.xlsx`
2. Abre automaticamente o navegador
3. Acessa a URL da empresa fictícia
4. Preenche os campos de cadastro com os dados de cada cliente
5. Pressiona "Enter" ou clica em "Cadastrar"
6. Repete até terminar todos os registros


## Importante

> **Este projeto utiliza `pyautogui`, que depende da posição dos elementos na tela.**  
> A automação pode não funcionar corretamente em outras resoluções, layouts ou sistemas diferentes.  
> Por isso, este repositório é voltado para fins **educacionais** e **portfólio**, e não para execução universal.


## Exemplo de planilha (`clientes.xlsx`)

| Código Produto | Nome completo do cliente | Produto    | Valor unitário | Quantidade pedida | Valor Total da Compra |
|----------------|---------------------------|------------|----------------|--------------------|------------------------|
| CP001          | Ana Souza                 | Mouse      | 35.00          | 1                  | 35.00                  |
| CP002          | Bruno Lima                | Teclado    | 120.00         | 2                  | 240.00                 |
| CP003          | Carlos Meireles           | Monitor    | 950.00         | 1                  | 950.00                 |
| CP004          | Daniela Rocha             | Impressora | 560.00         | 1                  | 560.00                 |
| CP005          | Eduarda Gomes             | Webcam     | 150.00         | 3                  | 450.00                 |


## Como executar

1. Instale as bibliotecas:
```bash
pip install pandas openpyxl pyautogui

Projeto desenvolvido por Luana Alves como parte do seu portfólio em automação de tarefas com Python.
Fique à vontade para conhecer mais projetos no meu perfil: github.com/Luaninhadejulho
