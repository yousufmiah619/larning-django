from django.urls import path
from . import views 

urlpatterns = [
    path('add-task', views.add_task, name='add_task'),
    path('mark_done/<int:task_id>/', views.mark_as_done, name='mark_as_done'),
    path('mark_undone/<int:task_id>/', views.mark_as_undone, name='mark_as_undone'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
]