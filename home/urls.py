from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name="home"),
    path('about-us/', views.about, name=("about")),
    path('services/', views.service, name=("services"))
]