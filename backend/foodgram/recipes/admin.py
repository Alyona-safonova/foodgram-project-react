from django.contrib import admin

from .models import (Favorite, Ingredient, IngredientInRecipe, Recipe,
                     ShoppingCart, Tag)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'color')
    empty_value_display = '-пусто-'


class RecipeIngredientInline(admin.StackedInline):
    model = IngredientInRecipe
    min_num = 1


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'id')
    readonly_fields = ('in_favorites',)
    list_filter = ('name', 'author', 'tags')
    empty_value_display = '-пусто-',
    inlines = (RecipeIngredientInline, )

    @admin.display(description='В избранном')
    def in_favorites(self, obj):
        return obj.favorite_recipe.count()


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)


class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount',)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe')


admin.site.register(Tag, TagAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientInRecipe, IngredientInRecipeAdmin)
admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(ShoppingCart, ShoppingCartAdmin)
