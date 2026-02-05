# assistente-educacional-langchain

Assistente Educacional com LangChain e Groq
- Projeto em Python que demonstra o uso do LangChain para criar prompts reutilizáveis e dinâmicos, integrados a um LLM da Groq (LLaMA 3.1).
- O sistema gera explicações automáticas de conceitos técnicos com base em tema e nível de conhecimento, utilizando LCEL (LangChain Expression Language).

Objetivo do Projeto
Demonstrar, de forma prática, como:
- Criar prompts parametrizados com PromptTemplate
- Separar lógica de código e texto
- Utilizar LCEL para conectar prompts a modelos de linguagem
- Construir uma base reutilizável para assistentes educacionais, chatbots ou copilotos técnicos
Este projeto vai além de uma simples chamada de API, aplicando boas práticas de arquitetura com LLMs.

Como funciona
Fluxo simplificado da aplicação:

Variáveis (tema, nível)
        ↓
PromptTemplate (LangChain)
        ↓
LCEL (prompt | llm)
        ↓
Modelo LLM (Groq - LLaMA 3.1)
        ↓
Resposta gerada pela IA

A IA não recebe código nem arquivos diretamente — ela recebe texto estruturado, montado dinamicamente pelo Python.

Tecnologias Utilizadas
- Python
- LangChain
- Groq
- LLaMA 3.1
- PromptTemplate
- LCEL (LangChain Expression Language)
- dotenv (.env)

Pré-requisitos
- Python 3.10+
- Conta na Groq
- Chave de API da Groq

Configuração do ambiente

1.) Clone o repositório:
    - git clone https://github.com/jrm0316/assistente-educacional-langchain.git
    - cd seu-repositorio

2.) Crie um arquivo .env:
    - GROQ_API_KEY=Sua_Chave_Aqui

3.) Instale as dependências:
    - pip install langchain langchain-groq python-dotenv

Executando o projeto
- python main.py

O código irá gerar automaticamente uma pergunta no formato:
“Explique Python para um nível iniciante, com exemplos simples.”
E exibirá a resposta da IA no terminal.

Conceitos Aplicados
- Prompt Engineering
- Prompts reutilizáveis
- Parametrização de entrada
- Arquitetura com LangChain
- Integração com LLMs
- Separação de lógica e texto

Aplicações práticas
Este padrão pode ser facilmente adaptado para:
- Assistentes educacionais
- Chatbots técnicos
- Copilotos internos
- Ferramentas de onboarding
- APIs baseadas em LLM

Observação
- Este projeto foi desenvolvido com foco em aprendizado prático de IA aplicada, seguindo padrões utilizados em aplicações reais com LLMs.

Autor
- Desenvolvido por Juliano Madeira
- Estudos focados em IA aplicada, backend e engenharia de prompts
