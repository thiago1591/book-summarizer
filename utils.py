import json

def find_chapter(book_content, index):
    start_index = book_content.find(f"capitulo{index+1}")
    end_index = book_content.find(f"capitulo{index+2}")

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