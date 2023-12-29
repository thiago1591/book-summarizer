from utils import *
import os

book_content = read_txt("output/book_summary.txt")
chapters_number = book_content.count("#CAPÍTULO")

book_name = input("qual é o nome do livro?: ")

res = create_notion_page(book_name, os.getenv('PAGE_ID'), None)
parent_page = res.json()
parent_page_id = parent_page['id']

for i in range(chapters_number):
    print("Enviando capítulo " + str(i+1) + "...")
    chapter_content = find_chapter_after_summarized(book_content, i)
    children = format_text_for_notion(chapter_content)
    chapter_title = get_chapter_title(chapter_content)
    res = create_notion_page(chapter_title, parent_page_id , children)




