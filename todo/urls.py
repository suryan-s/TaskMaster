
from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_todo, name='add_todo'),
    path('complete/<todo_id>', views.complete_todo, name='complete_todo'),
    path('delete/<todo_id>', views.delete, name='delete_todo'),
]
