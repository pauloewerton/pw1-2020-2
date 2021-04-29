from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'posts'

    ### Desconmente para filtrar posts por autor
    #def get_queryset(self):
    #    user = self.request.user
    #    return Post.objects.filter(author=user)

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post'

class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ('title', 'image', 'body')
    # login_url = 'login' # necessario no sistema customizado de autenticacao

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class BlogUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'image', 'body']

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.author != self.request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)

class BlogDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.author != self.request.user:
            raise PermissionDenied

        return super().dispatch(request, *args, **kwargs)

### Exemplo view com múltiplos modelos

#class BlogDetailView(DetailView):
#    template_name = 'post_detail.html'
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context['posts'] = Post.objects.all()
#        context['comments'] = Comment.objects.all()
#        return context