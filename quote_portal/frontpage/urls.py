from django.urls import path
from . import views

urlpatterns = [path('frontpage/', views.frontpage_start, name='frontpage')]

