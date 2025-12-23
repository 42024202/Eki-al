from django.urls import path
from apps.favorites.views import (
    FavoriteListView,
    FavoriteAddView,
    FavoriteRemoveView,
    FavoriteDetailView,
)   


urlpatterns = [    
    path('', FavoriteListView.as_view(), name='favorite_list'),
    path('add/', FavoriteAddView.as_view(), name='favorite_add'),
    path('<int:pk>/', FavoriteDetailView.as_view(), name='favorite_detail'),
    path('<int:pk>/remove/', FavoriteRemoveView.as_view(), name='favorite_remove'),
]
