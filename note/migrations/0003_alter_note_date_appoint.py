# Generated by Django 3.2.2 on 2021-05-12 18:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0002_auto_20210512_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='date_appoint',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
