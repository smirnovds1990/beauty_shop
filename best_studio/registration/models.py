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
    """Модель клиента."""
    name = models.CharField(
        verbose_name='Клиент', max_length=200,
        help_text='Введите имя в формате <Имя Фамилия>'
    )
    phone_number = PhoneNumberField(
        help_text='Введите номер в формате +79801234567',
        verbose_name='Номер телефона'
    )

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.name


class Record(models.Model):
    """Запись на процедуру."""
    date = models.DateTimeField(verbose_name='Дата и время')
    master = models.ForeignKey(
        Master, on_delete=models.CASCADE, verbose_name='Специалист',
        related_name='records'
    )
    procedure = models.ForeignKey(
        Procedure, on_delete=models.CASCADE, verbose_name='Услуга',
        related_name='records'
    )
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, verbose_name='Клиент',
        related_name='records'
    )

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'

    def __str__(self):
        return self.name
