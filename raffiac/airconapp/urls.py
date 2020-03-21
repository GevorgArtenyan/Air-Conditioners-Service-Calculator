from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.ACServiceCalcListView.as_view(), name='calc_list'),
    path('add/', views.ACServiceCalcCreateView.as_view(), name='calc_add'),
    path('<int:pk>/', views.ACServiceCalcUpdateView.as_view(), name='calc_change'),
    path('ajax/load-models/', views.load_models, name='ajax_load_models'),  # <-- this one here
]