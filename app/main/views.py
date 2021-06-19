# from .forms import CreateListForm
from .models import ToDoList
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.
class HomeView(TemplateView):
    template_name = 'main/home.html'

# To view the list of all Lists
class MyListView(ListView):
    template_name = 'main/mylist.html'
    context_object_name = 'list_name'
    
    def get_queryset(self):
        return ToDoList.objects.all()


class CreateList(CreateView):
    model = ToDoList
    fields = ['name']
    template_name = 'main/todolist_form.html'
     
class UpdateList(UpdateView):
    model = ToDoList
    fields = ['name']

class DeleteList(DeleteView):
    model = ToDoList
    success_url = reverse_lazy('main:home')


class DetailList(DetailView):
    model = ToDoList
    template_name = 'main/detail.html'
    context_object_name = 'list'
     
    
