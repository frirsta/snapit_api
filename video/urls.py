from django.urls import path
from video import views


urlpatterns = [
    path('video/', views.VideoList.as_view()),
    path('video/<int:pk>', views.VideoDetails.as_view()),
]
