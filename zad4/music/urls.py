from django.urls import path
from . import views
urlpatterns = [
    path('', views.LandingPage),

    path('api/music/', views.ReturnMusic)
]