from flask import Flask, render_template, request, redirect, url_for

from repositories import book_repository, author_repository

from flask import Blueprint

books_blueprint = Blueprint("books", __name__)

#GET '/books'
@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template("/books/index.html", books = books)

#POST '/books/<id>/delete'
@books_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect(url_for('.books'))

#GET '/books/new'
   