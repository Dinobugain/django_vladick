# Generated by Django 4.0.6 on 2022-07-11 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0004_country_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='born_date',
            field=models.DateField(verbose_name='Дата рождения'),
        ),
    ]
