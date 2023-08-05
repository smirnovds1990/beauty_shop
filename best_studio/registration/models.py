from django.contrib.auth import get_user_model
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()


class Master(models.Model):
    """Специалист, оказывающий услуги."""
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
        Master, verbose_name='Специалист', related_name='procedures',
        db_table='master_procedures'
    )
    title = models.CharField(
        verbose_name='Услуга', max_length=200, unique=True
    )
    price = models.CharField(verbose_name='Стоимость (Руб.)', max_length=200)
    duration = models.DurationField(
        blank=True, null=True, verbose_name='Продолжительность'
    )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def display_master(self):
        """Создай строку для отображения мастеров у процедур в админ панели."""
        return ', '.join([master.name for master in self.master.all()])
    display_master.short_description = 'Специалист'

    def __str__(self):
        return self.title


class Customer(models.Model):
    'Модель клиента.'
    name = models.CharField(
        verbose_name='Клиент', max_length=200,
        help_text='Введите имя в формате <Имя Фамилия>'
    )
    phone_number = PhoneNumberField(
        help_text='Введите номер в формате +79801234567',
        verbose_name='Номер телефона'
    )
    # procedure = models.ManyToManyField(
    #     Procedure, verbose_name='Услуга', related_name='customers',
    #     db_table='cutomer_procedures'
    # )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name
