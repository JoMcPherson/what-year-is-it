from django.urls import path
from .views import headlines, welcome_user

urlpatterns = [
    path("game/", headlines, name="year_headlines"),
    path("home/", welcome_user, name="home"),
]
