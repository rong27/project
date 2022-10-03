from django.urls import path
from app_userkey_sentiment import views

app_name="app_userkey_sentiment"

urlpatterns = [
    # For the user userkey sentiment analysis page
    path('', views.home, name='home'),
    path('api_get_userkey_sentiment/', views.api_get_userkey_sentiment),
]
