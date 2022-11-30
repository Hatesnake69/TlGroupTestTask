from django.urls import path

from . import views

urlpatterns = [
    path('<uuid:subdivision_id>/', views.list_all_subdivision_elements),
    path('', views.index),
]
