# Generated by Django 3.2 on 2024-05-23 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20240523_2128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Предложение', 'verbose_name_plural': 'Предложения'},
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(max_length=2000, verbose_name='Текст'),
        ),
    ]
