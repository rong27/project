from django.urls import path
from app_leaderboard import views

app_name = 'app_leaderboard'

urlpatterns = [
    path('', views.pk_nation, name = 'nation'),
    path('politicalparty', views.pk_political_party, name ='politicalParty'),
]
