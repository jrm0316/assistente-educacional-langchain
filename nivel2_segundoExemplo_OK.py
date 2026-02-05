# assistente-educacional-langchain
from dotenv import load_dotenv # Carrega o arquivo .env; É assim que o LC acha sua GROQ_API_KEY; Sem isso, nada funciona.
load_dotenv()

from langchain_groq import ChatGroq # Conecta com a IA da Groq
from langchain_core.prompts import PromptTemplate # Cria perguntas dinâmicas

# Criamos o modelo de IA
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0
)

# Criamos um template de prompt
prompt = PromptTemplate(
    input_variables=["tema", "nível"], # {tema} e {nível} são espaços em branco; depois você preenche eles com dados reais. Isso é o coração do LC.
    template = "Explique {tema} para um nível {nível}, com exemplos simples."
)

# Conectamos o prompt ao modelo (LCEL)
chain = prompt | llm # | significa: pega o texto do prompt e joga dentro do modelo 

# Executamos a chain pasasndo os valores
resposta = chain.invoke({
    "tema": "Python", # preenche {tema} -> Python
    "nível": "iniciante" # preenche {nível} -> iniciante
})

# Mostramos apenas o texto da resposta
print(resposta.content)