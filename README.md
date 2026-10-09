# 100 Days of Python — Exercícios e Projetos

Este repositório reúne exercícios e projetos que desenvolvi durante o curso **100 Days of Python**, ministrado por Angela Yu. Organizei o conteúdo por dia e tema para registrar minha evolução no aprendizado de Python e facilitar a consulta aos códigos.

O repositório contém projetos independentes — não é uma única aplicação que possa ser executada de uma só vez. Os tópicos e projetos variam de acordo com cada pasta.

## Conteúdos estudados

Ao longo dos exercícios, pratiquei conceitos e ferramentas como:

- **Fundamentos de Python:** variáveis, tipos de dados, condicionais, loops, funções, listas, dicionários, escopo e compreensão de listas.
- **Programação orientada a objetos (POO):** classes, objetos, estado e organização do código.
- **Arquivos e dados:** leitura e escrita de arquivos, CSV, JSON e introdução ao Pandas.
- **Interfaces gráficas:** projetos com Turtle e Tkinter.
- **APIs e integrações:** consumo de APIs, parâmetros, autenticação, variáveis de ambiente e envio de requisições.
- **Automação e web scraping:** Beautiful Soup, Selenium e automação de tarefas no navegador.
- **Desenvolvimento web:** HTML, CSS, Bootstrap, Flask, templates com Jinja e formulários.
- **Bancos de dados e aplicações web:** SQLite, rotas RESTful e autenticação em aplicações Flask.

## Alguns projetos do repositório

Abaixo estão alguns exemplos para explorar. Cada link abre a pasta correspondente; consulte os arquivos dentro dela para ver a implementação e os requisitos específicos.

| Dia | Projeto ou tema | O que pratiquei |
|---|---|---|
| [Dia 07](./Day%2007%20-%20Beginner%20-%20Hangman) | Hangman | Lógica de programação e controle de fluxo. |
| [Dia 11](./Day%2011%20-%20Beginner%20-%20The%20Blackjack%20Capstone%20Project) | Blackjack | Combinação de funções, condicionais e regras de um jogo. |
| [Dia 23](./Day%2023%20-%20Intermediate%20-%20The%20Turtle%20Crossing%20Capstone%20Project) | Turtle Crossing | Lógica de jogo e organização do código com objetos. |
| [Dia 28](./Day%2028%20-%20Intermediate%20-%20Tkinter%20Dynamic%20Typing%20and%20the%20Pomodoro%20GUI%20Application) | Pomodoro | Interface gráfica e temporizador com Tkinter. |
| [Dia 29](./Day%2029%20-%20Intermediate%20-%20Building%20a%20Password%20Manager%20GUI%20App%20with%20Tkinter) | Password Manager | Interface gráfica e gerenciamento de informações. |
| [Dia 33](./Day%2033%20-%20Intermediate+%20API%20Endpoints%20&%20API%20Parameters%20-%20ISS%20Overhead%20Notifier) | ISS Overhead Notifier | Consumo de API e lógica baseada em dados externos. |
| [Dia 39](./Day%2039%20-%20Intermediate+%20Capstone%20Flight%20Deal%20Finder) | Flight Deal Finder | Integração com serviços externos para buscar ofertas de voos. |
| [Dia 45](./Day%2045%20-%20Intermediate+%20Web%20Scraping%20with%20Beautiful%20Soup) | Web Scraping | Extração de informações de páginas web com Beautiful Soup. |
| [Dia 48](./Day%2048%20-%20Intermediate+%20Selenium%20Webdriver%20Browser%20and%20Game%20Playing%20Bot) | Automação com Selenium | Interação automatizada com o navegador. |
| [Dia 53](./Day%2053%20-%20Intermediate+%20Web%20Scraping%20Capstone%20-%20Data%20Entry%20Job%20Automation) | Data Entry Automation | Combinação de web scraping e automação de preenchimento de dados. |
| [Dia 64](./Day%2064%20-%20Advanced%20-%20My%20Top%2010%20Movies%20Website) | My Top 10 Movies Website | Aplicação web para apresentar e gerenciar informações de filmes. |
| [Dia 66](./Day%2066%20-%20Advanced%20-%20Building%20Your%20Own%20API%20With%20RESTful%20Routing) | API RESTful | Criação de rotas para uma API web. |
| [Dia 68](./Day%2068%20-%20Advanced%20-%20Authentication%20with%20Flask) | Autenticação com Flask | Conceitos de autenticação em aplicações web. |
| [Dia 69](./Day%2069%20-%20Advanced%20-%20Blog%20Capstone%20Project%20Part%204%20-%20Adding%20Users) | Blog com usuários | Evolução de uma aplicação Flask com funcionalidades de usuários. |

> Os projetos são exercícios de estudo. Para saber o escopo exato de cada implementação, consulte o código da respectiva pasta.

## Como explorar e executar os projetos

Como cada pasta contém um exercício ou projeto independente, os passos de execução podem variar:

1. Abra a pasta do dia que deseja explorar.
2. Leia os comentários e os arquivos Python para entender o funcionamento.
3. Verifique se a pasta possui um `README`, `requirements.txt` ou outro arquivo com instruções específicas.
4. Se houver um `requirements.txt` naquela pasta, crie e ative um ambiente virtual e instale as dependências listadas.
5. Execute o arquivo principal indicado pelos próprios arquivos ou pelas instruções daquele projeto.

Exemplo de criação de ambiente virtual a partir do diretório do projeto:

```bash
python -m venv .venv
```

Ativar no Linux/macOS:

```bash
source .venv/bin/activate
```

Ativar no Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Instale dependências somente quando houver um arquivo de requisitos para o projeto:

```bash
python -m pip install -r requirements.txt
```

Alguns exercícios podem depender de serviços externos, credenciais ou chaves de API. Consulte os arquivos antes de executar e configure esses valores localmente conforme necessário.

## Segurança

- Não adicione senhas, tokens, chaves de API ou credenciais pessoais ao repositório.
- Quando um projeto exigir segredos, prefira variáveis de ambiente e mantenha arquivos `.env` fora do controle de versão.
- Confira os termos de uso e as permissões necessárias antes de reutilizar serviços externos ou automatizar ações em sites de terceiros.

## Sobre o curso

Este repositório é um registro pessoal de estudos e implementações práticas realizadas durante o curso de Angela Yu. Não é um repositório oficial do curso nem é afiliado à instrutora ou à plataforma de ensino.

## Autor

**Fellipe de Oliveira**

- GitHub: [@FellipeO](https://github.com/FellipeO)
- LinkedIn: [fellipe-oliveira](https://www.linkedin.com/in/fellipe-oliveira-127652293/)
