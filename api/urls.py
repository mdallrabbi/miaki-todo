from django.urls import path
from . import views

urlpatterns = [
    path('', views.Overview, name="overview"),
    path('list/', views.List, name="todoList"),
    path('detail/<str:pk>/', views.Detail, name="detail"),
    path('update/<str:pk>/', views.Update, name="update"),
    path('create/', views.Create, name="create"),
    path('delete/', views.Delete, name="delete"),

]
