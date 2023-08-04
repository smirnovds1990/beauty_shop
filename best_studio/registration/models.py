from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Master(models.Model):
    """Мастер, оказывающий услуги."""
    name = models.CharField(
        verbose_name='Специалист', max_length=200, unique=True
    )
    bio = models.TextField(verbose_name='О специалисте', blank=True, null=True)
    specialty = models.CharField(
        max_length=200, verbose_name='Специальность', blank=True, null=True
    )

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'

    def __str__(self):
        return self.name


class Procedure(models.Model):
    """Оказываемая процедура."""
    master = models.ManyToManyField(
        Master, verbose_name='Специалист', related_name='masters',
        db_table='master_procedures'
    )
    title = models.CharField(
        verbose_name='Процедура', max_length=200, unique=True
    )
    price = models.CharField(verbose_name='Стоимость (Руб.)', max_length=200)
    # duration = models.TimeField(verbose_name='Длительность')

    class Meta:
        verbose_name = 'Процедура'
        verbose_name_plural = 'Процедуры'

    def display_master(self):
        """Создай строку для отображения мастеров у процедур в админ панели."""
        return ', '.join([master.name for master in self.master.all()])
    display_master.short_description = 'Специалист'

    def __str__(self):
        return self.title
