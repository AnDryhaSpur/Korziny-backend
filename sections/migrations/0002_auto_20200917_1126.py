# Generated by Django 2.0.10 on 2020-09-17 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sections', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='header',
            new_name='h1',
        ),
        migrations.AddField(
            model_name='page',
            name='image',
            field=models.ImageField(default='Нет изображения', upload_to='img'),
        ),
    ]
