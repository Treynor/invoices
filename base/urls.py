from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('add/', views.add, name="add"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('<int:id>/', views.invoice, name="invoice"),
    path('update/<str:id>/', views.update, name="update_invoice"),
]


