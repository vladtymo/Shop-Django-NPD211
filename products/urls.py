from django.urls import path

from products import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', views.upload, name = 'create'),
    path('delete/<int:id>', views.delete, name = 'delete'),
]
