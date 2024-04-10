from django.db import models
from . import choices, services


# Create your models here.
class Users(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    fisrt_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    otc = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return f'{self.last_name} {self.fisrt_name} {self.otc}'


class Level(models.Model):
    winter = models.CharField(choices=choices.LEVELS, max_length=3, default='n/d')
    spring = models.CharField(choices=choices.LEVELS, max_length=3, default='n/d')
    summer = models.CharField(choices=choices.LEVELS, max_length=3, default='n/d')
    autumn = models.CharField(choices=choices.LEVELS, max_length=3, default='n/d')

    class Meta:
        verbose_name = 'Уровень сложности'
        verbose_name_plural = 'Уровени сложности'


class Coords(models.Model):
    latitude = models.FloatField(blank=True)
    longtitude = models.FloatField(blank=True)
    height = models.IntegerField(blank=True)

    class Meta:
        verbose_name = 'Координаты'
        verbose_name_plural = 'Координаты'


class Pass(models.Model):
    status = models.CharField(choices=choices.STATUS, max_length=9, default='new')
    beauty_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    other_titles = models.CharField(max_length=255, blank=True)
    connect = models.CharField(max_length=255)
    add_time = models.DateTimeField(auto_now_add=True)
    coord = models.OneToOneField(Coords, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    level = models.OneToOneField(Level, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Перевал'
        verbose_name_plural = 'Перевалы'

    def __str__(self):
        return f'{self.id} {self.beauty_title} {self.title}'


class Images(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to=services.upload_path, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    rel_pass = models.ForeignKey(Pass, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.title}'
