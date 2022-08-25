import requests
from django.core.management.base import BaseCommand
import datetime

from django_films.models import Movie


class Command(BaseCommand):
    help = 'Parse Privatbank archive rates'  # noqa: A003, VNE003

    def handle(self, *args, **options):
        head = {
            'X-API-KEY': '538d2c9d-0ff2-449a-a865-613e7f96d144',
            'Content-Type': 'application/json',
        }
        for i in range(300, 310):
            url = f'https://kinopoiskapiunofficial.tech/api/v2.2/films/{i}'

            response = requests.get(url, headers=head).json()

            nameRu = response['nameRu']
            nameOriginal = response['nameOriginal']
            posterUrl = response['posterUrl']
            poster_get = requests.get(posterUrl)
            poster_name = "".join(nameOriginal.split())
            poster_down = open(f'C:/Users/admin/Documents/django_films/media/movies/{poster_name}.jpg', 'wb')
            poster_down.write(poster_get.content)
            poster_down.close()
            poster_path = 'movies/' + poster_name + '.jpg'
            year = response['year']
            description = response['description']
            slogan = response['slogan']
            countries = response['countries'][0]['country']

            try:
                Movie.objects.get(
                    title=nameRu,
                    title_ru=nameRu,
                    title_en=nameOriginal,

                    tagline=slogan,
                    tagline_ru=slogan,
                    tagline_en=slogan,

                    description=description,
                    description_ru=description,
                    description_en=description,

                    poster=poster_path,
                    year=year,
                    county=countries,
                    county_ru=countries,
                    county_en=countries,

                    world_premiere=datetime.date(2023, 12, 12),
                    budget=0,
                    fees_in_usa=0,
                    fees_in_world=0,
                    category_id=1,

                    url=poster_name.lower().replace("'", ''),
                    draft=False,
                )
                print(f'Взят фильм {nameRu}')
            except Movie.DoesNotExist:
                Movie.objects.create(
                    title=nameRu,
                    title_ru=nameRu,
                    title_en=nameOriginal,

                    tagline=slogan,
                    tagline_ru=slogan,
                    tagline_en=slogan,

                    description=description,
                    description_ru=description,
                    description_en=description,

                    poster=poster_path,
                    year=year,
                    county=countries,
                    county_ru=countries,
                    county_en=countries,

                    world_premiere=datetime.date(2023, 12, 12),
                    budget=0,
                    fees_in_usa=0,
                    fees_in_world=0,
                    category_id=1,

                    url=poster_name.lower().replace("'", ''),
                    draft=False,
                )
                print(f'Создан фильм: {nameRu}')
