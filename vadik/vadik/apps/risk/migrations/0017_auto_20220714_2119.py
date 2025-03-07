# Generated by Django 4.0.6 on 2022-07-14 14:19

from django.db import migrations
import django_db_constraints.operations


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0016_rename_страна_employee_country_id_and_more'),
    ]

    operations = [
        django_db_constraints.operations.AlterConstraints(
            name='country',
            db_constraints={'prime_risk': 'check ((type_risk <= 3) and (type_risk >= 0))'},
        ),
        django_db_constraints.operations.AlterConstraints(
            name='valuta',
            db_constraints={'prime_risk': 'check ((type_risk <= 3) and (type_risk >= 0))'},
        ),
    ]
