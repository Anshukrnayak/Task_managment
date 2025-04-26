from django.urls import path
from . import views

urlpatterns=[
    path('task-list/',views.TaskApiList.as_view(),name='api')
]