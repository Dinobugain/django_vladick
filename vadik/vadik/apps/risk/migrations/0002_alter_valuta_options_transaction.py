# Generated by Django 4.0.6 on 2022-07-11 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('risk', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='valuta',
            options={'verbose_name': 'Валюта', 'verbose_name_plural': 'Валюты'},
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='Сумма перевода')),
                ('level_risk', models.CharField(default='', max_length=10, null=True, verbose_name='Уровень риска')),
                ('type_valuta_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='risk.valuta')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Транзакция',
                'verbose_name_plural': 'Транзакции',
            },
        ),
    ]