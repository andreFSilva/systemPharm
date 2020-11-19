from django.urls import path
from . import views


urlpatterns = [
    path('core/', views.Home.as_view(), name='home'),
]