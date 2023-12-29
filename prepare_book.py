from utils import find_chapter, write_txt, read_txt
import json
import os

book_content = read_txt("book/book.txt")

chapters_number = book_content.count("capitulo")

if not os.path.exists("book/chapters"):
    os.makedirs("book/chapters")

for i in range(chapters_number):
    chapter_content = find_chapter(book_content, i)

    chapter_filename = f"book/chapters/{i+1}.txt"

    write_txt(chapter_filename, chapter_content)