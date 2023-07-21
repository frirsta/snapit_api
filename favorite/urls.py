from django.urls import path
from favorite import views

urlpatterns = [
    path('favorite/', views.FavoriteList.as_view()),
    path('favorite/<int:pk>', views.FavoriteDetail.as_view()),
]
