from django.urls import path
from . import views

urlpatterns = [
    path('', views.DetailsView.as_view(), name="tasks_details"),
    path('update/<int:id>/', views.TaskUpdateView.as_view(), name="tasks_update"),
    path('delete/<int:id>/', views.TaskDeleteView.as_view(), name="tasks_delete"),
    path('tasks/list/api/', views.TaskListView.as_view(), name='tasks_list_api'),
    path('tasks/details/api/<int:pk>/', views.TaskDetailsView.as_view(), name='tasks_details_api'),
]
