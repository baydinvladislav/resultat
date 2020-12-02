from django.db import models
from django.urls import reverse


class Document(models.Model):
    """Model of uploaded database's file"""
    name = models.CharField(max_length=255, blank=True, verbose_name='Название базы данных')
    document = models.FileField(upload_to='documents/', verbose_name='Файл')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('read_data', kwargs={'db_id': self.id})


class Table(models.Model):
    """Table template for filling with the received data from CSV"""
    document = models.ForeignKey(
        Document, 
        verbose_name='Имя загруженного файла', 
        related_name='projects', 
        on_delete=models.CASCADE,
    )
    number = models.IntegerField('Номер',)
    date = models.DateField('Дата',)
    project = models.CharField('Название проекта', max_length=5,)
    price = models.IntegerField('Стоимость',)
    available_numbers = models.IntegerField('Всего номеров получено',)
    used = models.IntegerField('Номеров использовано',)
    remainder = models.IntegerField('Остаток',)
    source = models.CharField('Источник', max_length=50,)
    how_collected = models.CharField('Способ получения', max_length=255,)
    responsible = models.CharField('Ответственный', max_length=255,)
    link = models.CharField('Ссылка', max_length=255,)
    status = models.CharField('Статус',max_length=5, blank=True,)
    comment = models.CharField('Комментарий',max_length=255, blank=True,)
    price_per_number = models.FloatField('Цена за каждый номер',)

    def __str__(self):
        return self.project
