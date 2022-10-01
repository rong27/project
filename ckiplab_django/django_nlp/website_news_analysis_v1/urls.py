from django.urls import path
from django.urls import include

from app_top_keyword import views
#from app_top_keyword.views import bar_chart

urlpatterns = [
    path('', views.bar_chart),
    #path('', bar_chart),
]
