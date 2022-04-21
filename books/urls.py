from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from .views import index, show_book, show_author

urlpatterns = [
    path('', index),
    path('books/<int:book_id>/', show_book),
    path('authors/<int:author_id>/', show_author)
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
