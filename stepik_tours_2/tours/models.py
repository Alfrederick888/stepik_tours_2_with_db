from django.contrib.gis.geoip2.resources import City
from django.db import models
from django.urls import reverse


class Cards(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название отеля')
    description = models.TextField(blank=True, verbose_name='Описание отеля')
    departure = models.CharField(max_length=10, verbose_name='Страна отправки')
    picture = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')
    price = models.IntegerField(verbose_name='Цена')
    stars = models.CharField(max_length=2, verbose_name='Оценка')
    country = models.CharField(max_length=50, verbose_name='Страна прибытия')
    nights = models.IntegerField(verbose_name='Количество ночей')
    date = models.CharField(max_length=50,verbose_name='Дата отправки')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    # cit = models.ForeignKey('City', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('cards', kwargs={'cards_id': self.pk})

    class Meta:
        verbose_name = 'Туры'
        verbose_name_plural = 'Туры'
        ordering = ['title', 'departure']

# class City(models.Model):
#     name = models.CharField(max_length=100, db_index=True)
#
#     def __str__(self):
#         return self.name
