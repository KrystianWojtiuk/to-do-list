from django.urls import path
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskToggleCompleteView,
    TagListView, TagCreateView, TagUpdateView, TagDeleteView
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task_list"),

    # Tasks
    path("tasks/new/", TaskCreateView.as_view(), name="task_create"),
    path("tasks/<int:pk>/edit/", TaskUpdateView.as_view(), name="task_update"),
    path("tasks/<int:pk>/delete/", TaskDeleteView.as_view(), name="task_delete"),
    path("tasks/<int:pk>/toggle/", TaskToggleCompleteView.as_view(), name="task_toggle_complete"),

    # Tags
    path("tags/", TagListView.as_view(), name="tag_list"),
    path("tags/new/", TagCreateView.as_view(), name="tag_create"),
    path("tags/<int:pk>/edit/", TagUpdateView.as_view(), name="tag_update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag_delete"),
]