from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
MY_KEY_OPENAI = os.getenv("MY_KEY_OPENAI")

cliente = OpenAI(api_key=os.getenv("MY_KEY_OPENAI"))

modelo = "gpt-5-nano"
promptSystem = f"""
        Você é um categorizador de produtos.
        Você deve assumir as categorias presentes na lista abaixo.

        # Lista de Categorias Válidas
            - Moda Sustentável
            - Produtos para o Lar
            - Beleza Natural
            - Eletrônicos Verdes

        # Formato da Saída
        Produto: Nome do Produto
        Categoria: apresente a categoria do produto

        # Exemplo de Saída
        Produto: Escova elétrica com recarga solar
        Categoria: Eletrônicos Verdes
    """

def getPromptUser():
    promptUser = str(input("Descreva o produto: "))
    os.system('cls')
    return promptUser

def categorizador():
    response = cliente.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": promptSystem,
            },
            {
                "role": "user",
                "content" : getPromptUser(),
            },
        ],
        model=modelo,
    )
    print(response.choices[0].message.content)

    