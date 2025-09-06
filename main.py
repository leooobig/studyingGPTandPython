from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
MY_KEY_OPENAI = os.getenv("MY_KEY_OPENAI")

cliente = OpenAI(api_key=os.getenv("MY_KEY_OPENAI"))

response = cliente.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "Listar apenas os nomes dos produtos, sem considerar a descrição."
        },
        {
            "role": "user",
            "content" : "Liste 3 produtos sustentáveis."
    
        },
    ],
    model="gpt-4"
)

print(response.choices[0].message.content)
