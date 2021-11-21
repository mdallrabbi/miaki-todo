from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('todo-list/', views.todoList, name="todo-list"),
    path('todo-detail/<str:pk>/', views.todoDetail, name="todo-Detail"),
    path('todo-update/<str:pk>/', views.todoUpdate, name="todo-update"),
    path('todo-create/', views.todoCreate, name="task-Create"),
    path('task-delete/', views.todoDelete, name="task-delete"),

]
