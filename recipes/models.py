from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

from slugify import UniqueSlugify
from stdimage import StdImageField

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


class Recipe(models.Model):
    title = models.CharField('Название рецепта', max_length=255)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Автор рецепта'
    )
    image = StdImageField(
        upload_to='recipes/',
        blank=True,
        variations={
            'large': (480, 480),
            'thumbnail': (100, 100, True),
            'medium': (364, 240), },
        delete_orphans=True
    )
    text = models.TextField('Текст рецепта')
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ингредиент'
    )
    cooking_time = models.PositiveSmallIntegerField('Время приготовления, мин.')
    slug = models.SlugField(
        max_length=255,
        blank=True,
        null=True
    )
    tags = models.ManyToManyField(
        'Tag',
        related_name='recipes',
        verbose_name='Теги'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        ordering = ('-pub_date',)
        verbose_name = 'рецепт'
        verbose_name_plural = 'рецепты'

    def save(self, *args, **kwargs):
        if not self.slug:
            slugify_unique = UniqueSlugify(separator='-', to_lower=True)
            self.slug = slugify_unique(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients_amounts'
    )
    quantity = models.DecimalField(
        max_digits=6,
        decimal_places=1,
        validators=[MinValueValidator(1)]
    )

    class Meta:
        unique_together = ('ingredient', 'recipe')


class Tag(models.Model):
    COLORS = (
        ('green', 'Зеленый'),
        ('orange', 'Оранжевый'),
        ('purple', 'Пурпурный')
    )
    title = models.CharField('Имя тега', max_length=50, db_index=True)
    display_name = models.CharField('Имя тега для шаблона', max_length=50)
    color = models.CharField('Цвет тега', max_length=50, choices=COLORS)

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.title
