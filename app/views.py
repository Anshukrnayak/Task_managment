from django.db.models import Expression
from django.db.transaction import commit
from django.views import generic
from django.shortcuts import HttpResponse,redirect
from .models import  Task
from django.urls import reverse_lazy
from django.contrib.auth.models import  User
from .forms import TaskForm


class TaskListView(generic.ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = 'home/task-list.html'

    def get_queryset(self):
        return Task.objects.filter(author=self.request.user)

class TaskCreateView(generic.CreateView):
    form_class = TaskForm
    template_name = 'home/task_create.html'
    model = Task
    context_object_name = 'form'

    def form_valid(self, form):
        try:
            task=form.save(commit=False)
            task.author=self.request.user
            task.save()

            return super().form_valid(form)
        except Exception as e:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('task_list')

class TaskDetailView(generic.UpdateView):
    template_name = 'home/task_task_create.html'
    model = Task
    form_class = TaskForm
    context_object_name = 'form'
    success_url = reverse_lazy('task_list')


class TaskUpdateView(generic.UpdateView):
    template_name = 'home/task_create.html'
    model = Task
    form_class = TaskForm

    success_url = reverse_lazy('task_list')

class TaskDeleteView(generic.DeleteView):
    template_name = 'home/delete.html'
    model = Task
    success_url = reverse_lazy('task_list')



