# Generated by Django 3.2.2 on 2021-05-16 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(choices=[('green', 'Зеленый'), ('orange', 'Оранжевый'), ('purple', 'Пурпурный')], max_length=50, verbose_name='Цвет тега'),
        ),
    ]
