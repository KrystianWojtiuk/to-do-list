from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, RedirectView
from .models import Task, Tag
from .forms import TaskForm, TagForm


# TASKS
class TaskListView(ListView):
    model = Task
    template_name = "todo/task_list.html"
    context_object_name = "tasks"
    ordering = ["completed", "-created_at"]

    def get_queryset(self):
        return (
            Task.objects.all()
            .prefetch_related("tags")   # fetch all tags in one query
            .order_by("completed", "-created_at")
        )


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo/task_form.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo/confirm_delete.html"
    success_url = reverse_lazy("task_list")


class TaskToggleCompleteView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        task = Task.objects.get(pk=kwargs["pk"])
        task.completed = not task.completed
        task.save()
        return reverse_lazy("task_list")


# TAGS
class TagListView(ListView):
    model = Tag
    template_name = "todo/tag_list.html"
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("tag_list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = "todo/tag_form.html"
    success_url = reverse_lazy("tag_list")


class TagDeleteView(DeleteView):
    model = Tag
    template_name = "todo/confirm_delete.html"
    success_url = reverse_lazy("tag_list")
