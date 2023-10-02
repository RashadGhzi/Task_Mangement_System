from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from .forms import TaskForm
from .models import Task
from rest_framework.decorators import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import TaskSerializer
from rest_framework import generics
from django.contrib import messages


class DetailsView(View):
    def get(self, request, pk=None):
        form = TaskForm(label_suffix="")
        task_objects = Task.objects.all()
        return render(request, 'tasks/details.html', {'form': form, 'task_objects': task_objects})

    def post(self, request, pk=None, *args, **kwargs):
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            task = form.save()  # Save the form and get the instance
            messages.success(request, "Data has been created.")
            return redirect('tasks_details')
        else:
            if request.POST.get('title') == "":
                messages.error(request, "All fields are required.")
            elif request.POST.get('description') == "":
                messages.error(request, "All fields are required.")
            elif request.POST.get('due_date') == "":
                messages.error(request, "All fields are required.")
            elif request.POST.get('priority') == "":
                messages.error(request, "All fields are required.")
            else:
                messages.error(request, "Please, Enter valid data.")
            return redirect('tasks_details')


class TaskUpdateView(View):
    def get(self, request, id, *args, **kwargs):
        task_object = Task.objects.get(id=id)
        form = TaskForm(instance=task_object)
        return render(request, 'tasks/update.html', {'form': form})

    def post(self, request, id):
        task_object = Task.objects.get(id=id)
        form = TaskForm(request.POST, instance=task_object)
        if form.is_valid():
            form.save()
            messages.success(request, "Data has been updated.")
            return redirect('tasks_details')
        else:
            messages.error(request, "Please, Enter valid data.")
            return redirect('tasks_update')


class TaskDeleteView(View):
    def get(self, request, id):
        task_object = Task.objects.get(id=id)
        task_object.delete()
        messages.success(request, "Data deleted successfully.")
        return redirect('tasks_details')


# -------------------------------- REST API -------------------------------------#
# API View to list al tasks, retrieve a single task, create a new task, update and existing tasks and delete a task.
# hit this api with postman

class TaskListView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
