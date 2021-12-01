import pdb
from models.author import Author
from models.book import Book

import repositories.book_repository as book_repository
import repositories.author_repository as author_repository

author1 = Author("Steven King")
author_repository.save(author1)

book1 = Book("IT", 1986, "Horror", author1)
book_repository.save(book1)

author_results = author_repository.select_all()
book_results = book_repository.select_all()

for result in author_results:
    print(result.__dict__)

for result in book_results:
    print(result.__dict__)   