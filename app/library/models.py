from django.db import models
from django.urls import reverse


class Author(models.Model):
    """Авторы"""
    name = models.CharField("Имя", max_length=120)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Genre(models.Model):
    """Жанры"""
    name = models.CharField('Название', max_length=100)
    url = models.SlugField('Ссылка', max_length=160, unique=True, default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Book(models.Model):
    """Книги"""
    title = models.CharField('Название', max_length=120)
    author = models.ManyToManyField(Author, max_length=120)
    description = models.TextField('Описание', max_length=8000)
    poster = models.ImageField('Постер', upload_to='static/books/', default='static/img/book.jpg')
    year = models.PositiveSmallIntegerField('Издание', default="0000")
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
