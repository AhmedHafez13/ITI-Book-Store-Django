from django.shortcuts import render
# from django.http import HttpResponse
from .models import Book, Author
import os


# Create your views here.
def index(request):
    all_books = Book.objects.all()
    for book in all_books:
        book.cover = os.path.basename(book.cover_image.name)

    return render(request, "books/index.html", context={'books': all_books})


def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.cover = os.path.basename(book.cover_image.name)
    return render(request, "books/book_details.html", context={'book': book})


def show_author(request, author_id):
    author = Author.objects.get(id=author_id)
    # print(author.book_set.all)
    books = author.book_set.all()
    for book in books:
        book.cover = os.path.basename(book.cover_image.name)
    return render(request, "books/author_details.html", context={
        'author': author,
        'books': books
    })
