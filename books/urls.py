from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import index, create_book, show_book, delete_book, show_author

urlpatterns = [
    path('', index, name="index"),
    path('books/create/', create_book, name="create_book"),
    path('books/delete/<int:book_id>', delete_book, name="create_book"),
    path('books/<int:book_id>/', show_book, name="book_details"),
    path('authors/<int:author_id>/', show_author, name="author_details")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
