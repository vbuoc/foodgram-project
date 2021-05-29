from django import forms

from recipes.models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'title',
            'tags',
            'cooking_time',
            'text',
            'image',
        )
        widgets = {
            'tags': forms.CheckboxSelectMultiple(
                attrs={'class': 'tags__checkbox'}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        # подменяем валидацию для "PositiveSmallIntegerField"
        self.fields['cooking_time'].validators[0].limit_value = 1

        for key, value in self.data.items():
            if 'valueIngredient' in key and int(value) <= 0:
                num = key.split('_')[1]
                name_ingredient = self.data[f'nameIngredient_{num}']
                self.add_error(
                    None,
                    f'Количество ингредиента "{name_ingredient}" должно быть больше 0.'
                )
