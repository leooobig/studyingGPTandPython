from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
MY_KEY_OPENAI = os.getenv("MY_KEY_OPENAI")

cliente = OpenAI(api_key=os.getenv("MY_KEY_OPENAI"))

def categorizador(produto:str):
    response = cliente.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": """
                Categorize o produto abaixo em uma das seguintes categorias:
                Higiene Pessoal, Moda, Casa, etc
                e de uma descrição para o produto, e faça de uma maneira que uma
                descrição não seja igual a do produto anterior.
                Para cada produto sempre mantenha a primeira categoria.
                """
            },
            {
                "role": "user",
                "content" : f"""
                {produto}
                """
            },
        ],
        model="gpt-5-nano",
        n = 3
    )
    
    for i in range(len(response.choices)):
        print(f"Reposta {i+1}: ")
        print(response.choices[i].message.content)
        print()

    