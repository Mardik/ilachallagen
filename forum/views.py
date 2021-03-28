from django.core.paginator import Paginator
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import Http404
from django.http import HttpResponse, HttpResponseNotFound 

from forum.models import Thread, Replie
from forum.forms import ReplieForm

# Create your views here.
class ThreadListView(ListView):
    model = Thread
    paginate_by = 20

# class ThreadDetailView(DetailView):
#     context_object_name = 'thread'
#     model = Thread

def thread_detail_view(request, pk):
    # if this is a POST request we need to process the form data
    try:
        thread = Thread.objects.get(pk=pk)
    except Thread.DoesNotExist:
        raise Http404("Thread does not exist")
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ReplieForm(request.POST)
        
        #check whether it's valid:
        if form.is_valid():
            text = form.cleaned_data['text']
            owner = form.cleaned_data['owner']
            replie = Replie()
            replie.text = text
            replie.owner = owner
            replie.thread = thread
            replie.save()
            form = ReplieForm()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReplieForm()
        
    return render(request, 'forum/thread_detail.html', {'thread': thread, 'form': form})

class ThreadCreateView(CreateView):
    model = Thread
    fields = ['title','text', 'owner']

class ThreadUpdateView(UpdateView):
    model = Thread
    fields = ['title','text']
    template_name = "forum/thread_form_update.html"
    
class ThreadDeleteView(DeleteView):
    model = Thread
    success_url = reverse_lazy('thread-list')

class ReplieDeleteView(DeleteView):
    model = Replie
    success_url = reverse_lazy('thread-list')

class ReplieUpdateView(UpdateView):
    model = Replie
    fields = ['text']