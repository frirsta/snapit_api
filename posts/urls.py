from django.urls import path
from posts import views


urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('post/<int:pk>', views.PostDetails.as_view()),
    
]
