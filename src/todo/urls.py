from django.urls import path
from .views import home, todo_create, todo_list, todo_update

urlpatterns = [
    path('home/', home, name='home'),
    path('list/', todo_list, name='todo-list'),
    path('add/', todo_create, name='todo-create'),
    path('<int:id>/update/', todo_update, name='todo-update'),
]
