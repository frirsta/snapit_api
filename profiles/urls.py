from django.urls import path
from profiles import views


urlpatterns = [
    path('profiles/', views.UserList.as_view()),
    path('profile/<int:pk>', views.UserDetails.as_view()),
]
