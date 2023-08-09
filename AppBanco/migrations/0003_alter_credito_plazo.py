# Generated by Django 4.1.7 on 2023-05-16 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppBanco', '0002_lineascredito_credito'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credito',
            name='Plazo',
            field=models.PositiveSmallIntegerField(choices=[(6, 6), (12, 12), (18, 18), (4, 24)], default=6, verbose_name='Plazo'),
        ),
    ]
