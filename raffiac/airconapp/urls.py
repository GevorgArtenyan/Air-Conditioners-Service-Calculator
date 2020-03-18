from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home, name='home'),
    path('result/', views.result, name='result'),
    path('api/', views.ModelAPIListView.as_view(), name='model-list'),
]
