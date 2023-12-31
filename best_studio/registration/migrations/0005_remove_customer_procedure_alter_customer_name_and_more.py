# Generated by Django 4.2.4 on 2023-08-12 14:23

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0004_alter_procedure_options_procedure_duration_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='procedure',
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(help_text='Введите имя в формате <Имя Фамилия>', max_length=200, verbose_name='Клиент'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(help_text='Введите номер в формате +79801234567', max_length=128, region=None, verbose_name='Номер телефона'),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='master',
            field=models.ManyToManyField(db_table='master_procedures', related_name='procedures', to='registration.master', verbose_name='Специалист'),
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Дата и время')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='registration.customer', verbose_name='Клиент')),
                ('master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='registration.master', verbose_name='Специалист')),
                ('procedure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='registration.procedure', verbose_name='Услуга')),
            ],
        ),
    ]
