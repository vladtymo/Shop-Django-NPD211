from django.urls import path

from products import views

urlpatterns = [
    path('home/', views.home),
    path('list/', views.index),
    path('details/<int:id>', views.details)
]
