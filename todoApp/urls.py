from django.urls import path
from . import views

app_name = 'todoApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('add_list/', views.add_list, name='add_list'),
    path('add_task/<int:list_id>/', views.add_task, name='add_task'),
    path('complete_task/<int:task_id>/', views.complete_task, name='complete_task'),
]
