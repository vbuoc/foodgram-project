from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from recipes.models import Ingredient
from api.models import Favorite, Subscription


class CustomModelSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return self.Meta.model.objects.create(**validated_data)


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('title', 'dimension')
        model = Ingredient


class FavoriteSerializer(CustomModelSerializer):
    class Meta:
        fields = ('recipe', )
        model = Favorite


class SubscriptionSerializer(CustomModelSerializer):
    class Meta:
        fields = ('author', )
        model = Subscription

    def validate_author(self, value):
        user = self.context['request'].user
        if user.id == value:
            raise ValidationError('Подписаться на себя конечно можно!'
                                  'Но зачем?')
        return value
