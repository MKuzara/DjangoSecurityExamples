from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Post
from .forms import PostForm

# Create your views here.
class PostListView(ListView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'posts'
    template_name = 'examples/list.html'

class PostView(DetailView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'post'
    template_name = 'examples/post.html'

class PostNewView(CreateView):
    form_class = PostForm
    queryset = Post.objects.all()
    context_object_name = 'form'
    template_name = 'examples/form.html'

class PostUpdateView(UpdateView):
    form_class = PostForm
    queryset = Post.objects.all()
    context_object_name = 'form'
    template_name = 'examples/form.html'

class PostDeleteView(DeleteView):
    model = Post
    queryset = Post.objects.all()
    context_object_name = 'post'
    template_name = 'examples/delete_form.html'


def search(request):
    q = request.GET.get('q', '')
    context = {}
    if q:
        posts = Post.objects.filter(title__contains=q)
        context['q'] = q
        context['posts'] = posts

    return render(request, 'examples/search.html', context)
