from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeLibraryView.as_view(), name='index'),
    # path('filter/<str:pk>/', views.FilterBook.as_view(), name='filter'),
    path('book/<int:pk>/', views.BookDetail.as_view(), name='book-detail'),
]
