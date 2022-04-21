import os
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

from .models import Book, Author
from .forms import BookForm


# Create your views here.
def index(request):
    all_books = Book.objects.all()
    for book in all_books:
        book.cover = os.path.basename(book.cover_image.name)

    return render(request, "books/index.html", context={'books': all_books})


def create_book(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save()
            return redirect("book_details", book_id=book.id)
    elif request.method == "GET":
        form = BookForm()
    else:
        return HttpResponse("Method not allowed")

    return render(request, "books/book_form.html", context={"form": form})


def show_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.cover = os.path.basename(book.cover_image.name)
    return render(request, "books/book_details.html", context={'book': book})


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            book = form.save()
            return redirect("book_details", book_id=book.id)
    elif request.method == "GET":
        form = BookForm(instance=book)
    else:
        return HttpResponse("Method not allowed")

    return render(request, "books/book_form.html", context={"form": form})


def delete_book(request, book_id):
    if request.method == "POST":
        book = get_object_or_404(Book, id=book_id)
        book.delete()
        return redirect("index")
    else:
        return HttpResponse("Method not allowed")


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
