from django.db import models


class TextFile(models.Model):
    name = models.CharField('Имя файла', max_length=30)
    file = models.FileField('Загрузить файл')

    objects = models.Manager()

    class Meta:
        verbose_name = 'Текстовый файл'
        verbose_name_plural = 'Текстовые файлы'

    def __str__(self):
        return self.name



