# Generated by Django 3.0.5 on 2020-04-11 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Tarih'),
        ),
    ]
