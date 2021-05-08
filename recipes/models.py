from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Ingredient(models.Model):
    title = models.CharField(
        'Название ингредиента',
        max_length=255,
        db_index=True
    )
    dimension = models.CharField('Единица измерения', max_length=10)

    class Meta:
        ordering = ('title', )
        verbose_name = 'ингредиент'
        verbose_name_plural = 'ингредиенты'

    def __str__(self):
        return f'{self.title}, {self.dimension}'
