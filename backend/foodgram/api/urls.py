from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

app_name = 'api'

router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='users')
router.register(r'tags', views.TagsViewset, basename='tags')
router.register(r'ingredients', views.IngredientsViewSet,
                basename='Ingredients')
router.register(r'recipes', views.RecipesViewSet, basename='recipes')
router.register(
    r'ingredients', views.IngredientsViewSet, basename='ingredients')

urlpatterns = [
    path(r'auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls)),
]
