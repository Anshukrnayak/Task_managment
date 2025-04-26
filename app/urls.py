from . import views
from django.urls import path


urlpatterns=[

    path('',views.TaskListView.as_view(),name='task_list'),
    path('task_create/',views.TaskCreateView.as_view(),name='task_create'),
    path('task-delete/<int:pk>/',views.TaskDeleteView.as_view(),name='delete_task'),
    path('task-update/<int:pk>/',views.TaskUpdateView.as_view(),name='update_task')


]