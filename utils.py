import json
import requests
import os
from dotenv import load_dotenv

load_dotenv()

def find_chapter(book_content, index):
    start_index = book_content.find(f"capitulo{index+1}")
    end_index = book_content.find(f"capitulo{index+2}")

    if end_index == -1:
        return book_content[start_index:].strip()

    return book_content[start_index:end_index].strip()

def find_chapter_after_summarized(book_content, index):
    start_index = book_content.find(f"#CAPÍTULO {index+1}")
    end_index = book_content.find(f"#CAPÍTULO {index+2}")

    if end_index == -1:
        return book_content[start_index:].strip()
    
    return book_content[start_index:end_index].strip()

def read_txt(file_name):
    with open(file_name, 'r') as file:
        content = file.read()
    return content

def read_json(file_name):
    with open(file_name, 'r') as file:
        json_data = json.load(file)
    return json_data

def write_txt(file_name, content):
    with open(file_name, 'w') as file:
        file.write(content)

def append_txt(file_name, context):
    with open(file_name, 'a') as file:
        file.write(context)

def find_chapters_name(path):
    with open(path, 'r') as arquivo:
        linhas = arquivo.readlines()
        for i, linha in enumerate(linhas):
            if 'capitulo' in linha.lower(): 
                if i + 1 < len(linhas):  
                    print(linhas[i + 1].strip())  

def format_text_for_notion(text):
    lines = text.split('\n')
    notion_formatted_text = []

    for line in lines:
        if line.startswith('- '):
            notion_formatted_text.append({
                "object": "block",
                "type": "bulleted_list_item",
                "bulleted_list_item": {
                   "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": line[2:],
                        "link": None
                    }
                    }],
                    "color": "default",
                }
            })
        elif line.strip() == '':
            continue
        else:
            notion_formatted_text.append({
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [{
                    "type": "text",
                    "text": {
                        "content": line,
                        "link": None
                    }
                    }],
                    "color": "default"
                }
            })

    return notion_formatted_text

def create_notion_page(pageTitle, parentId, children):
    create_url = "https://api.notion.com/v1/pages"

    headers = {
        "Authorization": "Bearer " + os.getenv('NOTION_TOKEN'),
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }

    payload = {
        "parent": {"page_id": parentId },
        "properties": {"title": [{"type": "text", "text": {"content": pageTitle}}]}
    }

    if children is not None:
        payload["children"] = children

    res = requests.post(create_url, headers=headers, json=payload)
    return res

def get_chapter_title(chapter):
    linhas = chapter.split('\n')  

    for linha in linhas:
        if "Título: " in linha:
            titulo = linha.replace("Título: ", "")  
            return titulo.strip() 

    return None