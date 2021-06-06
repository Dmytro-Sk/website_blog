from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

from .models import Post
from .forms import PostForm, EditPostForm


class BlogPageView(ListView):
    model = Post
    template_name = 'blog/main_page.html'
    ordering = ['-id']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'blog/update_post.html'
    form_class = EditPostForm

    def get_success_url(self):
        return reverse('blog:post-details', kwargs={'pk': self.object.pk})


class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete_post.html'
    success_url = reverse_lazy('blog:blog-page')
