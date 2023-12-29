import os
from openai import OpenAI
from utils import read_txt, write_txt, append_txt
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv('OPENAI_SK')
)

first_option = input("Digite 1 para analisar o livro ou 2 para analisar um capítulo específico: ")
if(first_option == "2"):
    chapter_number = input("Digite o número do capítulo que deseja analisar: ")
    chapter = read_txt(f"book/chapters/{chapter_number}.txt")
    input_message = f"""
    Faça uma análise do texto abaixo destacando os pontos principais. A análise não deve ser nem muito longa nem muito curta
    No começo da sua resposta, inclua o título, seguindo o seguinte formato de exemplo -> Título: Esse é um exemplo
    O título está no começo do texto, não inclua a palavra capítulo e sua numeração, apenas a frase do título.
    Responda em português.  
    \n\n{chapter}"""
    chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": input_message,
        }
    ],
        model="gpt-4-1106-preview",
        #model="gpt-3.5-turbo-1106",
    )
    output = chat_completion.choices[0].message.content
    if not os.path.exists("output/chapters"):
        os.makedirs("output/chapters")
    write_txt(f"output/chapters/{chapter_number}.txt", output)
else: 
    number_chapters = len(os.listdir("book/chapters"))
    for i in range(number_chapters):
        chapter = read_txt(f"book/chapters/{i+1}.txt")
        input_message = f"""
            Faça uma análise do texto abaixo destacando os pontos principais. A análise não deve ser nem muito longa nem muito curta
            No começo da sua resposta, inclua o título, seguindo o seguinte formato de exemplo -> Título: Esse é um exemplo
            O título está no começo do texto, não inclua a palavra capítulo e sua numeração, apenas a frase do título.
            Responda em português.  
            \n\n{chapter}"""
        print(f"analizando capítulo {i+1}, aguarde...")
        chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input_message,
            }
        ],
            model="gpt-4-1106-preview",
            #model="gpt-3.5-turbo-1106",
        )
        output = chat_completion.choices[0].message.content
        append_txt(f"output/book_summary.txt", f"#CAPÍTULO {i+1}\n\n")
        append_txt(f"output/book_summary.txt", f"{output}\n\n")
    print("Análise concluída! Verifique o arquivo output/book_summary.txt")


