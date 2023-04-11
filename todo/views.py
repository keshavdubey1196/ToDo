from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Task
from django.urls import reverse_lazy

# Create your views here.


class TaskList(ListView):
    model = Task
    context_object_name = "tasklist"
    template_name = "todo/tasks.html"


class TaskDetail(DetailView):
    model = Task
    context_object_name = "task"
    template_name = "todo/task.html"


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = reverse_lazy("tasks")
