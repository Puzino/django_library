from django.views.generic import ListView, DetailView
from .models import Book, Genre


class GetGenres():
    def get_genres(self):
        return Genre.objects.all()


class HomeLibraryView(GetGenres, ListView):
    model = Book
    template_name = 'index.html'
    context_object_name = 'books'


class BookDetail(GetGenres, DetailView):
    model = Book
    template_name = 'book_detail.html'


# class FilterBook(GetGenres, ListView):
#
#
#     def get_queryset(self):
#         query_set = Book.objects.filter(genres=2)
#
#         print(query_set)
#         return query_set
