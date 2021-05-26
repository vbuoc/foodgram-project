import csv
import os

from django.core.management.base import BaseCommand
from foodgram.settings import BASE_DIR

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Import Ingredients from csv file'

    def handle(self, *admin, **options):
        file_path = os.path.join(BASE_DIR, 'ingredients.csv')
        with open(file_path) as file:
            reader = csv.reader(file)
            for row in reader:
                title, dimension = row
                Ingredient.objects.get_or_create(
                    title=title,
                    dimension=dimension
                )
