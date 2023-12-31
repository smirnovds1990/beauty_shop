# Generated by Django 4.2.4 on 2023-08-05 21:18

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_master_specialty'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='procedure',
            options={'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AddField(
            model_name='procedure',
            name='duration',
            field=models.DurationField(blank=True, null=True, verbose_name='Продолжительность'),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='price',
            field=models.CharField(max_length=200, verbose_name='Стоимость (Руб.)'),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='title',
            field=models.CharField(max_length=200, unique=True, verbose_name='Услуга'),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Клиент')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('procedure', models.ManyToManyField(db_table='cutomer_procedures', related_name='procedures', to='registration.procedure', verbose_name='Услуга')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
