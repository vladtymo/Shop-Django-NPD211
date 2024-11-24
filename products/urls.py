from django.urls import path

from products import views

urlpatterns = [
    path('home/', views.home),
    path('details/<int:id>', views.details)
]
