# Generated by Django 3.2.8 on 2021-11-22 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='attributes',
            index_together={('id', 'slug')},
        ),
    ]
