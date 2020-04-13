# Generated by Django 3.0.5 on 2020-04-12 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_ad_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('url', models.URLField()),
            ],
        ),
    ]